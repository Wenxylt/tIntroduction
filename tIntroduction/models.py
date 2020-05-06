from django.db import models

class Member(models.Model):
    identifier = models.CharField(max_length=20, primary_key=True)
    fullname = models.CharField(max_length=20)
    extra = models.CharField(max_length=200, null=True)
    profilename = models.CharField(max_length=100, null=True)
