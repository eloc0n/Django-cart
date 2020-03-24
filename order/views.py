#import time

from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required

from .models import Order
from shopping_cart.models import Cart
from .utils import id_generator
# Create your views here.

def orders(request):

    context = {

    }

    return render(request, 'orders/user.html', context)


@login_required # require user login
def checkout(request):
    try:
        the_id = request.session['cart_id'] # if cart id exist grab it
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None
        return HttpResponseRedirect(reverse('cart'))
    
    try:
        new_order = Order.objects.get(cart=cart)
    except Order.DoesNotExist:
        new_order = Order()
        new_order.cart = cart
        new_order.user = request.user   # assign a user to the order
        new_order.order_id = id_generator()                                                         
        new_order.save()
    except:
        # error message
        return HttpResponseRedirect(reverse('cart'))

    # assign an address    
    # run credit card
    if new_order.status == 'Finished':
        del request.session['cart_id']
        del request.session['items_total']
        return HttpResponseRedirect(reverse('cart'))
    
    empty_message = "Your order has been sent and its being processed"
       
    context = {
        'empty':True,
        'empty_message':empty_message,
        # 'new_order':new_order,
    }

    return render(request, 'cart/cart.html', context)
