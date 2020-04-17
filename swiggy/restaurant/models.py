from django.db import models
from s_admin.models import AreaModel
from s_admin.models import RestauranrTypeModel


class RestaurantModel(models.Model):
    res_id=models.IntegerField(primary_key=TabError)
    res_name=models.CharField(unique=True,max_length=40)
    res_contact=models.IntegerField(unique=True)
    res_email=models.EmailField(unique=True)
    res_area=models.ForeignKey(AreaModel,on_delete=models.CASCADE)
    res_type=models.ForeignKey(RestauranrTypeModel,on_delete=models.CASCADE)
    res_password=models.CharField(max_length=30)
    res_otp=models.IntegerField()
    res_status=models.CharField(max_length=30,default=False)