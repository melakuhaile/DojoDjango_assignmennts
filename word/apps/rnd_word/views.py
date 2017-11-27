# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
import string
from django.shortcuts import render, redirect

def rnd_word(n):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))

def index(request):
    try:
        request.session['check']
    except KeyError:
        request.session['check'] = 0

    return render(request, "rnd_word/index.html")

def generate(request):
    request.session['check'] += 1  
    request.session['word'] = rnd_word(14)
    return redirect('/')

def reset(request):
    del request.session['check']
    del request.session['word']
    return redirect('/')