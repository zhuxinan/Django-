from django.contrib import admin

# Register your models here.
from .models import Questions,Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 1

class QuestionsAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['Qid','Qquestion']

admin.site.register(Questions,QuestionsAdmin)

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['Cid','Coption','Cvote']


admin.site.register(Choice,ChoiceAdmin)
