from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited


def index(request):
    response = "Hello, I am your  request!"
    return HttpResponse(response)
def test(request):
    response = "Hello. I am test"
    return HttpResponse(response)

