from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo(request):
    name="india"
    return render(request,"index.html",{'obj':name})

def addition(request):
    return render(request,"result.html")
