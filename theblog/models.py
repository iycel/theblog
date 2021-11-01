from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    title_tag = models.CharField(max_length=50, default='Awkward Blog from Awkward Men', verbose_name='Title Tag')
    body = models.TextField(verbose_name='Content')
    image = models.ImageField(upload_to='post_pic', blank=True, verbose_name='Image')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Login User')
    post_date = models.DateField(auto_now_add=True)
    CATEGORY = {
        ('c1', 'Cat c1'),
        ('c2', 'Cat c2')
    }

    category = models.CharField(choices=CATEGORY,max_length=50, verbose_name='Category')
    
    STATUS = {
        ('s1', 'Sta s1'),
        ('s2', 'Sta s2')
    }

    status= models.CharField(max_length=50, choices=STATUS, verbose_name='Status')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse("post_details", args=(str(self.id)))
    
    class META :
        ordering = ['-post_date']
    



