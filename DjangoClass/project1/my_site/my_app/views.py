from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
articles={
    'sports': 'sports page',
    'news' : 'news page',
    'polictal' : 'polictal page',

}

def sports(request,topic):
    return HttpResponse(articles[topic])



def index(request):
    return HttpResponse('Hello world!!!')


def simple_view(request):

    return render(request,'my_app/example.html')