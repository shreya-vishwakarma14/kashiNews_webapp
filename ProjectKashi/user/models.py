from django.db import models


# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=25)
    Email = models.CharField(max_length=30)
    Number = models.CharField(max_length=12)
    DOB = models.DateField()
    Password = models.CharField(max_length=25)
    ConfirmPassword = models.CharField(max_length=25)

    def __str__(self):
        return self.Name
