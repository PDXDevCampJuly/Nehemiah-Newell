from django.shortcuts import render

def about(request):
    return render(request,"about.html")

def table_of_contents(request):
    return render(request, "table.html")