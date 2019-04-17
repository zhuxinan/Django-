from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import BookInfo,HeroInfo
from django.template import loader,RequestContext

def index(request):
    # return HttpResponse('首页')
    template = loader.get_template('booktest/index.html')
    result = template.render({'username':'zxa'})
    return HttpResponse(result)

def list(request):
    # return HttpResponse('列表页')
    book = BookInfo.objects.all()
    return render(request,'booktest/list.html',{"booklist":book})

def detail(request,id):
    # try:
    #     book = BookInfo.objects.get(pk=int(id))
    #     return HttpResponse(book)
    # except:
    #     return HttpResponse('id不对，请重新输入')
    book = BookInfo.objects.get(pk = id)
    return render(request,'booktest/detail.html',{"book":book})
