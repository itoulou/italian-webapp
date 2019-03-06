from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from add_verb.forms import Verb_ARE_Form
from add_verb.models import Verb_are

# Create your views here.
def add_verb_are(request):
    """
    add verb to the database
    """
    if request.method == "POST":
        
        verb_form = Verb_ARE_Form(request.POST)
        
        if verb_form.is_valid():
            verb_form.save()
            verb = request.GET.get("infinitive")
            messages.error(request, "verb " + str(verb) + " added")
            return redirect("home")
    
    else:
        verb_form = Verb_ARE_Form()
    return render(request, "home.html", {"verb_form": verb_form})    