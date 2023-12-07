from django.shortcuts import render
from .models import InfoUser, About, Skills, Work, Education
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