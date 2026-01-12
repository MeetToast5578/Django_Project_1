from django import forms
from core.models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = [
            'first_name',
            'last_name',
            'email',
            'message'
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
            'email' : forms.EmailInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Email Address'
            }),
            'message' : forms.Textarea(attrs={
                'class' : 'form-control',
                
                'placeholder' : 'Message'
            })
        }

    def clean(self):
        value = self.cleaned_data['email']
        if not value.endswith('gmail.com'):
            raise forms.ValidationError('Email must be gmail.com')
        return self.cleaned_data