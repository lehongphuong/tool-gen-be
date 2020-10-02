from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=255)
    createdate = models.DateField(auto_created=True) 

class Class(models.Model):
    idproject = models.IntegerField(default=0)
    classname = models.CharField(max_length=255)
    properties = models.TextField()
    attributes = models.TextField()
    lengths = models.TextField()

class CRUD(models.Model):
    idproject = models.IntegerField(default=0)
    idclass = models.IntegerField(default=0)
    actiontype = models.CharField(max_length=10)
    titles = models.TextField()
    properties = models.TextField()
    alias = models.TextField()
    refers = models.TextField()
    titlecreate = models.CharField(max_length=100)
    titleupdate = models.CharField(max_length=100)
    inputtypes = models.TextField()
    validates = models.TextField()
    formats = models.TextField() 
    createdate = models.DateField(auto_created=True) 

