from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
import stripe


stripe.api_key = settings.STRIPE_SECRET


@login_required()
def delivery(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            request.session['form_data_page_1'] = order_form.cleaned_data
            return redirect('checkout')
    else:
        order_form = OrderForm(request.session['form_data_page_1'])
    return render(request, "deliver.html", {"order_form": order_form})

# @login_required()
# def verify_delivery(request, content):
#     return render(request, 'myapp/verify_content.html', {'content' : content})


@login_required()
def checkout(request):
    deliv_details = request.session['form_data_page_1']
    order_form = OrderForm(deliv_details)
    if request.method == "POST":
        # order_form = request.session['order_form']
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            del_total = 0

            for id, content in cart.items():
                product = get_object_or_404(Product, pk=id)
                cat = Product.objects.filter(id=id, category__icontains='A')
                if cat:
                    del_total = 5
                for size, quantity in content.items():
                    total += quantity * product.price
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save()
            total = del_total + total
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.success(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect(reverse('home'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "Unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        

    return render(request, "checkout.html", {
        "order_form": order_form,
        "payment_form": payment_form,
        "publishable": settings.STRIPE_PUBLISHABLE
        })
