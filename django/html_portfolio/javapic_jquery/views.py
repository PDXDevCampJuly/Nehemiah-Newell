from django.shortcuts import render

# Create your views here.
def index_jquery(request):
    return render(request,"index_jquery.html")

def join_jquery(request):
    return render(request,"join_jquery.html")

def gallery_jquery(request):
    return render(request,"gallery_jquery.html")
