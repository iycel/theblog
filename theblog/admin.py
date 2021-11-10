from django.contrib import admin
from .models import Category, Post, Comment, Like, DisLike, PostView

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(DisLike)
admin.site.register(PostView)


