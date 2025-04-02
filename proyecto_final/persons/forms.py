from collections import OrderedDict

from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput,
        min_length=8,
        help_text="Mínimo 8 caracteres"
    )
    class Meta:
        model = Person
        fields = [
            'username', 'first_name','last_name', 'email', 'birth_date', 'gender',
            'profile_picture', 'weight', 'height', 'fitness_goal',
            'activity_level',
            'allergies', 'medical_conditions', 'target_weight', 'bio', 'cuello', 'cadera', 'cintura',
        ]

    FORM_ORDER = [
        'username',
        'first_name',
        'last_name',
        'password',
        'email',
        'birth_date',
        'gender',
        'weight',
        'height',
        'cuello',
        'cadera',
        'cintura',
        'fitness_goal',
        'activity_level',
        'allergies',
        'medical_conditions',
        'target_weight',
        'profile_picture',
        'bio'
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields = OrderedDict((key, self.fields[key]) for key in self.FORM_ORDER)
