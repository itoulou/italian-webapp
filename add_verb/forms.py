from django import forms
from add_verb.models import Verb_are

class Verb_ARE_Form(forms.ModelForm):
    class Meta:
        model = Verb_are
        fields = ("infinitive", "tense", "first_person_singular",
                  "second_person_singular", "third_person_singular",
                  "first_person_plural", "second_person_plural",
                  "third_person_plural")
    