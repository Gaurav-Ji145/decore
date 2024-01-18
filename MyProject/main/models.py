from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()


def __str__(self):
    return f"{self.name}{self.mobile_no}{self.email}{self.message}"
