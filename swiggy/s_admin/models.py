from django.db import models

class LoginModel(models.Model):
    admin_name=models.CharField(max_length=40)
    admin_password=models.CharField(max_length=30)
    otpcode=models.IntegerField(unique=True)

class StateModel(models.Model):
    state_no=models.IntegerField(primary_key=True)
    state_name=models.CharField(max_length=60)

    def __str__(self):
        return self.state_name

class CityModel(models.Model):
    city_no=models.IntegerField(primary_key=True)
    city_name=models.CharField(max_length=50)
    state=models.ForeignKey(StateModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name

class AreaModel(models.Model):
    area_no=models.IntegerField(primary_key=True)
    area_name=models.CharField(max_length=40)
    city=models.ForeignKey(CityModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.area_name

class RestauranrTypeModel(models.Model):
    type_no=models.IntegerField(primary_key=True)
    type_name=models.CharField(max_length=40)

    def __str__(self):
        return self.type_name
