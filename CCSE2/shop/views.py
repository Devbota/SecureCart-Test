from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart, Order #using same models created in views
from django.contrib.auth.decorators import login_required #makes sure views require authentication
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model #retrival of created user model

User = get_user_model() 

# View all products
def product_list(request):
    products = Product.objects.all() #Ensure this fetches all products
    return render(request, 'shop/product_list.html', {'products': products})

#Displays detail of specific product
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'shop/product_detail.html', {'product': product})

#Handling registration for user
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login")  # Redirect to login after successful signup
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/signup.html", {"form": form})



#Adding products to User's cart
@login_required #requires login to access data
def add_to_cart(request, product_id): #adds into cart data from database
    product = get_object_or_404(Product, id=product_id) 
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product) #gets product
    if not created:
        cart_item.quantity += 1 #incraments the cart
        cart_item.save()
    return redirect('cart')

#Details item in user's cart
@login_required
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'shop/cart.html', {'cart_items': cart_items})

#Handles checkout process and payment for user
@login_required
def checkout(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    total_cost = sum(item.product.price * item.quantity for item in cart_items)

    if request.method == "POST":
        if user.balance >= total_cost:  #Check if user has enough money
            user.balance -= total_cost  #Deduct money from user balance
            user.save()

            for item in cart_items:
                Order.objects.create(user=user, product=item.product, quantity=item.quantity)
                item.product.stock -= item.quantity  #Reduce product stock
                item.product.save()

            cart_items.delete()  #Clear cart after successful checkout
            return redirect('order_history')
        else:
            return render(request, 'shop/checkout.html', {
                'cart_items': cart_items,
                'error': "Insufficient balance! Please add more funds."
            })

    return render(request, 'shop/checkout.html', {'cart_items': cart_items, 'balance': user.balance})
#Showcases user's past order history
@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'shop/order_history.html', {'orders': orders})
