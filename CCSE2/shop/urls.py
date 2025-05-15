from django.urls import path #path function used to help me define URL patterns
from .views import product_list
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'), #products on homepage
    path('product/<int:product_id>/', views.product_detail, name='product_detail'), 
    path('cart/', views.view_cart, name='cart'), #Displays customer's shopping cart
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),  #adds item to cart
    path('checkout/', views.checkout, name='checkout'), #neccessary for checking out within my program
    path('orders/', views.order_history, name='order_history'), #screen showing past orders of user logged in
]
