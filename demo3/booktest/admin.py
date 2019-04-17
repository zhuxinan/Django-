from django.contrib import admin

# Register your models here.

from .models import BookInfo,HeroInfo

class HeroInfoInline(admin.StackedInline):
    model = HeroInfo
    extra = 1

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['bookid','bookname','bookauthor','bookcontent']
    list_filter = ['bauthor',]
    search_fields = ['bauthor','id','bname']
    list_per_page = 2
    inlines = [HeroInfoInline]

admin.site.register(BookInfo,BookInfoAdmin)

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['heroid','heroname','herogender','herocontent']
    list_filter = ['hname','hgender','hcontent']
    search_fields = ['hname','hgender','hcontent']
    list_per_page = 2

admin.site.register(HeroInfo,HeroInfoAdmin)