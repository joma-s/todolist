from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

# Create your views here.

def index(request):
    if "tasks" not in request.session: # if there's no tasks list in the session, create a blank one
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {  # return the index file with the session's tasks list
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":        # if something has been sent in post
            form = NewTaskForm(request.POST)    # save user data to the form variable
            if form.is_valid():                 # if data is valid
                task = form.cleaned_data["task"]    # save cleaned data in the task variable
                request.session["tasks"] += [task] # append task to the session's tasks list
                return HttpResponseRedirect(reverse("tasks:index"))     # and redirect to the index page
            else:
                return render(request, "tasks/add.html", {      # otherwise, return the add page with the form filled out with user data so the user can see any errors from the server
                    "form" : form
                })

    return render(request,"tasks/add.html", {    # if no post request has been sent, display empty form
        "form" : NewTaskForm()
    })