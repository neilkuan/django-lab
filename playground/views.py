from django.shortcuts import render
from django.http import HttpResponse, QueryDict
# Create your views here.


def say_hello(request):
    # return string direct 
    # return  HttpResponse("Hello  world!!!")

    # return html template via render
    name = request.GET.get('name', '')
    if name != '':
       return render(request, 'hello.html', {'name': name})
    else:
       return render(request, 'hello.html')
