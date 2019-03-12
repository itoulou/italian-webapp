from django import forms
from django.core.exceptions import ValidationError
from add_verb.models import Verb_ARE, Verb_ARELineItem, Verb_ERE, Verb_ERELineItem, Verb_IRE, Verb_IRELineItem


class Verb_ARE_Form(forms.ModelForm):
    class Meta:
        model = Verb_ARE
        fields = ("infinitive", "meaning", "auxiliary_verb", "reflexive", "irregular")
        
    # def return_infinitive(self):
    #     infinitive = self.cleaned_data.get('infinitive')
    #     return infinitive

class Verb_ARE_LineForm(forms.ModelForm):
    class Meta:
        model = Verb_ARELineItem
        fields = ("tense", "first_person_singular",
                  "second_person_singular", "third_person_singular",
                  "first_person_plural", "second_person_plural",
                  "third_person_plural")
                  
    # def clean_infinitive_and_tense(self):
    #     tense = self.cleaned_data.get('tense')
    #     infinitive = Verb_ARE_Form.return_infinitive(self)
    #     if Verb_ARE.objects.filter(infinitive=infinitive) and Verb_ARELineItem.objects.filter(tense=tense):
    #         raise forms.ValidationError(u'This verb and tense has already been submitted')
    #     else:
    #         raise forms.ValidationError('This code is being executed')
    #     return infinitive    

class Verb_ERE_Form(forms.ModelForm):
    class Meta:
        model = Verb_ERE
        fields = ("infinitive", "meaning", "auxiliary_verb", "reflexive", "irregular")

class Verb_ERE_LineForm(forms.ModelForm):
    class Meta:
        model = Verb_ERELineItem
        fields = ("tense", "first_person_singular",
                  "second_person_singular", "third_person_singular",
                  "first_person_plural", "second_person_plural",
                  "third_person_plural")        
        


class Verb_IRE_Form(forms.ModelForm):
    class Meta:
        model = Verb_IRE
        fields = ("infinitive", "meaning", "auxiliary_verb", "reflexive", "irregular")


class Verb_IRE_LineForm(forms.ModelForm):
    class Meta:
        model = Verb_IRELineItem
        fields = ("tense", "first_person_singular",
                  "second_person_singular", "third_person_singular",
                  "first_person_plural", "second_person_plural",
                  "third_person_plural")        