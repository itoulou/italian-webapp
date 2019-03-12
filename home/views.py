from django.shortcuts import render
from django.contrib import auth, messages
from add_verb.forms import Verb_ARE_Form, Verb_ARE_LineForm, Verb_ERE_Form, Verb_ERE_LineForm, Verb_IRE_Form, Verb_IRE_LineForm

# Create your views here.
def home(request):
    verb_infinitive_form_are = Verb_ARE_Form()
    verb_conjugations_form_are = Verb_ARE_LineForm()
    verb_infinitive_form_ere = Verb_ERE_Form()
    verb_conjugations_form_ere = Verb_ERE_LineForm()
    verb_infinitive_form_ire = Verb_IRE_Form()
    verb_conjugations_form_ire = Verb_IRE_LineForm()
    
    return render(request, "home.html", {"verb_infinitive_form_are": verb_infinitive_form_are,
                                         "verb_conjugations_form_are": verb_conjugations_form_are,
                                         "verb_infinitive_form_ere": verb_infinitive_form_ere,
                                         "verb_conjugations_form_ere": verb_conjugations_form_ere,
                                         "verb_infinitive_form_ire": verb_infinitive_form_ire,
                                         "verb_conjugations_form_ire": verb_conjugations_form_ire,
                                        })    
    