from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model
from django import forms


class UserCreationForm(forms.ModelForm):
    password1=forms.CharField(label='Mot de Passe', widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirmation de Mot passe',
                                widgets=forms.PasswordInput)

    class Meta:
        model=get_user_model()
        fields=('username', 'email')

    def clean_password2(self):
        password1=self.cleaned_data.get('password1')
        password2=self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Les mots de passe ne correspondent pas")
        return password2

    def save(self, commit=True):
        user=super().save(commit=False)
        user.set_apssword(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password=ReadOnlyPasswordHashField()

    class Meta:
        model=get_user_model()
        fields=('username', 'email')#city,
