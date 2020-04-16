from django import forms
from s_admin.models import StateModel,CityModel,AreaModel,RestauranrTypeModel


class StateForm(forms.ModelForm):
    class Meta:
        model=StateModel
        fields="__all__"

class CityForm(forms.ModelForm):
    class Meta:
        model=CityModel
        fields="__all__"
        exclude=("city_no",)
class AreaForm(forms.ModelForm)  :
    class Meta:
        model=AreaModel
        fields="__all__"
        exclude= ('area_no',)

class RestaurantTypeForm(forms.ModelForm):
    class Meta:
        model=RestauranrTypeModel
        fields="__all__"
        exclude=('type_no',)