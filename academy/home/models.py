from django.db import models
import datetime

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100, default="None")
    duration = models.CharField(max_length=100, default="None")
    img = models.ImageField(upload_to='pics')
    def __str__(self):
        return self.name

class Gallery(models.Model):
    name = models.CharField(max_length=100, default="None")
    img = models.ImageField(upload_to='pics')
    def __str__(self):
        return self.name
class Slider(models.Model):
    name = models.CharField(max_length=100, default="None")
    img = models.ImageField(upload_to='pics')
    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=22, default="None")
    feedback = models.CharField(max_length=250, default="None")
    about = models.CharField(max_length=20, default="None")
    img = models.ImageField(upload_to='pics')
    def __str__(self):
        return self.name

class Blog(models.Model):
    date = models.DateField(default= "None")
    title = models.CharField(max_length=35, default="None")
    img = models.ImageField(upload_to='pics')
    summary = models.CharField(max_length=1000, default="None")
    def __str__(self):
        return self.title
