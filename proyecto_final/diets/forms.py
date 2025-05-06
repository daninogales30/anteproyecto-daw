from django import forms

from diets.models import DayDiet, SemanalDiet, FoodItem, Day


class DayDietForm(forms.ModelForm):
    class Meta:
        model = DayDiet
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Obtenemos el usuario desde las kwargs
        super(DayDietForm, self).__init__(*args, **kwargs)
        if user:
            # Filtramos los workouts por el usuario actual
            self.fields['semanal_diet'].queryset = SemanalDiet.objects.filter(user=user)


class DayForm(forms.ModelForm):
    class Meta:
        model = Day
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Obtenemos el usuario desde las kwargs
        super(DayForm, self).__init__(*args, **kwargs)
        if user:
            # Filtramos los workouts por el usuario actual
            self.fields['semanal_diet'].queryset = SemanalDiet.objects.filter(user=user)

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
