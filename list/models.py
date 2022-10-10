from django.db import models

# Create your models here.
class Near_by(models.Model):
    near_by_place = models.CharField(max_length=200)
    def __str__(self):
        return self.near_by_place
class Near(models.Model):
    near = models.CharField(max_length=200)
    def __str__(self):
        return self.near 

class List(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    Hostel_Name = models.CharField(max_length=100)
    Description = models.TextField()
    Adress = models.TextField()
    nearby_hotels = models.ManyToManyField(Near_by, blank=True)
    nearby=models.ManyToManyField(Near,blank=True)
    is_completed = models.BooleanField(default=False)
    label = models.CharField(max_length=200)
    contact= models.IntegerField(default=0)
    priority = models.IntegerField(default=1)