from django.shortcuts import render,HttpResponseRedirect, reverse

from product.models import Product, Variaton
from .models import Cart, CartItem

# Create your views here.

def cart(request):

    try:
        the_id = request.session['cart_id']  # if cart id exist grab it
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None
    
    if the_id:
        new_total = 0.00
        nav_total = 0
        for item in cart.cartitem_set.all(): # cartitem_set looks for the foreign key relation in CartItem
            line_total = float(item.product.price) * item.quantity
            new_total += line_total
            nav_total += item.quantity
        
        
        request.session['items_total'] = nav_total  # get the total amount of items in cart and we will use this 
                                                    # to display next to cart navbar the total amount in cart
       
        # request.session['items_total'] = cart.cartitem_set.count()
       
        cart.total = new_total
        cart.save()

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


def remove_from_cart(request, pk):
    try:
        the_id = request.session['cart_id'] # if cart id exist grab it
        cart = Cart.objects.get(id=the_id)
    except:
        return HttpResponseRedirect(reverse('cart'))
    
    cartitem = CartItem.objects.get(id=pk)
    # cartitem.delete()
    cartitem.cart = None
    cartitem.save()
    #send success message
    return HttpResponseRedirect(reverse('cart'))


def add_to_cart(request, pk):
   
    request.session.set_expiry(3600)    # cart will expire after 3600 seconds(1hr) but in administration(models)
                                        # it still exists and user will be logged out

    try:
        the_id = request.session['cart_id'] # if cart id exist grab it
    except:
        new_cart = Cart() # if it doesnt exist, create cart id
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    cart = Cart.objects.get(id=the_id) # use the cart id from above
    try:
        product = Product.objects.get(id=pk)  # grab product id
    except Product.DoesNotExist:
        pass
    except:
        pass



    product_var = [] #product variation
    if request.method == 'POST':
        qty = request.POST['qty']
        # size = request.POST['size']
        # color = request.POST['color']

        # print(qty)
        
        if int(qty) >= 1:
        
            for item in request.POST:
                key = item
                val = request.POST[key]
            
                try:
                    v = Variaton.objects.get(product=product, category__iexact=key, title__iexact=val)
                    product_var.append(v)
                except:
                    pass

            cart_item = CartItem.objects.create(cart=cart, product=product) # add items to the cart

            if len(product_var) > 0:
                cart_item.variations.add(*product_var)  #for item in product_var:
                                                        #cart_item.variations.add(item)
            cart_item.quantity = qty
            cart_item.save()
            # success message
            return HttpResponseRedirect(reverse('cart'))
    
    # error message    
    return HttpResponseRedirect(reverse('cart'))