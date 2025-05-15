from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model 

User = get_user_model()  #Gets customer user model defined in code

 # Extension of the user, allowed me to add in balance
class CustomUserCreationForm(UserCreationForm):
    balance = forms.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        initial=0.00, 
        required=False, 
        help_text="Set initial balance for the user."
    )

    class Meta:
        model = User  # Use the custom user model
        fields = ("username", "password1", "password2", "balance")
     #Here I am able to add username, password fields, and additional balance fields