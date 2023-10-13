from my_website import views
from django.urls import path

urlpatterns = [
    path("", views.contact, name="contact"),
    path("download", views.download, name="download"),
    path("", views.index, name="index"),
]
