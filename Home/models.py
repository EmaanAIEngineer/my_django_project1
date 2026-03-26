from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name= models.CharField(max_length=122)
    email= models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    message=models.TextField()
def __str__(self):
    return self.name

