from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader,RequestContext
from .models import Questions,Choice


def index(request):
    # return HttpResponse("投票管理")
    # template = loader.get_template('vote/index.html')
    # questions = Questions.objects.all()
    # result = template.render({"questions":questions})
    # return HttpResponse(result)
    question = Questions.objects.all()
    context = {'questions':question}
    return render(request,'vote/index.html',context)


def detail(request,id):
    # return HttpResponse("投票详情")
    question = Questions.objects.get(pk=id)
    return render(request,'vote/detail.html',{'questions':question})

def toupiao(request,id):
    # return HttpResponse("投票详情")
    tid = request.POST['choice']
    result = Choice.objects.get(pk=tid)
    result.votes += 1
    result.save()
    # question = Questions.objects.get(pk=id)
    # return render(request, 'vote/detail.html', {'questions': question})
    return HttpResponseRedirect('/vote/detail/'+id+'/')