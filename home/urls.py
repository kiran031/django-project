from django.contrib import admin
from django.urls import path,include
from home import views

#url dispatching to get the required different pages
urlpatterns = [
    path('',views.index,name="home"),
    path('about',views.about,name="about"),
    path('acm',views.acm,name="acm"),
    path('achivements',views.achivements,name="achivements"),
    path('contact',views.contact,name="contact"),
]