from django.shortcuts import render, redirect
from django.contrib import messages
from add_verb.models import Verb_ARE, Verb_ERE, Verb_IRE
from add_verb.forms import Verb_ARE_Form, Verb_ARE_LineForm, Verb_ERE_Form, Verb_ERE_LineForm, Verb_IRE_Form, Verb_IRE_LineForm

# Create your views here.
def do_search(request):
    """
    Search for a specific verb
    """
    if request.method == "GET":
        verb_infinitive_form_are = Verb_ARE_Form()
        verb_conjugations_form_are = Verb_ARE_LineForm()
        verb_infinitive_form_ere = Verb_ERE_Form()
        verb_conjugations_form_ere = Verb_ERE_LineForm()
        verb_infinitive_form_ire = Verb_IRE_Form()
        verb_conjugations_form_ire = Verb_IRE_LineForm()
        
        verb_searched = request.GET.get('search-verb', False)

        if verb_searched.endswith("are") or verb_searched.endswith("arsi"):
            all_verbs = Verb_ARE.objects.filter(infinitive__icontains=verb_searched)
        
        elif verb_searched.endswith("ere") or verb_searched.endswith("ersi"):
            all_verbs = Verb_ERE.objects.filter(infinitive__icontains=verb_searched)
        
        elif verb_searched.endswith("ire") or verb_searched.endswith("irsi"):
            all_verbs = Verb_IRE.objects.filter(infinitive__icontains=verb_searched)
        
        else:
            messages.error(request, "Please enter the infinitive of the verb you're looking for")
            return redirect('home')
        print(all_verbs)
        return render(request, 'home.html', {"all_verbs": all_verbs,
                                             "verb_infinitive_form_are": verb_infinitive_form_are,
                                             "verb_conjugations_form_are": verb_conjugations_form_are,
                                             "verb_infinitive_form_ere": verb_infinitive_form_ere,
                                             "verb_conjugations_form_ere": verb_conjugations_form_ere,
                                             "verb_infinitive_form_ire": verb_infinitive_form_ire,
                                             "verb_conjugations_form_ire": verb_conjugations_form_ire,
                                            })    
        
    else:
        messages.error(request, "An error occured please try again later")

    return redirect('home')
    