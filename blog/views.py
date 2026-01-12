from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import CommentForm
from django.contrib import messages

# Create your views here.

def blog_single(request):
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(data = request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.WARNING, "Successfully Sent!")
            return redirect(reverse_lazy('blog_single'))
    context = {
        'form' : form
    }
    return render(request, 'blog-single.html', context)