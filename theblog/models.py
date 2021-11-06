from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    return 'blog/{0}/{1}'.format(instance.author.id, filename)
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    title_tag = models.CharField(max_length=50, default='Awkward Blog from Awkward Men', verbose_name='Title Tag')
    body = models.TextField(verbose_name='Content')
    image = models.ImageField(upload_to=user_directory_path, default='django.png')
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

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.user.username

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class DisLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
        
class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    



