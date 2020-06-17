from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    category=forms.ModelMultipleChoiceField(
        label=('categries'),
        queryset=Category.objects.all(),

    )
    class Meta:
        model=Product
        fields=('title', 'font_image', 'price', 'description')

    def save(self, commit=True):
        product=super().save(commit=False)
        category=self.cleaned_data['category']
        title=self.cleaned_data['title']
        font_image=self.cleaned_data['font_image']
        price=self.cleaned_data['price']
        description=self.cleaned_data['description']
        if commit:
            product.save()
        return product
