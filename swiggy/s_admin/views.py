from django.contrib import messages
from django.shortcuts import render, redirect
from s_admin.models import LoginModel
from s_admin.models import StateModel,CityModel,AreaModel,RestauranrTypeModel
from s_admin.forms import StateForm,CityForm,AreaForm,RestaurantTypeForm

def admin_login(request):
    return render(request,'s_admin/admin_log.html')


def loging_page(request):
    ausername=request.POST.get("username")
    apassword=request.POST.get("password")
    try:
        LoginModel.objects.get(admin_name=ausername,admin_password=apassword)
        request.session['status']= True
        return redirect('adminhome_page')
    except LoginModel.DoesNotExist:
        messages.success(request, "invalid username and password")
        return redirect("admin_login")


def adminhome_page(request):
    return render(request,"s_admin/adminhome.html")


def admin_logout(request):
    request.session['status']= False
    return redirect('admin_login')


def statelogin(request):
    sdata=StateModel.objects.all()
    return render(request,"s_admin/stateopen.html",{"sf":StateForm(),"sdata":sdata})


def savestate(request):
    stf=StateForm(request.POST)
    if stf.is_valid():
        stf.save()
        return redirect('state_open')
    else:
        return render(request,"s_admin/stateopen.html",{"sf":stf})


def update_state(request):
    sno=request.GET.get("sno")
    sname=request.GET.get("sname")
    d1={"sno":sno,"sname":sname}
    return render(request,"s_admin/stateopen.html",{"supdate_data":d1,"sdata":StateModel.objects.all()})


def update_state_data(request):
    sno=request.POST.get("s1")
    sname=request.POST.get("s2")
    StateModel.objects.filter(state_no=sno).update(state_name=sname)
    return redirect('state_open')


def delete_state(request):
    sno=request.GET.get("sno")
    StateModel.objects.filter(state_no=sno).delete()
    return redirect('state_open')


def city_open(request):
    return render(request,"s_admin/city_open.html",{"cf":CityForm,"sdata":CityModel.objects.all()})

def city_savedata(request):
    cf=CityForm(request.POST)
    if cf.is_valid():
        cf.save()
        return redirect('city_open')
    else:
        return render(request,"s_admin/city_open.html",{"cf":cf})

def city_update(request):
    cno=request.GET.get("cno")
    cname=request.GET.get('cname')
    d1 = {"cno":cno,"cname":cname}
    return render(request,"s_admin/city_open.html",{"cupdate_data":d1,"sdata":CityModel.objects.all()})


def update_city_data(request):
    cno=request.POST.get('t1')
    cname=request.POST.get('t2')
    CityModel.objects.filter(city_no=cno).update(city_name=cname)
    return redirect('city_open')


def delete_city(request):
    cno=request.GET.get("cno")
    CityModel.objects.filter(city_no=cno).delete()
    return redirect('city_open')


def area_open(request):
    return render(request,"s_admin/area_open.html",{"af":AreaForm(),"sdata":AreaModel.objects.all()})


def area_save(request):
    af=AreaForm(request.POST)
    if af.is_valid():
        af.save()
        return redirect('area_open')
    else:
        return render(request,"s_admin/area_open.html",{"af":af})


def update_area(request):
    ano=request.GET.get("ano")
    aname=request.GET.get("aname")
    d1={"ano":ano,"aname":aname}
    return render(request,"s_admin/area_open.html",{"aupdate_data":d1,"sdata":AreaModel.objects.all()})


def update_data_save(request):
    ano=request.POST.get("d1")
    aname=request.POST.get("d2")
    AreaModel.objects.filter(area_no=ano).update(area_name=aname)
    return redirect("area_open")


def delete_area(request):
    ano=request.GET.get('ano')
    AreaModel.objects.filter(area_no=ano).delete()
    return redirect('area_open')


def type_open(request):
    return render(request,"s_admin/type_open.html",{"rtf":RestaurantTypeForm(),"sdata":RestauranrTypeModel.objects.all()})


def type_data_save(request):
    rtf=RestaurantTypeForm(request.POST)
    if rtf.is_valid():
        rtf.save()
        return redirect('type_open')


def type_update(request):
    tno=request.GET.get("tno")
    tname=request.GET.get("tname")
    d1={"tno":tno,"tname":tname}
    return render(request,"s_admin/type_open.html",{"tupdate_data":d1,"sdata":RestauranrTypeModel.objects.all()})

def update_type_data(request):
    tno = request.POST.get("t1")
    tname = request.POST.get("t2")
    AreaModel.objects.filter(type_no=tno).update(type_name=tname)
    return redirect("type_open")

def delete_type(request):
    tno=request.GET.get("tno")
    RestauranrTypeModel.objects.filter(type_no__exact=tno).delete()
    return redirect('type_open')