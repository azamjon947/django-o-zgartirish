from django.shortcuts import render
from .models import Home

def about(request):
    home = Home.objects.all()
    context = {
        "malumot": home
    }
    return render(request, 'base.html', context)
