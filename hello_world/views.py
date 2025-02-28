from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse == "POST":
        return HttpResponse("you must have POSTed something")
        else:
            return HttpResponse(request.method)
