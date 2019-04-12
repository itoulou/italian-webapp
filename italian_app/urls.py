"""italian_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from home import urls as home_urls
from authentication.views import login
from authentication import urls as urls_authentication
from add_verb import urls as urls_add_verb
from search import urls as urls_search

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', login, name="login"),
    url(r'^authentication/', include(urls_authentication)),
    url(r'^home/', include(home_urls)),
    url(r'^add-verb/', include(urls_add_verb)),
    url(r'^search/', include(urls_search)),
]
