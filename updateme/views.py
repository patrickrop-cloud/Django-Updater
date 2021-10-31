from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout as dj_login
from .forms import CreateUserForm, BusinessForm
from updateme.models import Business, NeighbourHood, User

# Create your views here.

def index(request):
    businesses = Business.objects.all()
    if 'item_name' in request.GET:
        item_name=request.GET['item_name']
        businesses=businesses.filter(name_icontains=item_name)
    else:
        businesses=Business.objects.all()

    user = User.objects.all()
    neighbourHood=NeighbourHood.objects.all()

    context = {'businesses':businesses,'users':users,'neighbourhoods':neighbourhoods}
    return render(request,'index.html',context)
