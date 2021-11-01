from updateme.models import Business, NeighbourHood, User
from django.shortcuts import render,redirect
from .forms import CreateUserForm,BusinessForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout as dj_login
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    businesses=Business.objects.all()

    if 'item_name' in request.GET:
        item_name=request.GET['item_name']
        businesses=businesses.filter(name__icontains=item_name)
    else:
        businesses=Business.objects.all()

    users=User.objects.all()
    neighbourhoods=NeighbourHood.objects.all()


    context={'businesses':businesses,'users':users,'neighbourhoods':neighbourhoods}
    return render(request,'index.html',context)

def registeruser(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully!. Check out our Email later :)')

            return redirect('login')
    else:
        form = CreateUserForm
    context = {
            
            'form':form,
                        }

    return render(request,'registration/register.html',context)

def loginpage(request):
    if request.user.is_authenticated:

            return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username or password is incorrect')

      
    return render(request,'registration/login.html')

def logoutuser(request):
    
    return redirect(reverse('login'))
@login_required(login_url='login')
def new_business(request):
    current_user = request.user

    if request.method =='POST':
        form = BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
           

            business.save()
    else:
        form = BusinessForm()

    return render(request,'business.html',{"form":form})

def profile(request):
    users=User.objects.all()
    context={'users':users}
    return render(request,'profile.html',context)