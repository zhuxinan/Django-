from django.db import models

# Create your models here.

class BookInfo(models.Model):
    bname = models.CharField(max_length=20)
    bauthor = models.CharField(max_length=20)
    bcontent = models.CharField(max_length=100)
    def __str__(self):
        return self.bname

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=100)
    def __str__(self):
        return self.hname