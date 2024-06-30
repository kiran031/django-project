"""
URL configuration for Hello project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

#changing admin page header.title,and site_index.title so make my admin page suitable for my project
admin.site.site_header = "AITM Admin"
admin.site.site_title = "AITM Admin Portal"
admin.site.index_title = "Welcome to AITM Researcher Portal"

# making Url's dispatch helps to find out the specific page and helps to go to the app urls directory
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls'))
]
