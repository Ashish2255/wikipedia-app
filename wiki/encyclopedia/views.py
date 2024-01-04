from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from . import util
import os

from django.http import HttpResponse
from django.conf import settings
import markdown

def display(request,entry):
    return render(request,"encyclopedia/edit.html",{
        "content":entry
    })

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request,name):
    
    return render(request, "encyclopedia/title.html",{
        "entry":util.get_entry(name)
    })

def search(request):
    if request.method == "POST":
        # Get the value of the 'q' parameter from the form data
        query = request.POST.get("q")

        # Use the 'query' parameter as needed (e.g., pass it to another function)
        return title(request, query)

    # If the request method is not POST, you might want to handle it accordingly
    return index(request)

def new(request):
    return render(request, "encyclopedia/new.html")

def edit(request):
    return render(request,"encyclopedia/edit.html")

def create_file(request):
    if request.method == "POST":
        # Get the values from the form data
        tit = request.POST.get("tit")
        content = request.POST.get("myText")

        util.save_entry(tit,content)
        return title(request,tit)

    return render(request, "new.html")

