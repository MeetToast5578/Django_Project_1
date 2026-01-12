from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = [
            'name',
            'email',
            'subject',
            'message'
        ]
        widgets = {
            'name' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Name'
            }),
            'subject' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Subject'
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