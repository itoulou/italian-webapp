from django.db import models

# Create your models here.
class Verb_ARE(models.Model):
    
    """
    Model for verbs ending in '-are'
    """
    AUX_VERBS = (
            ("avere", "avere"),
            ("essere", "essere")
        )
    infinitive = models.CharField(max_length=30, blank=False, null=True)
    meaning = models.CharField(max_length=30, blank=False, null=True)
    reflexive = models.BooleanField(default=False)
    irregular = models.BooleanField(default=False)
    auxiliary_verb = models.CharField(max_length=30, choices=AUX_VERBS, blank=False, null=True)
    
    def __str__(self):
        return self.infinitive
        
class Verb_ARELineItem(models.Model):
    
    verb = models.ForeignKey(Verb_ARE, null=True, blank=False, related_name="are_line_items")
    TENSES = (
        ("Presente", "Presente"),
        ("Passato Prossimo", "Passato Prossimo"),
        ("Imperfetto", "Imperfetto"),
        ("Trapassato Prossimo", "Trapassato Prossimo"),
        ("Futuro Semplice", "Futuro Semplice"),
        ("Futuro Anteriore", "Futuro Anteriore"),
        ("Congiuntivo Presente", "Congiuntivo Presente"),
        ("Congiuntivo Passato", "Congiuntivo Passato"),
        ("Congiuntivo Imperfetto", "Congiuntivo Imperfetto"),
        ("Congiuntivo Trapassato", "Congiuntivo Trapassato"),
        ("Condizionale Presente", "Condizionale Presente"),
        ("Condizionale Passato", "Condizionale Passato"),
    )
    
    tense = models.CharField(max_length=50, choices=TENSES, blank=False, null=True)
    first_person_singular = models.CharField(max_length=30, blank=False, null=True)
    second_person_singular = models.CharField(max_length=30, blank=False, null=True)
    third_person_singular = models.CharField(max_length=30, blank=False, null=True)
    first_person_plural = models.CharField(max_length=30, blank=False, null=True)
    second_person_plural = models.CharField(max_length=30, blank=False, null=True)
    third_person_plural = models.CharField(max_length=30, blank=False, null=True)
    
    def __unicode__(self):
        return "{0}".format(self.tense.title)
        

class Verb_ERE(models.Model):
    
    """
    Model for verbs ending in '-ere'
    """
    AUX_VERBS = (
            ("avere", "avere"),
            ("essere", "essere")
        )
    infinitive = models.CharField(max_length=30, blank=False, null=True)
    meaning = models.CharField(max_length=30, blank=False, null=True)
    reflexive = models.BooleanField(default=False)
    irregular = models.BooleanField(default=False)
    auxiliary_verb = models.CharField(max_length=30, choices=AUX_VERBS, blank=False, null=True)
    
    def __str__(self):
        return self.infinitive
        
class Verb_ERELineItem(models.Model):
    
    verb = models.ForeignKey(Verb_ERE, null=True, blank=False, related_name="ere_line_items")
    TENSES = (
        ("Presente", "Presente"),
        ("Passato Prossimo", "Passato Prossimo"),
        ("Imperfetto", "Imperfetto"),
        ("Trapassato Prossimo", "Trapassato Prossimo"),
        ("Futuro Semplice", "Futuro Semplice"),
        ("Futuro Anteriore", "Futuro Anteriore"),
        ("Congiuntivo Presente", "Congiuntivo Presente"),
        ("Congiuntivo Passato", "Congiuntivo Passato"),
        ("Congiuntivo Imperfetto", "Congiuntivo Imperfetto"),
        ("Congiuntivo Trapassato", "Congiuntivo Trapassato"),
        ("Condizionale Presente", "Condizionale Presente"),
        ("Condizionale Passato", "Condizionale Passato"),
    )
    
    tense = models.CharField(max_length=50, choices=TENSES, blank=False, null=True)
    first_person_singular = models.CharField(max_length=30, blank=False, null=True)
    second_person_singular = models.CharField(max_length=30, blank=False, null=True)
    third_person_singular = models.CharField(max_length=30, blank=False, null=True)
    first_person_plural = models.CharField(max_length=30, blank=False, null=True)
    second_person_plural = models.CharField(max_length=30, blank=False, null=True)
    third_person_plural = models.CharField(max_length=30, blank=False, null=True)
    
    def __unicode__(self):
        return "{0}".format(self.tense.title)
        
class Verb_IRE(models.Model):
    
    """
    Model for verbs ending in '-ire'
    """
    AUX_VERBS = (
            ("avere", "avere"),
            ("essere", "essere")
        )
    infinitive = models.CharField(max_length=30, blank=False, null=True)
    meaning = models.CharField(max_length=30, blank=False, null=True)
    reflexive = models.BooleanField(default=False)
    irregular = models.BooleanField(default=False)
    auxiliary_verb = models.CharField(max_length=30, choices=AUX_VERBS, blank=False, null=True)
    
    def __str__(self):
        return self.infinitive
        
class Verb_IRELineItem(models.Model):
    
    verb = models.ForeignKey(Verb_IRE, null=True, blank=False, related_name="ire_line_items")
    TENSES = (
        ("Presente", "Presente"),
        ("Passato Prossimo", "Passato Prossimo"),
        ("Imperfetto", "Imperfetto"),
        ("Trapassato Prossimo", "Trapassato Prossimo"),
        ("Futuro Semplice", "Futuro Semplice"),
        ("Futuro Anteriore", "Futuro Anteriore"),
        ("Congiuntivo Presente", "Congiuntivo Presente"),
        ("Congiuntivo Passato", "Congiuntivo Passato"),
        ("Congiuntivo Imperfetto", "Congiuntivo Imperfetto"),
        ("Congiuntivo Trapassato", "Congiuntivo Trapassato"),
        ("Condizionale Presente", "Condizionale Presente"),
        ("Condizionale Passato", "Condizionale Passato"),
    )
    
    tense = models.CharField(max_length=50, choices=TENSES, blank=False, null=True)
    first_person_singular = models.CharField(max_length=30, blank=False, null=True)
    second_person_singular = models.CharField(max_length=30, blank=False, null=True)
    third_person_singular = models.CharField(max_length=30, blank=False, null=True)
    first_person_plural = models.CharField(max_length=30, blank=False, null=True)
    second_person_plural = models.CharField(max_length=30, blank=False, null=True)
    third_person_plural = models.CharField(max_length=30, blank=False, null=True)
    
    def __unicode__(self):
        return "{0}".format(self.tense.title)        

    

