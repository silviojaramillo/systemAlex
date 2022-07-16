from django.shortcuts import render

from .models import AboutMe

# Create your views here.
def about(request):
    biography = AboutMe.objects.all()
    return render(request,"about/about.html",{'biography': biography})