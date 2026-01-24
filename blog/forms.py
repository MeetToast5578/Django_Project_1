from django import forms
from .models import Comment, BLog


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = [
            'message'
        ]
        widgets = {
            'message' : forms.Textarea(attrs={
           
                
                'placeholder' : 'Message'
            })
        }
    
    
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
    