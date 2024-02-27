from django import forms
from .models import Comment
from .models import Product

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'photo']
