from django.conf.urls import url
from authentication.views import login, register, logout

urlpatterns = [
        url(r'^login/', login, name="login"),
        url(r'^register/', register, name="register"),
        url(r'^logout/', logout, name="logout")
    ]
