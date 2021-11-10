from django.urls import path
from .views import post_add, post_delete, post_dislike, post_like, post_list, post_details, post_update 

app_name = 'theblog'
urlpatterns = [
    path('', post_list, name='home'),
    path('details/<int:id>/', post_details, name='details'),
    path('newpost/', post_add, name='newpost'),
    path('update/<int:id>/', post_update, name='post_update'),
    path('delete/<int:id>/', post_delete, name='post_delete'),
    path('like/<int:id>/', post_like, name='post_like'),
    path('dislike/<int:id>/', post_dislike, name='post_dislike'),
]


