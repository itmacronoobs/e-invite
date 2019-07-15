from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request): 

    context = {

    'title': 'MvitesApp: HomePage',
    }
    return render(request,'mvitesapp/index.html',context)

def excel(request): 

    context = {

    'title': 'MvitesApp: Excel',
    }
    return render(request,'mvitesapp/excel.html',context)
