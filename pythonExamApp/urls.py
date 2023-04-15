from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index),
    path("register", views.register),
    path("travels", views.travels),
    path("logout", views.logout),
    path("login", views.login),
    path("travels/add", views.addtrip),
    path("createtrip", views.createtrip),
    path("destination/<tripID>", views.tripdetails),
    path("JoinTrip/<tripID>", views.JoinTrip),
    path("cancel/<tripID>", views.cancel),
    path('home/', views.home, name='home')
]
 