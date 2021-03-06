from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, ProductReview
from django.contrib import messages
from .forms import ProdReviewForm
from django.db.models import Avg
from django.contrib.auth.decorators import login_required
import sweetify


def all_prods(request):
    """Returns all products and their average ratings."""
    products = Product.objects.all()
    stars = Product.objects.annotate(
        avg_review=Avg('productreview__rating'),
    )
    context = {
        'products': products,
        'stars': stars
    }
    return render(request, "products.html", context)


def single_prod(request, pk):
    """Returns single product and its avergae rating."""
    product = get_object_or_404(Product, pk=pk)
    stars = Product.objects.filter(id=pk).annotate(
        avg_review=Avg('productreview__rating')
    )
    context = {
        'product': product,
        'stars': stars,
    }
    return render(request, 'aproduct.html', context)


@login_required()
def review_prod(request, pk):
    """
    Allows user to add a review for a product and checks if they've already
    reviewed it. Returns them to product page with a sweetify alert depending
    on whether they have or not successfully added a review.
    """
    product = get_object_or_404(Product, pk=pk)
    user = request.user
    if request.method == "POST":
        if ProductReview.objects.filter(user=user, product=product).exists():
            form = ProdReviewForm(request.POST)
            sweetify.error(
                request,
                "Already reviewed this product",
                icon='info',
                timer='2500',
                toast='true',
                position='center',
                background='#181818',
            )
            return redirect(single_prod, product.pk)
        else:
            form = ProdReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.product = product
                form.instance.user = request.user
                review.save()
                sweetify.success(
                    request,
                    "Review added, thanking you",
                    icon='success',
                    timer='2500',
                    toast='true',
                    position='top',
                )
                return redirect(single_prod, product.pk)
    else:
        form = ProdReviewForm()
    return render(request, 'prodreview.html', {
        'form': form, 'product': product.pk
        }
    )


@login_required()
def edit_review_prod(request, pk):
    """Edits a previous review a user had for a product."""
    review = get_object_or_404(ProductReview, pk=pk)
    product = review.product_id
    if request.method == "POST":
        form = ProdReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            form.instance.user = request.user
            review.save()
            sweetify.success(
                request,
                "Review updated",
                icon='success',
                timer='2500',
                toast='true',
                position='top',
            )
            return redirect(single_prod, product)
    else:
        form = ProdReviewForm(instance=review)

    return render(request, 'editprodreview.html', {
        'form': form, 'product': product
        }
    )


@login_required()
def delete_prod_review(request, pk):
    """Deletes a previous review a user had for a product."""
    review = get_object_or_404(ProductReview, pk=pk)
    product = review.product_id
    if review.user == request.user:
        review.delete()
        sweetify.success(
            request,
            "Review deleted",
            icon='success',
            timer='2500',
            toast='true',
            position='center',
            background='#181818',
        )
        return redirect(single_prod, product)


def apparel(request):
    """Returns a view of all apparel products nad their ratings."""
    results = Product.objects.filter(category__icontains='A')
    stars = Product.objects.annotate(
        avg_review=Avg('productreview__rating'),
    )
    context = {
        'products': results,
        'stars': stars
    }
    if not results:
        messages.error(request, "No apparel as of yet, that will change soon!")
        return redirect(reverse('products'))
    else:
        return render(request, "products.html", context)


def plans(request):
    """Returns a view of all plans nad their ratings."""
    results = Product.objects.filter(category__icontains='P')
    stars = Product.objects.annotate(
        avg_review=Avg('productreview__rating'),
    )
    context = {
        'products': results,
        'stars': stars
    }
    if not results:
        messages.error(request, "No plans as of yet, that will change soon!")
        return redirect(reverse('products'))
    else:
        return render(request, "products.html", context)


def sort(request):
    """Sorts all products view either alphabeticaly or by price."""
    stars = Product.objects.annotate(
        avg_review=Avg('productreview__rating'),
    )
    select = request.GET['sort']
    if select == 'LtoH':
        results = Product.objects.order_by('price')
        return render(request, "products.html",
        {"products": results, 'stars': stars})
    elif select == 'HtoL':
        results = Product.objects.order_by('-price')
        return render(request, "products.html",
        {"products": results, 'stars': stars})
    elif select == 'AtoZ':
        results = Product.objects.order_by('name')
        return render(request, "products.html",
        {"products": results, 'stars': stars})
    elif select == 'ZtoA':
        results = Product.objects.order_by('-name')
        return render(request, "products.html",
        {"products": results, 'stars': stars})


def sort_apparel(request):
    """
    Sorts apparel view of products either alphabeticaly or by price.
    """
    stars = Product.objects.annotate(
        avg_review=Avg('productreview__rating'),
    )
    select = request.GET['sorta']
    items = Product.objects.filter(category__icontains='A')
    if select == 'LtoH':
        results = items.order_by('price')
        return render(request, "products.html",
        {"products": results, 'stars': stars})
    elif select == 'HtoL':
        results = items.order_by('-price')
        return render(request, "products.html",
        {"products": results, 'stars': stars})
    elif select == 'AtoZ':
        results = items.order_by('name')
        return render(request, "products.html",
        {"products": results, 'stars': stars})
    elif select == 'ZtoA':
        results = items.order_by('-name')
        return render(request, "products.html",
        {"products": results, 'stars': stars})


def sort_plans(request):
    """
    Sorts view of plan products either alphabeticaly or by price.
    """
    stars = Product.objects.annotate(
        avg_review=Avg('productreview__rating'),
    )
    select = request.GET['sortp']
    items = Product.objects.filter(category__icontains='P')
    if select == 'LtoH':
        results = items.order_by('price')
        return render(request, "products.html",
        {"products": results, 'stars': stars})
    elif select == 'HtoL':
        results = items.order_by('-price')
        return render(request, "products.html",
        {"products": results, 'stars': stars})
    elif select == 'AtoZ':
        results = items.order_by('name')
        return render(request, "products.html",
        {"products": results, 'stars': stars})
    elif select == 'ZtoA':
        results = items.order_by('-name')
        return render(request, "products.html",
        {"products": results, 'stars': stars})
