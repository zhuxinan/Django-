from django.db import models

# Create your models here.

class Questions(models.Model):
    question = models.CharField(max_length=100)
    qpub_date = models.DateTimeField()
    def __str__(self):
        return self.question
    def Qid(self):
        return self.id
    Qid.short_description = '问题编号'

    def Qquestion(self):
        return self.question
    Qquestion.short_description = '问题'

class Choice(models.Model):
    choice = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    questions = models.ForeignKey(Questions,on_delete=models.CASCADE)
    def __str__(self):
        return self.choice
    def Cid(self):
        return self.id
    Cid.short_description = '选项编号'

    def Coption(self):
        return self.choice
    Coption.short_description = '选项'

    def Cvote(self):
        return self.votes
    Cvote.short_description = '选项选票'
