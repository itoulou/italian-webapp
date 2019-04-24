from django.conf.urls import url
from view_verb.views import view_verb, choose_tense

urlpatterns = [
        url(r'^(?P<pk>\d+)/(?P<infinitive>\w+)/$', view_verb, name="view-verb"),
        url(r'^(?P<pk>\d+)/(?P<infinitive>\w+)/tense/$', choose_tense, name="choose-tense"),
    ]