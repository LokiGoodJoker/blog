from django.contrib import admin
from blog.models import Post, Tag # наша модель из blog/models.py

admin.site.register(Post)
admin.site.register(Tag)