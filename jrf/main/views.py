from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "title": "Main"
    }
    return render(request, 'main/pages/main.html', context)
    # return HttpResponse("Main")