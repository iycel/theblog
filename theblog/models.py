from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    title_tag = models.CharField(max_length=50, default='Awkward Blog from Awkward Men', verbose_name='Title Tag')
    body = models.TextField(verbose_name='Content')
    image = models.ImageField(upload_to='post_pic', blank=True, verbose_name='Image')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Login User')
    post_date = models.DateTimeField(auto_now_add=True)
    
    STATUS = {
        ('d', 'Draft'),
        ('p', 'Published')
    }

    status= models.CharField(max_length=50, choices=STATUS, verbose_name='Status', default="d")

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    # def get_absolute_url(self):
    #     return reverse("post_details", args=(str(self.id)))
    
    # class Meta :
    #     ordering = ['-post_date']

    



