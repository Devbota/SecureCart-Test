from django.db import models
from django.contrib.auth.models import AbstractUser

#I Extended User model to add balance   
class Userbalance(AbstractUser):
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    #troubleshooting section, allowed me to fix conflicts
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="userbalance_set",  #Fix clashes with Django default configurations
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="userbalance_set",  # Fix clashes with Django's default permissions system
        blank=True
    )

    def __str__(self):
        return self.username

#class shows products availanle in the store
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (£)")
    stock = models.IntegerField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name

#Customer's order
class Order(models.Model):
    user = models.ForeignKey(Userbalance, on_delete=models.CASCADE) 
    product = models.ForeignKey(Product, on_delete=models.CASCADE) #used this tpo store products associated with current order
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=50, default='Shipped') #order status set to default for testing purposes
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
    
    #I created this as  string representation of the order

#Items added to the cart stored here before chekcout
class Cart(models.Model):
    user = models.ForeignKey(Userbalance, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in {self.user.username}'s cart"
    #I created this as  string representation of the item in cart

 

