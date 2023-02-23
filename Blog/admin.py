from django.contrib import admin
from .models import Post
from .models import BlogComment

admin.site.register(Post)
admin.site.register(BlogComment)