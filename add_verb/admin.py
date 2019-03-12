from django.contrib import admin
from add_verb.models import Verb_ARE, Verb_ARELineItem, Verb_ERE, Verb_ERELineItem, Verb_IRE, Verb_IRELineItem
from add_verb.forms import Verb_ARE_LineForm

# Register your models here.
class VerbAREAdminInline(admin.TabularInline):
    model = Verb_ARELineItem

class VerbAREAdmin(admin.ModelAdmin):
    inlines = (VerbAREAdminInline, )
    
class VerbEREAdminInline(admin.TabularInline):
    model = Verb_ERELineItem

class VerbEREAdmin(admin.ModelAdmin):
    inlines = (VerbEREAdminInline, )
    
class VerbIREAdminInline(admin.TabularInline):
    model = Verb_IRELineItem

class VerbIREAdmin(admin.ModelAdmin):
    inlines = (VerbIREAdminInline, )    

admin.site.register(Verb_ARE, VerbAREAdmin)     
admin.site.register(Verb_ERE, VerbEREAdmin)
admin.site.register(Verb_IRE, VerbIREAdmin)
