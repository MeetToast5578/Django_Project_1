from django.contrib import admin
from .models import Comment, BLog, BlogTag
# Register your models here.

admin.site.register(Comment)
admin.site.register(BLog)
admin.site.register(BlogTag)