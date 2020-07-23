from django.db import models

# Create your models here.

"""Import episodes"""
class Episode(models.Model):
	epname = models.TextField()
	epdesc = models.TextField()
	season = models.IntegerField()
	epnum = models.IntegerField()



