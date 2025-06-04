from django import forms

from diets.models import DayDiet, SemanalDiet, FoodItem, Day


class DayDietForm(forms.ModelForm):
    class Meta:
        model = DayDiet
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['semanal_diet'].queryset = SemanalDiet.objects.filter(user=user)

            # Obtener semanal_diet_id de los datos enviados (POST/GET)
            semanal_diet_id = None
            if 'semanal_diet' in self.data:
                try:
                    semanal_diet_id = int(self.data.get('semanal_diet'))
                except (ValueError, TypeError):
                    pass
            elif self.instance.pk:
                semanal_diet_id = self.instance.semanal_diet_id

            # Actualizar el queryset de day
            if semanal_diet_id:
                self.fields['day'].queryset = Day.objects.filter(semanal_diet_id=semanal_diet_id)
            else:
                self.fields['day'].queryset = Day.objects.none()
        else:
            self.fields['semanal_diet'].queryset = SemanalDiet.objects.none()
            self.fields['day'].queryset = Day.objects.none()

    def clean(self):
        cleaned_data = super().clean()
        semanal_diet = cleaned_data.get('semanal_diet')
        day = cleaned_data.get('day')

        if semanal_diet and day:
            if not Day.objects.filter(id=day.id, semanal_diet=semanal_diet).exists():
                self.add_error('day', 'El día seleccionado no pertenece a la dieta semanal.')

        return cleaned_data


class DayDietUpdateForm(forms.ModelForm):
    class Meta:
        model = DayDiet
        fields = ['semanal_diet', 'day', 'moment', 'food_item', 'quantity_g', 'notes']

        widgets = {
            'semanal_diet': forms.TextInput(attrs={'readonly': 'readonly'}),
            'day': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['semanal_diet'].disabled = True
        self.fields['day'].disabled = True


class DayForm(forms.ModelForm):
    class Meta:
        model = Day
        fields = ['semanal_diet', 'day']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(DayForm, self).__init__(*args, **kwargs)
        if user:
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
