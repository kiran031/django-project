from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here. # sending the request to the server to get the required page that is doing by the by writting program by python
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def acm(request):
    return render(request,'acm.html')

def achivements(request):
   return render(request,'achivements.html')


# i am trying here to post my data in the my database by wiriting python code by the post method duo to lot of data
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        disc = request.POST.get('disc')
        contact = Contact(name=name,email=email,number=number,disc=disc,date=datetime.today())
        contact.save()

    
    return render(request,'contact.html')