from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .forms import CommentForm, BlogForm
from .models import BLog
from django.contrib import messages

# Create your views here.

def blog_single(request, slug):
    blog = get_object_or_404(BLog, slug=slug)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(data = request.POST)
        print(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            messages.add_message(request, messages.SUCCESS, "Successfully Sent!")
            return redirect(reverse_lazy('blog_single', kwargs={'slug': blog.slug}))
    context = {
        'form' : form,
        'blog' : blog
    }
    return render(request, 'blog-single.html', context)


def blog(request):
    blogs = BLog.objects.all()
    context = {
        'blogs' : blogs
    }
    return render(request, 'blog.html', context)

def blog_create(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(data = request.POST, files = request.FILES)
        print(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            form.save_m2m()  # Save many-to-many relationships (tags)
            messages.add_message(request, messages.SUCCESS, "Blog Successfully Created!")
            return redirect(reverse_lazy('blog', ))
    context = {
        'form' : form
    }
    
    return render(request, 'blog-create.html', context)