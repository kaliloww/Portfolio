from django.shortcuts import render
from .models import InfoUser
# Create your views here.

def index(request):
    infouser = InfoUser.objects.latest("id")
    return render(request,"index.html", locals())

def about(request):
    return render(request,"about.html",locals())