from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fee_home(request):
    return HttpResponse('<h2>From Fee App Home</h2>')
def submit_fee(request):
    return HttpResponse('Fee submitted')
