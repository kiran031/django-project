from django.db import models

# Creating  models to create data table in my db.sqlite3 accordind to my contact page

class Contact(models.Model):
    name = models.CharField(max_length=122)  
    email =models.CharField(max_length=122)
    number =models.CharField(max_length=122)
    disc =  models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name