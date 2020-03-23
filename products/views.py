from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product
from django.contrib import messages
from .forms import ProdReviewForm


def all_prods(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def single_prod(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'aproduct.html', {'product': product})


def review_prod(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProdReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            form.instance.user = request.user
            review.save()
            messages.success(request, "Review Added")
            # return redirect('aproduct.html', product.pk)
            return redirect(reverse('products'))
    else:
        form = ProdReviewForm()
    return render(request, 'prodreview.html', {'form': form})


def apparel(request):
    results = Product.objects.filter(category__icontains='apparel')
    if not results:
        messages.error(request, "no results for your search")
        return redirect(reverse('products'))
    else:
        return render(request, "prods-apparel.html", {"products": results})


def plans(request):
    results = Product.objects.filter(category__icontains='plan')
    if not results:
        messages.error(request, "no results for your search")
        return redirect(reverse('products'))
    else:
        return render(request, "prods-plans.html", {"products": results})


def sort(request):
    select = request.GET['sort']
    if select == 'LtoH':
        results = Product.objects.order_by('price')
        if not results:
            messages.error(request, "no results for your search")
            return redirect(reverse('products'))
        else:
            return render(request, "products.html", {"products": results})
    elif select == 'HtoL':
        results = Product.objects.order_by('-price')
        if not results:
            messages.error(request, "no results for your search")
            return redirect(reverse('products'))
        else:
            return render(request, "products.html", {"products": results})
    elif select == 'AtoZ':
        results = Product.objects.order_by('name')
        if not results:
            messages.error(request, "no results for your search")
            return redirect(reverse('products'))
        else:
            return render(request, "products.html", {"products": results})
    elif select == 'ZtoA':
        results = Product.objects.order_by('-name')
        if not results:
            messages.error(request, "no results for your search")
            return redirect(reverse('products'))
        else:
            return render(request, "products.html", {"products": results})


def sort_apparel(request):
    select = request.GET['sorta']
    items = Product.objects.filter(category__icontains='apparel')
    if select == 'LtoH':
        results = items.order_by('price')
        if not results:
            messages.error(request, "no results for your search")
            return redirect(reverse('products'))
        else:
            return render(request, "prods-apparel.html", {"products": results})
    elif select == 'HtoL':
        results = items.order_by('-price')
        if not results:
            messages.error(request, "no results for your search")
            return redirect(reverse('products'))
        else:
            return render(request, "prods-apparel.html", {"products": results})
    elif select == 'AtoZ':
        results = items.order_by('name')
        if not results:
            messages.error(request, "no results for your search")
            return redirect(reverse('products'))
        else:
            return render(request, "prods-apparel.html", {"products": results})
    elif select == 'ZtoA':
        results = items.order_by('-name')
        if not results:
            messages.error(request, "no results for your search")
            return redirect(reverse('products'))
        else:
            return render(request, "prods-apparel.html", {"products": results})


def sort_plans(request):
    select = request.GET['sortp']
    items = Product.objects.filter(category__icontains='plan')
    if select == 'LtoH':
        results = items.order_by('price')
        if not results:
            messages.error(request, "no results for your search")
            return redirect(reverse('products'))
        else:
            return render(request, "prods-plans.html", {"products": results})
    elif select == 'HtoL':
        results = items.order_by('-price')
        if not results:
            messages.error(request, "no results for your search")
            return redirect(reverse('products'))
        else:
            return render(request, "prods-plans.html", {"products": results})
    elif select == 'AtoZ':
        results = items.order_by('name')
        if not results:
            messages.error(request, "no results for your search")
            return redirect(reverse('products'))
        else:
            return render(request, "prods-plans.html", {"products": results})
    elif select == 'ZtoA':
        results = items.order_by('-name')
        if not results:
            messages.error(request, "no results for your search")
            return redirect(reverse('products'))
        else:
            return render(request, "prods-plans.html", {"products": results})
