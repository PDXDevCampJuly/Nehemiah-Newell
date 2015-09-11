from django.shortcuts import render
from django.http import HttpResponse

def forum(request):
    return render(request,"fakeForum.html")