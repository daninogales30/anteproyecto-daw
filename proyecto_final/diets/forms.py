from django import forms

from diets.models import DayDiet


class DayDietForm(forms.Form):
    class Meta:
        model = DayDiet
        fields = '__all__'