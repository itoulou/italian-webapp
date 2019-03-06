from django.shortcuts import render
from django.contrib import auth, messages
from add_verb.forms import Verb_ARE_Form

# Create your views here.
def home(request):
    print(request.user)
    verb_form = Verb_ARE_Form()
    return render(request, 'home.html', {"verb_form": verb_form})
    