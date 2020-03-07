from django import forms
from .models import Orders,Customers,Products
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields =['customer','product','status']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields= ['name','email','mobile']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields =['name','price','category','description']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']