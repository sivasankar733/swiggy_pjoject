from django.contrib import messages
from django.shortcuts import render, redirect
from restaurant.models import RestaurantModel
from restaurant.forms import RestaurantForm

def restaurant(request):
    return render(request, "restaurant/manu.html")


def restaurant_registration(request):
    return render(request,"restaurant/register.html",{"rf":RestaurantForm()})


def restaurant_data(request):
    rf=RestaurantForm(request.POST)
    if rf.is_valid():
        db=rf.save(commit=False)
        db.res_otp=515101
        db.res_status='pending'
        db.save()
        messages.success(request,"once the admin aprove the registration you will receive email and a text messages")
        return redirect('restaurant')
    else:
        return render(request,"restaurant/register.html",{"rf":rf})