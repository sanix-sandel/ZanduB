from django import forms
from .models import Product, Category
from django.shortcuts import get_object_or_404

class ProductForm(forms.ModelForm):

    class Meta:
        model=Product

        fields=('title', 'font_image', 'category', 'price', 'description')

    def save(self, commit=True):
        product=super().save(commit=False)
        title=self.cleaned_data['title']
        price=self.cleaned_data['price']
        description=self.cleaned_data['description']
        if commit:
            product.save()
        return product
