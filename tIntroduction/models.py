from django.db import models

class Member(models.Model):
    fullname = models.CharField(max_length=20, primary_key=True)
    extra = models.CharField(max_length=200, null=True)
    intro = models.CharField(max_length=100, null=True)
    profilename = models.CharField(max_length=100, null=True)
