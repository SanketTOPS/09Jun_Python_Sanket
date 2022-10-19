from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
   path('',views.index),
   path('getall/',views.getall),
   path('getstid/<int:id>',views.getstid),
   path('insertdata/',views.insertdata),
   path('updatedata/<int:id>',views.updatedata),
   path('deletedata/<int:id>',views.deletedata),
]
