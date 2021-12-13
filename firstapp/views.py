from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'firstapp/home.html')


def login(request):
    return render(request,'firstapp/login.html')


def signup(request):
    return render(request,'firstapp/signup.html')


def predict(request):
    return render(request,'firstapp/predict.html')


def result(request):
    return render(request,'firstapp/result.html')

