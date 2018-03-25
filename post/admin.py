# Register your models here.
from django.contrib import admin
from .models import Post, PostLog

admin.site.register(Post)
admin.site.register(PostLog)
