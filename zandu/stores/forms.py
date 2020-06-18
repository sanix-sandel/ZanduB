from django import forms
from .models import Store, Post

class StoreForm(forms.ModelForm):
    class Meta:
        model=Store
        fields=('title', 'cover_image', 'slogan', 'about', 'address')

    def save(self, commit=True):
        store=super().save(commit=False)
        title=self.cleaned_data['title']
        slogan=self.cleaned_data['slogan']
        about=self.cleaned_data['about']
        address=self.cleaned_data['address']
        if commit:
            store.save()
        return store

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('content',)

    def save(self, commit=True):
        post=super().save(commit=False)
        content=self.cleaned_data['content']
        if commit:
            post.save()
        return post        
