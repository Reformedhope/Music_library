from django.db import models

# Create your models here.
#This is where we are going to create representations of our table in the database. which is were we will define them
#creating the model first is called the code first approch with backend, Than the table will create auto based on the class. 

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    release_date = models.DateField(null=True)
    genre = models.CharField(max_length=255)
    likes = models.IntegerField()
    
