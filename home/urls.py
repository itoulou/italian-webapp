from django.conf.urls import url
from home.views import home

urlpatterns = [
        url(r'^$', home, name="home"),
    ]