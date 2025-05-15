from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Product, Order, Userbalance #models which will be utilised in admin panel


#Allows admin to customise product
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

#Allows admin to customise Order and user
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'status', 'created_at')


#Allows admin to change the balance of customer
class UserBalanceAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Financial Information', {'fields': ('balance',)}),
    )    

#Registration for the models 
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Userbalance, UserBalanceAdmin)



