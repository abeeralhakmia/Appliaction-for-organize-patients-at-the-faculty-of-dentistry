from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path("register",views.register,name="register"),
path("login",views.login,name="login"),
path("getAllsections",views.getAllsections,name="getAllsections"),
path("getAllSports",views.getAllSports,name="getAllSports"),
path("getsportsById",views.getsportsById,name="getsportsById"),
path("getAllPhysicals",views.getAllPhysicals,name="getAllPhysicals"),
path("getphysicalTherapyById",views.getphysicalTherapyById,name="getphysicalTherapyById"),
path("getAllFeeds",views.getAllFeeds,name="getAllFeeds"),
path("getfeedById",views.getfeedById,name="getfeedById"),


]