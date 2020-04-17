from django import forms

from restaurant.models import RestaurantModel


class RestaurantForm(forms.ModelForm):
    class Meta:
        model=RestaurantModel
        fields="__all__"
        exclude=("res_id","res_otp","res_status",)