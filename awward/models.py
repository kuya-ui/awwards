from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    dpic = models.ImageField(upload_to = 'images/')
    bio = models.TextField(max_length=1000)
    info = models.TextField(max_length=5000)

class Projects(models.Model):
    title = models.CharField(max_length=500)
    description=models.TextField(max_length=2000)
    link=models.URLField()
    image=models.ImageField(upload_to='images/')
    user = models.ForeignKey(User,on_delete = models.CASCADE)

class Ratings(models.Model):
    design = models.IntegerField(default=1)
    usability = models.IntegerField(default=1)
    content = models.IntegerField(default=1)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    project_id = models.ForeignKey(Projects,on_delete=models.CASCADE)

class Comments(models.Model):
    project_id = models.ForeignKey(Projects,on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    user = models.ForeignKey(User,on_delete = models.CASCADE)