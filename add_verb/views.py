from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from add_verb.forms import Verb_ARE_Form, Verb_ARE_LineForm, Verb_ERE_Form, Verb_ERE_LineForm, Verb_IRE_Form, Verb_IRE_LineForm
from add_verb.models import Verb_ARE, Verb_ARELineItem, Verb_ERE, Verb_ERELineItem, Verb_IRE, Verb_IRELineItem

# Create your views here.
def add_verb_are(request):
    """
    add verb to the database
    """
    if request.method == "POST":
        
        verb_infinitive_form = Verb_ARE_Form(request.POST)
        verb_conjugations_form = Verb_ARE_LineForm(request.POST)
        
        if verb_infinitive_form.is_valid() and verb_conjugations_form.is_valid():
            infinitive_from_form = verb_infinitive_form.cleaned_data['infinitive']
            ending = "are"
            reflexive_ending = "arsi"
            if infinitive_from_form.endswith(ending) == False and infinitive_from_form.endswith(reflexive_ending) == False:
                messages.error(request, "this verb doesn't end in 'are'")
                return redirect("home")
            verbs = Verb_ARE.objects.filter(infinitive=infinitive_from_form)
              
            if verbs:
                for verb in verbs:
                    if verb.are_line_items.filter(tense=verb_conjugations_form.cleaned_data['tense']):
                        messages.error(request, "this verb and tense has already been added")
                        return redirect("home")
                    else:
                        verb_conjugations = verb_conjugations_form.save(commit=False)
                        verb_conjugations.verb = verb
                        verb_conjugations.save()
                        messages.error(request, "verb " + str(verb) + " added")
                        return redirect("home")
                        
            verb = verb_infinitive_form.save()
            print(verb)
            verb_conjugations = verb_conjugations_form.save(commit=False)
            verb_conjugations.verb = verb
            verb_conjugations.save()
            messages.error(request, "verb "+ str(verb) + " added")
            return redirect("home")
            
        else:
            messages.error(request, "a problem occured, try again")
            return redirect("home")
    
    else:
        verb_infinitive_form_are = Verb_ARE_Form()
        verb_conjugations_form_are = Verb_ARE_LineForm()
    return render(request, "home.html", {"verb_infinitive_form_are": verb_infinitive_form_are,
                                         "verb_conjugations_form_are": verb_conjugations_form_are,
                                        })
                                         
def add_verb_ere(request):
    """
    add verb to the database
    """
    if request.method == "POST":
        
        verb_infinitive_form = Verb_ERE_Form(request.POST)
        verb_conjugations_form = Verb_ERE_LineForm(request.POST)
        
        if verb_infinitive_form.is_valid() and verb_conjugations_form.is_valid():
            infinitive_from_form = verb_infinitive_form.cleaned_data['infinitive']
            ending = "ere"
            reflexive_ending = "ersi"
            if infinitive_from_form.endswith(ending) == False and infinitive_from_form.endswith(reflexive_ending) == False:
                messages.error(request, "this verb doesn't end in 'ere'")
                return redirect("home")
            verbs = Verb_ERE.objects.filter(infinitive=infinitive_from_form)
            if verbs:
                for verb in verbs:
                    # %(app_label)s_%(class)s
                    if verb.ere_line_items.filter(tense=verb_conjugations_form.cleaned_data['tense']):
                        messages.error(request, "this verb and tense has already been added")
                        return redirect("home")
                    else:
                        verb_conjugations = verb_conjugations_form.save(commit=False)
                        verb_conjugations.verb = verb
                        verb_conjugations.save()
                        messages.error(request, "verb " + str(verb) + " added")
                        return redirect("home")
                        
            verb = verb_infinitive_form.save()
            print(verb)
            verb_conjugations = verb_conjugations_form.save(commit=False)
            verb_conjugations.verb = verb
            verb_conjugations.save()
            messages.error(request, "verb "+ str(verb) + " added")
            return redirect("home")
            
        else:
            messages.error(request, "a problem occured, try again")
            return redirect("home")
    
    else:
        verb_infinitive_form_ere = Verb_ERE_Form()
        verb_conjugations_form_ere = Verb_ERE_LineForm()
    return render(request, "home.html", {"verb_infinitive_form_ere": verb_infinitive_form_ere,
                                         "verb_conjugations_form_ere": verb_conjugations_form_ere,
                                         })

def add_verb_ire(request):
    """
    add verb to the database
    """
    if request.method == "POST":
        
        verb_infinitive_form = Verb_IRE_Form(request.POST)
        verb_conjugations_form = Verb_IRE_LineForm(request.POST)
        
        if verb_infinitive_form.is_valid() and verb_conjugations_form.is_valid():
            infinitive_from_form = verb_infinitive_form.cleaned_data['infinitive']
            ending = "ire"
            reflexive_ending = "irsi"
            if infinitive_from_form.endswith(ending) == False and infinitive_from_form.endswith(reflexive_ending) == False:
                messages.error(request, "this verb doesn't end in 'ire'")
                return redirect("home")
            verbs = Verb_IRE.objects.filter(infinitive=infinitive_from_form)
            if verbs:
                for verb in verbs:
                    # %(app_label)s_%(class)s
                    if verb.ire_line_items.filter(tense=verb_conjugations_form.cleaned_data['tense']):
                        messages.error(request, "this verb and tense has already been added")
                        return redirect("home")
                    else:
                        verb_conjugations = verb_conjugations_form.save(commit=False)
                        verb_conjugations.verb = verb
                        verb_conjugations.save()
                        messages.error(request, "verb " + str(verb) + " added")
                        return redirect("home")
                        
            verb = verb_infinitive_form.save()
            print(verb)
            verb_conjugations = verb_conjugations_form.save(commit=False)
            verb_conjugations.verb = verb
            verb_conjugations.save()
            messages.error(request, "verb "+ str(verb) + " added")
            return redirect("home")
            
        else:
            messages.error(request, "a problem occured, try again")
            return redirect("home")
    
    else:
        verb_infinitive_form_ire = Verb_IRE_Form()
        verb_conjugations_form_ire = Verb_IRE_LineForm()
    return render(request, "home.html", {"verb_infinitive_form_ire": verb_infinitive_form_ire,
                                         "verb_conjugations_form_ire": verb_conjugations_form_ire})
                                         
                                         