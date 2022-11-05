from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField('data published')
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    email = models.EmailField(max_length=254, blank=True)
    url = models.URLField(max_length=200, blank=True)
    hashtags = models.ManyToManyField('Hashtag', blank = True)
    post_like = models.ManyToManyField(User, related_name='like_users', blank=True)
    like_count = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    def __str__(self):
        return self.comment
    
    postid = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=True)
    text = models.CharField(max_length=50)

class Hashtag(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name