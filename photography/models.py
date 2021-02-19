from django.db import models

# Create your models here.
class Pic(models.Model):
    pic_name = models.CharField(max_length=50,blank=True)
    pic_id = models.IntegerField()
    thumbnail = models.ImageField(blank=True)

    def __str__(self):
        return self.pic_name

class Message(models.Model):
    sender = models.CharField(max_length=50,blank=True)
    email = models.EmailField(max_length=50,blank=True)
    content = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.sender
