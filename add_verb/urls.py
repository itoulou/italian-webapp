from django.conf.urls import url
from add_verb.views import add_verb_are, add_verb_ere, add_verb_ire

urlpatterns = [
        url(r'add-verb-are/', add_verb_are, name="add-verb-are"),
        url(r'add_verb_ere/', add_verb_ere, name="add-verb-ere"),
        url(r'add_verb_ire/', add_verb_ire, name="add-verb-ire"),
    ]