from django.shortcuts import render
from django.http import HttpResponse


def learn_django(request):
        return HttpResponse('Hello django')

def learn_py(request):
        return HttpResponse('<h1>My Home</h1>')
def index(request):
        return HttpResponse('<h1>Home Page</h1>') 