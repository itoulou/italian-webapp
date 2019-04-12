from django.conf.urls import url
from search.views import do_search

urlpatterns = [
        url(r'^search-verb/$', do_search, name="search-verb"),
    ]