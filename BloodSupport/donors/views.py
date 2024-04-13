from multiprocessing import context
from django.shortcuts import redirect, render, reverse
from .forms import DonorForm
from .models import Donor
from django.template import loader
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
from tkinter import *
from templates import *


def Home(request):
    return render(request,'home.html')

def SignupPage(request):
    form=DonorForm()
    if request.method=='POST':
        pass1=request.POST.get('password')
        pass2=request.POST.get('password2')
        uname=request.POST.get('username')
        email=request.POST.get('email')
        
        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            form=DonorForm(request.POST)
            if form.is_valid():
                form.save()
                my_user=User.objects.create_user(uname,email,pass1)
                my_user.save()
                return HttpResponse("Sucessfully Registered!!")
            else:
                return HttpResponse("Invalid Registration. Email ID, Username, Phone Number must be unique!!")
            #form=DonorForm()
            #return redirect('adddonor')
    context={
        'form':form,
    }
        
    return render (request,'addDonor.html',context)


def LoginPage(request):
    msg=""
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        #user=authenticate(request,email=email,password=pass1)
        user=authenticate(request,username=username,password=pass1)
        #print(user,username)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('admindashboard')
            else:
                return redirect('donordashboard')
        else:
            i=Donor.objects.get(username=username)
            if i.password==pass1:
                login(request,user)
                return redirect('donordashboard')
            else:
                msg="Username or Password is incorrect!!!"

    return render (request,'login.html',{'msg':msg})

@login_required(login_url='login')
@user_passes_test(lambda user:not user.is_staff)
def DonorDashboard(request):
    user=request.user.username
    i=Donor.objects.get(username=user)
    context={
        'i':i,
    }
    return render(request,'DonorDashboard.html',context)


@login_required(login_url='login')
@user_passes_test(lambda user:user.is_staff)
def AdminDashboard(request):
    return render(request,'AdminDashboard.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@user_passes_test(lambda user:user.is_staff)
def BloodGroups(request):
    context={
        'data':['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    }
    return render(request,'index.html',context)

@login_required(login_url='login')
@user_passes_test(lambda user:user.is_staff)
def DonorsPage(request):    
    data=Donor.objects.all()
    context={
        'data':data,
    }
    return render(request,'displayDonors.html',context)


#Donor
@login_required(login_url='login')
def DonorDetails(request,id):
    i=Donor.objects.get(id=id)
    context={
        'i':i,
    }
    return render(request,'donorDetails.html',context)

# Delete View
@login_required(login_url='login')
def DeleteDonor(request,id):
    a=Donor.objects.get(pk=id)
    username=a.username
    u=User.objects.get(username=username)
    u.delete()
    a.delete()
    return redirect('/')
    

# Update View
@login_required(login_url='login')
@user_passes_test(lambda user:not user.is_staff)
def UpdateDonor(request,id):
    if request.method=='POST':
        data=Donor.objects.get(pk=id)
        form=DonorForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect(reverse('donordashboard'))
        else:
            return HttpResponse("Invalid Registration. Email ID, Username, Phone Number must be unique!!")
    else:
        data=Donor.objects.get(pk=id)
        form=DonorForm(instance=data)
        field = form.fields['username']
        field.widget = field.hidden_widget()
    context={
        'form':form,
    }
    return render (request,'updateDonor.html',context)


@login_required(login_url='login')
@user_passes_test(lambda user:user.is_staff)
def RequiredDonorDetails(request,bloodgroup):
    i=Donor.objects.filter(bloodgroup=bloodgroup).values()
    context={
        'data':i,
    }
    return render(request,'displayDonorsAtLoginPage.html',context)

