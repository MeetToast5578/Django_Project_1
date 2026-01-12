from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()



class ProfileForm(forms.ModelForm):

    fullname = forms.CharField(max_length=200, widget= forms.TextInput(attrs={
        'class' : 'form-control'
    }))

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
            'email' : forms.EmailInput(attrs={
                'class' : 'form-control'
            }),
            'phone' : forms.TextInput(attrs={
                'class' : 'form-control'
            }),
        }

    def save(self, commit = ...):
        user = super().save(commit)
    
        user.save()

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