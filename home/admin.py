from django.contrib import admin

#importing Created Contact Model in my app admin page so i can register
from home.models import Contact

# Register your models here.
admin.site.register(Contact)