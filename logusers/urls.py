from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'logusers'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),  #https://docs.djangoproject.com/en/3.2/topics/auth/default/#using-the-views
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
