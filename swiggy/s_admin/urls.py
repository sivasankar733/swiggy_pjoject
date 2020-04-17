"""swiggy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path



from s_admin import views

urlpatterns = [
    path('',views.admin_login,name='admin_login'),
    path('adminlog_check/',views.loging_page,name='adminlog_check'),
    path('adminhome_page/',views.adminhome_page,name='adminhome_page'),
    path('admin_logout/',views.admin_logout,name='admin_logout'),
    path('upate_state_data/',views.update_state_data,name='upate_state_data'),
    path('delete_state/',views.delete_state,name='delete_state'),

    #state
    path('state_open/',views.statelogin,name='state_open'),
    path('save_state/',views.savestate,name='save_state'),
    path('update_state',views.update_state,name='update_state'),
    path('upate_state_data/',views.update_state_data,name='upate_state_data'),
    path('delete_state/',views.delete_state,name='delete_state'),

    #city
    path('city_open/',views.city_open,name='city_open'),
    path('city_data/',views.city_savedata,name='city_data'),
    path('update_city/',views.city_update,name='update_city'),
    path('update_city_data/',views.update_city_data,name='update_city_data'),
    path('delete_city/',views.delete_city,name='delete_city'),

    #area
    path('area_open/',views.area_open,name='area_open'),
    path('area_save/',views.area_save,name='area_save'),
    path('update_area/',views.update_area,name='update_area'),
    path('update_save_data/',views.update_data_save,name='update_save_data'),
    path('delete_area/',views.delete_area,name='delete_area'),

    #type
    path('type_open/',views.type_open,name='type_open'),
    path('type_save/',views.type_data_save,name='type_save'),
    path('update_type/',views.type_update,name='update_type'),
    path('update_type_data/',views.update_type_data,name='update_type_data'),
    path('delete_type/',views.delete_type,name='delete_type'),

    #restaurant
    path('restaurant_details/',views.pending_res_details,name='restaurant_details'),
    path('show_approval/',views.show_approval,name='show_approval'),
    path('show_cancel/',views.show_cancel,name='show_cancel'),
    path('accept_res/',views.accept_res,name='accept_res'),
    path('reject_res/',views.reject_res,name='reject_res'),

]
