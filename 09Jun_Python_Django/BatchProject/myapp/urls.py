from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('notes/',views.notes,name='notes'),
    path('profile/',views.profile,name='profile'),
    path('userlogout/',views.userlogout),
]