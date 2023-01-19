from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def res(request):
    html = '<h1>Hello World!</h1><br><h2>Good morning</h2><br><h3>Good afternoon</h3><br><h4>Good evening</h4>'
    return HttpResponse(html)