from django.contrib import admin

# Register your models here.
from blog_api.models import Post, Comment, Category, PostImages

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(PostImages)