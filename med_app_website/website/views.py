from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return render(request, 'website/index.html')

def page2(request):
  return render(request, 'website/howitworks.html')
