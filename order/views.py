import time

from django.shortcuts import render, HttpResponseRedirect, reverse


from .models import Order
from shopping_cart.models import Cart

# Create your views here.
def checkout(request):

    try:
        # if cart id exist grab it
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None
        return HttpResponseRedirect(reverse('cart'))
    
    new_order, created = Order.objects.get_or_create(cart=cart)
    
    if created:
        # assign a user to the order
        # assign an address
        new_order.order_id = str(time.time())
        new_order.save()
        
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
