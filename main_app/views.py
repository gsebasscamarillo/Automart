from django.shortcuts import render
#from django.http import HttpResponse #primer paso
# Create your views here.

def index(request):
    return render(request, 'index.html')
    #return HttpResponse("<h1>Bienvenido a AutoMart</h1>") #primer paso