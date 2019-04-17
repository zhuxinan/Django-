from django.db import models

# Create your models here.

class BookInfo(models.Model):
    bname = models.CharField(max_length=20)
    bauthor = models.CharField(max_length=20)
    bcontent = models.CharField(max_length=100)
    def __str__(self):
        return self.bname
    def bookname(self):
        return self.bname
    bookname.short_description = '书籍名称'
    def bookauthor(self):
        return self.bauthor
    bookauthor.short_description = '书籍作者'
    def bookcontent(self):
        return self.bcontent
    bookcontent.short_description = '书籍简介'
    def bookid(self):
        return self.id
    bookid.short_description = '书籍编号'

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=100)
    hbook = models.ForeignKey('BookInfo',on_delete=models.CASCADE)
    def __str__(self):
        return self.hname
    def heroname(self):
        return self.hname
    heroname.short_description = '人物名称'
    def herogender(self):
        return self.hgender
    herogender.short_description = '人物性别'
    def herocontent(self):
        return self.hcontent
    herocontent.short_description = '人物简介'
    def heroid(self):
        return self.id
    heroid.short_description = '人物编号'