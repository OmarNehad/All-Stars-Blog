from django.db import models
# from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse



# User = get_user_model()
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    # slug = models.SlugField(allow_unicode=True,unique=True,blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to ='images',blank=True)

    def __str__(self):
        return self.name

    # def save(self,*args,**kwargs):
    #     self.slug = slugify(self.name)
    #     super().save(*args,**kwargs)

class Event(models.Model):
    # user = models.ForeignKey(User)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    summary = models.TextField()
    release_date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


    # def get_absolute_url(self):
    #     return reverse('events:single', kwargs={'pk':self.pk})

    class Meta:
        ordering = ['-created_date']

class Comment(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE, related_name='comments')
    # user = models.ForeignKey(User)
    name = models.CharField(max_length=20)
    email_adress = models.EmailField()
    body = models.TextField()
    created_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('events:single', kwargs={'pk':self.event.pk})


class EventImage(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to ='images')

    def __str__(self):
        return self.event.title + ' image'

class EventVideo(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE, related_name='videos')
    video = models.FileField(upload_to ='videos')

    def __str__(self):
        return self.event.title + ' video'
