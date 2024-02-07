from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def demo(request):
#     return HttpResponse("hello world")


def demo(request):
    return render(request,"index.html")

def about(request):
    return HttpResponse(" iam about page")

def contact(request):
    return HttpResponse(" iam contact page")


def gallery(request):
    return render(request,"gallery.html")