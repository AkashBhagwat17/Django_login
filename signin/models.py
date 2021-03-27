from django.db import models

# Create your models here.
class SignIn(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    date = models.DateField()

    def __str__(self):
        return self.username