 # -*- coding: utf-8 -*-

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'surveys/index.html')

def create(request):
    # Check if user has a session
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1

    request.session['data'] = {
        "Name": request.POST['name'],
        "Dojo Location": request.POST['dojo_location'],
        "Favorite Language": request.POST['favorite_lang'],
        "Comments": request.POST['comments']
    }
    return redirect('/results')

def results(request):
    print "Go to show results!"
    print request.session
    return render(request, 'surveys/results.html') 