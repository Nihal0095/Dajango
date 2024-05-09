from django.db import models

# Create your models here.
class TeamDetails(models.Model):
    playername= models.CharField(max_length=30)
    playersurname=models.CharField(max_length=35)
    playerage=models.CharField(max_length=5)
    playerspeciality=models.CharField(max_length=20)