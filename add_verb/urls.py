from django.conf.urls import url
from add_verb.views import add_verb_are

urlpatterns = [
        url(r'add-verb-are', add_verb_are, name="add-verb-are")
    ]