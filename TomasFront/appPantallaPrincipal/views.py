from django.shortcuts import render

# Create your views here.
def initialView(request):
    return render(request, 'initialView.html')

def homeView(request):
    return render(request, 'homeView.html')

def talkingView(request):
    return render(request, 'talkingView.html')

def visionView(request):
    return render(request, 'visionView.html')

def gameSelectView(request):
    return render(request, 'gameSelectView.html')

def gameView(request):
    return render(request, 'gameView.html')

