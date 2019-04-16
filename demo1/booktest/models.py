from django.db import models

# Create your models here.

class Book(models.Model):
    bname = models.CharField(max_length=20)
    bcontent = models.CharField(max_length=100)
    bpub_date = models.DateTimeField()
    def __str__(self):
        return self.bname

class Hero(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=100)
    hbook = models.ForeignKey('Book',on_delete=models.CASCADE)
    def __str__(self):
        return self.hname

