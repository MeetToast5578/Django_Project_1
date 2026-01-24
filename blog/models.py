from django.db import models
from core.models import AbstractModel
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class BlogTag(AbstractModel):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class BLog(AbstractModel):
    user = models.ForeignKey(User,related_name='blogs', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    cover_image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    content = models.TextField()
    slug = models.SlugField(null=True, blank=True)
    tags = models.ManyToManyField(BlogTag, related_name='blogs', blank=True)

    def __str__(self):
        return f'Blog by {self.user.username} - {self.title}'
    
    class Meta:
        verbose_name_plural = 'Blogs'
        ordering = ("-created_at",)


class Comment(AbstractModel):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    blog = models.ForeignKey(BLog, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment by {self.name}'