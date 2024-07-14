from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()

class Testimonial(models.Model):
  name = models.CharField(max_length=100)
  designation = models.CharField(max_length=100)
  img = models.ImageField(upload_to='media')
  content = models.TextField()    

class Team(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)  
    img = models.ImageField(upload_to='media')
    content = models.TextField()