from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    print(request.GET)
 
    return render(request, "encyclopedia/entry.html", {
        #  "name": name.capitalize(),
         "entry": util.get_entry(title),
         "title": title 
         
    })

from django import forms

class NewTaskForm(forms.Form):
    search = forms.CharField(label="New Search")



def search(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": NewTaskForm()
    })