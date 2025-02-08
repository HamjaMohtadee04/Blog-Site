from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    publish_date =models.DateField()

class Comment(models.Model):
    commentContent = models.TextField() 

