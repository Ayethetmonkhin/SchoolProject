from django.db import models

# Create your models here.
class Course(models.Model):
    photo = models.ImageField(upload_to='photo')
    name = models.CharField(max_length=255)
    fee = models.PositiveIntegerField(default=0)
    description = models.TextField()

class Teacher(models.Model):
    photo = models.ImageField(upload_to='photo')
    name = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    description = models.TextField()