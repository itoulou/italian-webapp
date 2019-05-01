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
    if infinitive.endswith("are") or infinitive.endswith("arsi"):
        verb_conjugations = Verb_ARE.objects.filter(infinitive=infinitive)
        for verb in verb_conjugations:
            for item in verb.are_line_items.filter(tense="Presente"):
                conjugations = item
                
        conjugations_presente = return_conjugations(request, infinitive, "are", "Presente")
        conjugations_passato_prossimo = return_conjugations(request, infinitive, "are", "Passato Prossimo")
        conjugations_imperfetto = return_conjugations(request, infinitive, "are", "Imperfetto")
        conjugations_trapassato_prossimo = return_conjugations(request, infinitive, "are", "Trapassato Prossimo")
        conjugations_futuro_semplice = return_conjugations(request, infinitive, "are", "Futuro Semplice")
        conjugations_futuro_anteriore = return_conjugations(request, infinitive, "are", "Futuro Anteriore")
        conjugations_congiuntivo_presente = return_conjugations(request, infinitive, "are", "Congiuntivo Presente")
        conjugations_congiuntivo_passato = return_conjugations(request, infinitive, "are", "Congiuntivo Passato")
        conjugations_congiuntivo_imperfetto = return_conjugations(request, infinitive, "are", "Congiuntivo Imperfetto")
        conjugations_congiuntivo_trapassato = return_conjugations(request, infinitive, "are", "Congiuntivo Trapassato")
        conjugations_condizionale_presente = return_conjugations(request, infinitive, "are", "Condizionale Presente")
        conjugations_condizionale_passato = return_conjugations(request, infinitive, "are", "Condizionale Passato")
                
    elif infinitive.endswith("ere") or infinitive.endswith("ersi"):
        verb_conjugations = Verb_ERE.objects.filter(infinitive=infinitive)
        for verb in verb_conjugations:
            for item in verb.ere_line_items.filter(tense="Presente"):
                conjugations = item
        
        conjugations_presente = return_conjugations(request, infinitive, "ere", "Presente")
        conjugations_passato_prossimo = return_conjugations(request, infinitive, "ere", "Passato Prossimo")
        conjugations_imperfetto = return_conjugations(request, infinitive, "ere", "Imperfetto")
        conjugations_trapassato_prossimo = return_conjugations(request, infinitive, "ere", "Trapassato Prossimo")
        conjugations_futuro_semplice = return_conjugations(request, infinitive, "ere", "Futuro Semplice")
        conjugations_futuro_anteriore = return_conjugations(request, infinitive, "ere", "Futuro Anteriore")
        conjugations_congiuntivo_presente = return_conjugations(request, infinitive, "ere", "Congiuntivo Presente")
        conjugations_congiuntivo_passato = return_conjugations(request, infinitive, "ere", "Congiuntivo Passato")
        conjugations_congiuntivo_imperfetto = return_conjugations(request, infinitive, "ere", "Congiuntivo Imperfetto")
        conjugations_congiuntivo_trapassato = return_conjugations(request, infinitive, "ere", "Congiuntivo Trapassato")
        conjugations_condizionale_presente = return_conjugations(request, infinitive, "ere", "Condizionale Presente")
        conjugations_condizionale_passato = return_conjugations(request, infinitive, "ere", "Condizionale Passato")
            
                
    elif infinitive.endswith("ire") or infinitive.endswith("irsi"):
        verb_conjugations =  Verb_IRE.objects.filter(infinitive=infinitive)
        for verb in verb_conjugations:
            for item in verb.ire_line_items.filter(tense="Presente"):
                conjugations = item
        
        conjugations_presente = return_conjugations(request, infinitive, "ire", "Presente")
        conjugations_passato_prossimo = return_conjugations(request, infinitive, "ire", "Passato Prossimo")
        conjugations_imperfetto = return_conjugations(request, infinitive, "ire", "Imperfetto")
        conjugations_trapassato_prossimo = return_conjugations(request, infinitive, "ire", "Trapassato Prossimo")
        conjugations_futuro_semplice = return_conjugations(request, infinitive, "ire", "Futuro Semplice")
        conjugations_futuro_anteriore = return_conjugations(request, infinitive, "ire", "Futuro Anteriore")
        conjugations_congiuntivo_presente = return_conjugations(request, infinitive, "ire", "Congiuntivo Presente")
        conjugations_congiuntivo_passato = return_conjugations(request, infinitive, "ire", "Congiuntivo Passato")
        conjugations_congiuntivo_imperfetto = return_conjugations(request, infinitive, "ire", "Congiuntivo Imperfetto")
        conjugations_congiuntivo_trapassato = return_conjugations(request, infinitive, "ire", "Congiuntivo Trapassato")
        conjugations_condizionale_presente = return_conjugations(request, infinitive, "ire", "Condizionale Presente")
        conjugations_condizionale_passato = return_conjugations(request, infinitive, "ire", "Condizionale Passato")
                
    else:
        messages.error(request, "An error occured, Please try again later")
        return redirect('home')
        
    variables = {"verb": verb,
                 "conjugations": conjugations,
                #  "conjugations_lg": conjugations_lg,
                "conjugations_presente": conjugations_presente,
                "conjugations_passato_prossimo": conjugations_passato_prossimo,
                "conjugations_imperfetto": conjugations_imperfetto,
                "conjugations_trapassato_prossimo": conjugations_trapassato_prossimo,
                "conjugations_futuro_semplice": conjugations_futuro_semplice,
                "conjugations_futuro_anteriore": conjugations_futuro_anteriore,
                "conjugations_congiuntivo_presente": conjugations_congiuntivo_presente,
                "conjugations_congiuntivo_passato": conjugations_congiuntivo_passato,
                "conjugations_congiuntivo_imperfetto": conjugations_congiuntivo_imperfetto,
                "conjugations_congiuntivo_trapassato": conjugations_congiuntivo_trapassato,
                "conjugations_condizionale_presente": conjugations_condizionale_presente,
                "conjugations_condizionale_passato": conjugations_condizionale_passato,
                 }
    return render(request, 'viewverb.html', variables)    
    # except:
    #     messages.error(request, "An error occured please try again")
    #     return redirect("home")

def return_conjugations(request, infinitive, ending, tense):
    """
    returns all the conjugations if present for that verb else return None
    """
    if ending == "are" or ending == "arsi":

        verb_conjugations = Verb_ARE.objects.filter(infinitive=infinitive)
        if verb_conjugations: 
            for verb in verb_conjugations:
                if verb.are_line_items.filter(tense=tense):
                    for item in verb.are_line_items.filter(tense=tense):
                        conjugations = item
                else:
                    conjugations = None
                 
    elif ending == "ere" or ending == "ersi":
        
         verb_conjugations = Verb_ERE.objects.filter(infinitive=infinitive)
         if verb_conjugations: 
            for verb in verb_conjugations:
                if verb.ere_line_items.filter(tense=tense):
                    for item in verb.ere_line_items.filter(tense=tense):
                        conjugations = item
                else:
                    conjugations = None
             
    elif ending == "ire" or ending == "irsi":
        
         verb_conjugations = Verb_IRE.objects.filter(infinitive=infinitive)
         if verb_conjugations: 
            for verb in verb_conjugations:
                if verb.ire_line_items.filter(tense=tense):
                    for item in verb.ire_line_items.filter(tense=tense):
                        conjugations = item
                else:
                    conjugations = None
        
               
    return conjugations            
                

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
    
    
    
        
       