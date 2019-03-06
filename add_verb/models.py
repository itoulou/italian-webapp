from django.db import models

# Create your models here.
class Verb_are(models.Model):
    
    """
    Model for verbs ending in '-are'
    """
    
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
    
    infinitive = models.CharField(max_length=30)
    tense = models.CharField(max_length=50, choices=TENSES)
    first_person_singular = models.CharField(max_length=30)
    second_person_singular = models.CharField(max_length=30)
    third_person_singular = models.CharField(max_length=30)
    first_person_plural = models.CharField(max_length=30)
    second_person_plural = models.CharField(max_length=30)
    third_person_plural = models.CharField(max_length=30)
    
    def __str__(self):
        return self.infinitive
    