from django import forms
from .models import Comment, BLog


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
           
                'placeholder' : 'Name'
            }),
            'subject' : forms.TextInput(attrs={
           
                'placeholder' : 'Subject'
            }),
            'email' : forms.EmailInput(attrs={
           
                'placeholder' : 'Email Address'
            }),
            'message' : forms.Textarea(attrs={
           
                
                'placeholder' : 'Message'
            })
        }

    def clean(self):
        value = self.cleaned_data['email']
        if not value.endswith('gmail.com'):
            raise forms.ValidationError('Email must be gmail.com')
        return self.cleaned_data
    
    
class BlogForm(forms.ModelForm):

    class Meta:
        model = BLog
        fields = [
            'title',
            'content',
            'cover_image'
        ]
        widgets = {
            'title' : forms.TextInput(attrs={
                'placeholder' : 'Title'
            }),
            'content' : forms.Textarea(attrs={
                'placeholder' : 'Content'
            }),
        }
    