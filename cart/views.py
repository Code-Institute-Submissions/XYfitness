from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.views import single_prod


@login_required
def view_cart(request):
    return render(request, "cart.html")


@login_required
def cart_add(request, id):
    quantity = int(request.POST.get('quantity'))

    if quantity:
        cart = request.session.get('cart', {})
        if id in cart:
            cart[id] = (int(cart[id]) + quantity)
        else:
            cart[id] = cart.get(id, quantity)

        request.session['cart'] = cart
        messages.success(request, "Item added to cart")
        return redirect(single_prod, id)

    else:
        return redirect(reverse('products'))


@login_required
def change_cart(request, id):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    messages.success(request, "Cart updated")
    return redirect(reverse('view_cart'))
