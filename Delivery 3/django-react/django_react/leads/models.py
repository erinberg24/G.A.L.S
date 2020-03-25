from django.db import models

# Create your models here.
class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    eagleid = models.CharField(max_length=8)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
