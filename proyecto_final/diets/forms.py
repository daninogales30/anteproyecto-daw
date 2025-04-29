from django import forms

from diets.models import DayDiet, SemanalDiet, FoodItem


class DayDietForm(forms.ModelForm):
    class Meta:
        model = DayDiet
        fields = '__all__'

class SemanalDietForm(forms.ModelForm):
    class Meta:
        model = SemanalDiet
        fields = ['name', 'start_date', 'finish_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'finish_date': forms.DateInput(attrs={'type': 'date'}),
        }

class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name', 'calories_per_100g', 'category', 'notes']
