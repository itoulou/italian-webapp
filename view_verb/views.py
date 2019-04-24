from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from add_verb.models import Verb_ARE, Verb_ERE, Verb_IRE
from add_verb.admin import VerbAREAdmin, VerbEREAdmin, VerbIREAdmin


# Create your views here.
def view_verb(request, pk, infinitive):
    """
    view verb searched for
    """
    # try:
    if infinitive.endswith("are") or infinitive.endswith("arsi"):
        verb_conjugations = Verb_ARE.objects.filter(infinitive=infinitive)
        for verb in verb_conjugations:
            for item in verb.are_line_items.filter(tense="Presente"):
                conjugations = item
            # for item in verb.are_line_items.all():
            #     conjugations_lg = item
                
                
    elif infinitive.endswith("ere") or infinitive.endswith("ersi"):
        verb_conjugations = Verb_ERE.objects.filter(infinitive=infinitive)
        for verb in verb_conjugations:
            for item in verb.ere_line_items.filter(tense="Presente"):
                conjugations = item
            
                
    elif infinitive.endswith("ire") or infinitive.endswith("irsi"):
        verb_conjugations =  Verb_IRE.objects.filter(infinitive=infinitive)
        for verb in verb_conjugations:
            for item in verb.ire_line_items.filter(tense="Presente"):
                conjugations = item
    else:
        messages.error(request, "An error occured, Please try again later")
        return redirect('home')
        
    tenses = ["Presente", "Passato Prossimo", "Imperfetto", "Trapassato Prossimo",
              "Futuro Semplice", "Futuro Anteriore", "Congiuntivo Presente",
              "Congiuntivo Passato", "Congiuntivo Imperfetto", 
              "Congiuntivo Trapassato", "Condizionale Presente",
              "Condizionale Passato"]
    count = 0          
    return render(request, 'viewverb.html', {"verb": verb, "tenses": tenses,
                                                 "conjugations": conjugations,
                                                 "count": count,
                                                #  "conjugations_lg": conjugations_lg,
                                                 })    
    # except:
    #     messages.error(request, "An error occured please try again")
    #     return redirect("home")

@csrf_exempt
def choose_tense(request, pk, infinitive):
    """
    function to return all the conjugations of the verb
    based on the tense chosen
    """
    if request.method == "POST":
        tense_selected = request.POST.get("tense")
        
        try:
            if infinitive.endswith("are") or infinitive.endswith("arsi"):
                verb_conjugations = Verb_ARE.objects.filter(infinitive=infinitive)
                for verb in verb_conjugations:
                    for item in verb.are_line_items.filter(tense=tense_selected):
                        conjugations = item
            elif infinitive.endswith("ere") or infinitive.endswith("ersi"):
                verb_conjugations = Verb_ERE.objects.get(infinitive=infinitive)
                for verb in verb_conjugations:
                    for item in verb.ere_line_items.filter(tense=tense_selected):
                        conjugations = item
            elif infinitive.endswith("ire") or infinitive.endswith("irsi"):
                verb_conjugations = Verb_IRE.objects.filter(infinitive=infinitive)
                for verb in verb_conjugations:
                    for item in verb.ire_line_items.filter(tense=tense_selected):
                        conjugations = item
            else:
                messages.error(request, "An error occured, Please try again later")
                return redirect('home')
            
            data = {
                "tense": tense_selected,
                "first_person_singular": conjugations.first_person_singular,
                "second_person_singular": conjugations.second_person_singular,
                "third_person_singular": conjugations.third_person_singular,
                "first_person_plural": conjugations.first_person_plural,
                "second_person_plural": conjugations.second_person_plural,
                "third_person_plural": conjugations.third_person_plural,
            }    
            
        except:
            null = None
            data = {
                "tense": tense_selected,
                "first_person_singular": null,
                "second_person_singular": null,
                "third_person_singular": null,
                "first_person_plural": null,
                "second_person_plural": null,
                "third_person_plural": null,
            }    
            
    return JsonResponse(data) 
    
    
    
        
       