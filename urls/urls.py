from django.urls import path
from . import views

app_name = "urls"

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.addUrl.as_view(), name="add"),
    #path("add/", views.url_create, name="add"),
]