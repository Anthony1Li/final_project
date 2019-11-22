from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
   return render(request, 'myapp/hello.html', {})

def morning(request):
   return render(request, 'myapp/morning.html', {})

def viewArticle(request, articleId):
   text = f"Displaying article Number : {articleId}"
   return HttpResponse(text)