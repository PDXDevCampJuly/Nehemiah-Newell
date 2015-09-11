from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    content = {'someadjective': 'hype!', 'randomname':'ichi'}
    return render(request, 'index.html', content)


def liars_damn_liars_and_corgis(request):
    return HttpResponse("Corgis are Awesome! <a href='/hello'>Homepage! Please! Woof!</a>")

def forum(request):
    return render(request,"fakeForum.html")