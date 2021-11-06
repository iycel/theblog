from django.urls import path
from .views import home, post_add, post_delete, post_list, post_details, post_update 

app_name = 'theblog'
urlpatterns = [
    # path('', home, name='home'),
    path('', post_list, name='list'),
    path('details/<int:id>/', post_details, name='details'),
    path('newpost/', post_add, name='newpost'),
    path('update/<int:id>/', post_update, name='post_update'),
    path('delete/<int:id>/', post_delete, name='post_delete'),
]


