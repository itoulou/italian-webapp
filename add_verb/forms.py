from django import forms
from django.core.exceptions import ValidationError
from add_verb.models import Verb_ARE, Verb_ARELineItem, Verb_ERE, Verb_ERELineItem, Verb_IRE, Verb_IRELineItem


class Verb_ARE_Form(forms.ModelForm):
    class Meta:
        model = Verb_ARE
        fields = ("infinitive", "meaning", "auxiliary_verb", "reflexive", "irregular")
        

class Verb_ARE_LineForm(forms.ModelForm):
    class Meta:
        model = Verb_ARELineItem
        fields = ("tense", "first_person_singular",
                  "second_person_singular", "third_person_singular",
                  "first_person_plural", "second_person_plural",
                  "third_person_plural")

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