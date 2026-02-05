from django.http import HttpResponse
from django.shortcuts import render

def test(request):
    return HttpResponse("hello jaymin rana ")


def aboutus(request):
    return render(request,"aboutus.html ")

def contectus(request):
    return render(request,"contectus.html ")
def home(request):
    return render(request,"home.html ")
def reacp(request):
    return render(request,"reacp.html ")
def recipe(request):
    ingredent =["suger","tea powder","milk","water"]
    data ={"name":"tea","time":"10","ingredent":ingredent}
    return render(request,"recipe.html ",data)




