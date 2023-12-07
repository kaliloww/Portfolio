from django.shortcuts import render, redirect
from .models import InfoUser, About, Skills, Work, Education, Contact
# Create your views here.

def index(request):
    infouser = InfoUser.objects.latest("id")
    return render(request,"index.html", locals())

def about(request):
    about = About.objects.latest("id")
    skill = Skills.objects.all
    work = Work.objects.all
    education = Education.objects.all
    return render(request,"about.html", locals())

def contact(request):
    infouser = InfoUser.objects.latest("id")
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        Contact.objects.create(name= name , email = email , message=message)
        return redirect('index')
    return render(request, "contact.html", locals())