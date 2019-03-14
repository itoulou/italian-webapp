from django.test import TestCase
from add_verb.forms import Verb_ARE_Form, Verb_ERE_Form, Verb_IRE_Form
from add_verb.models import Verb_ARE, Verb_ERE, Verb_IRE

# Create your tests here.
class TestViews(TestCase):
    
    def test_get_home_page(self):
        page = self.client.get("/home/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "home.html")

class TestForms(TestCase):    
    def test_verb_are_form(self):
        
        form = Verb_ARE_Form({
                                    'infinitive': 'mangiare',
                                    'meaning': 'eat',
                                    'auxiliary_verb': 'avere'
                                })
        self.assertTrue(form.is_valid())
        
    def test_verb_ere_form(self):
        
        form = Verb_ERE_Form({
                                    'infinitive': 'leggere',
                                    'meaning': 'read',
                                    'auxiliary_verb': 'avere'
                                })
        self.assertTrue(form.is_valid())
        
    def test_verb_ire_form(self):
        
        form = Verb_IRE_Form({
                                    'infinitive': 'dormire',
                                    'meaning': 'sleep',
                                    'auxiliary_verb': 'avere'
                                })
        self.assertTrue(form.is_valid())

class TestModels(TestCase):
    def test_verb_ends_in_are_or_arsi(self):
        verb = Verb_ARE(infinitive="andare")
        reflexive_verb = Verb_ARE(infinitive="svegliarsi")
        verb.save()
        reflexive_verb.save()
        self.assertTrue(verb.infinitive.endswith("are"))
        self.assertTrue(reflexive_verb.infinitive.endswith("arsi"))
        
    def test_verb_ends_in_ere_or_ersi(self):
        verb = Verb_ARE(infinitive="correre")
        reflexive_verb = Verb_ARE(infinitive="accorgersi")
        verb.save()
        reflexive_verb.save()
        self.assertTrue(verb.infinitive.endswith("ere"))
        self.assertTrue(reflexive_verb.infinitive.endswith("ersi"))
    
    def test_verb_ends_in_ire_or_irsi(self):
        verb = Verb_ARE(infinitive="finire")
        reflexive_verb = Verb_ARE(infinitive="divertirsi")
        verb.save()
        reflexive_verb.save()
        self.assertTrue(verb.infinitive.endswith("ire"))
        self.assertTrue(reflexive_verb.infinitive.endswith("irsi"))    
        
        