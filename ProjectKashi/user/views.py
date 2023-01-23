from django.shortcuts import render
from .models import *


# Create your views here.
def home(request):
    return render(request, 'user/index.html')


def Ghat(request):
    return render(request, 'user/Ghat.html')


def About(request):
    return render(request, 'user/about.html')


def Videos(request):
    return render(request, 'user/videos.html')


def Kashi(request):
    return render(request, 'user/Kashi.html')


def StudentLearning(request):
    return render(request, 'user/StudentLearning.html')


def Places(request):
    return render(request, 'user/Places.html')


def Contact(request):
    if request.method == 'POST':
        Name = request.POST.get("name", "")
        Email = request.POST.get("email", "")
        Number = request.POST.get("number", "")
        DOB = request.POST.get("dob","")
        Password = request.POST.get("password", "")
        ConfirmPassword = request.POST.get("conformPassword","")
        a = Contact(name=Name, email=Email, number=Number, dob=DOB, password=Password, conformPassword=ConfirmPassword)
        a.save()
    return render(request, 'user/Contact.html')
