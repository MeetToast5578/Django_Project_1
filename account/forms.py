from django import forms
from django.contrib.auth import get_user_model
from .models import Address

User = get_user_model()



class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'profile_image',
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }


class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = [
            'street',
            'city',
            'state',
            'zip_code',
            'country',
        ]
        widgets = {
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
        }

class LoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Password'
    }))


class RegisterForm(forms.ModelForm):

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Confirm Password'
    }))

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'phone',
            'profile_image',
            'password',
        ]
        widgets = {
            'first_name' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'First Name'
            }),
            'last_name' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Last Name'
            }),
            'username' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Username'
            }),
            'email' : forms.EmailInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Email'
            }),
            'phone' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Phone'
            }),
            'password' : forms.PasswordInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Password'
            }),

        }

    # def save(self, commit = ...):
    #     user = super().save(commit)
    #     user.set_password(self.cleaned_data['password'])
    #     user.save()

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Passwords must match!!!')