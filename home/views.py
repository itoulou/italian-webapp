from django.shortcuts import render
from django.contrib import auth, messages

# Create your views here.
def home(request):
    return render(request, 'home.html')
    