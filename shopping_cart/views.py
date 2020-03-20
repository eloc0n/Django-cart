from django.shortcuts import render,HttpResponseRedirect, reverse

from product.models import Product
from .models import Cart, CartItem

# Create your views here.

def cart(request):

    try:
        # if cart id exist grab it
        the_id = request.session['cart_id']
    except:
        the_id = None

    if the_id:
        cart = Cart.objects.get(id=the_id)
        context = {
            'cart': cart,
        }
    else:
        empty_message = "Your cart is empty!"
        context = {
            'empty':True,
            'empty_message':empty_message,
        }
        

    return render(request, 'cart/cart.html', context)


def add_to_cart(request, pk):
    # cart will expire after 3600 seconds(1hr) but in administration(models)
    # it still exists and user will be logged out
    request.session.set_expiry(3600)

    try:
        qty = request.GET.get('qty')
        update_qty = True
    except:
        qty = None
        update_qty = False

    try:
        attr = request.GET.get('attr')
    except:
        attr = None
        
    print(attr)

    try:
        # if cart id exist grab it
        the_id = request.session['cart_id']
    except:
        # if it doesnt exist, create cart id
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    # use the cart id from above
    cart = Cart.objects.get(id=the_id)
    
    try:
        # grab product id
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        pass
    except:
        pass

    # add items to the cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if update_qty and qty:
        if int(qty) == 0:
            cart_item.delete()
        else:
            cart_item.quantity = qty
            cart_item.save()
    else:
        pass

    '''
    if not cart_item in cart.items.all():
        cart.items.add(cart_item)
    else:
        cart.items.remove(cart_item)
    '''

    new_total = 0.00
    # cartitem_set looks for the foreign key relation in CartItem
    for item in cart.cartitem_set.all():
        line_total = float(item.product.price) * item.quantity
        new_total += line_total
    
    # get the total amount of items in cart and we will use this 
    # to display next to cart navbar the total amount in cart
    request.session['items_total'] = cart.cartitem_set.count()
    
    cart.total = new_total
    cart.save()

    return HttpResponseRedirect(reverse('cart'))