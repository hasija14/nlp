from django.db import models
import datetime
# Create your models here.
class UserInfo(models.Model):
    Name=models.CharField(max_length=25)
    DOB=models.DateField()
    Email=models.EmailField()
    Contact=models.IntegerField()


    def __str__(self):
        return self.Name
