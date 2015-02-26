# -*- coding: utf-8 -*-
from django import forms
from booking.models import Person, PhoneField, TimeField
from django.forms.extras.widgets import SelectDateWidget, Select
from django.core.exceptions import ValidationError


BIRTH_YEAR_CHOICES = ('2015',)

HOURS_CHOICES = [(str(x), x) for x in range(9, 19)]
MINUTES_CHOICES = [(str(x), x) for x in range(0, 60, 10)]

CITIES = [("Донецьк", "Донецьк"), ("Київ", "Київ"), ("Львів", "Львів"), ("Луцьк", "Луцьк"), ("Одеса", "Одеса"), ("Харків", "Харків")]


class PersonForm(forms.ModelForm):
    first_name = forms.CharField(max_length=128, help_text="Введіть ім'я:")
    last_name = forms.CharField(max_length=30, help_text="Введіть прізвище:")
    organization_name = forms.CharField(max_length=30, help_text="Введіть назву установи:")
    city = forms.ChoiceField(choices=CITIES, help_text="Оберіть місто:")
    number = PhoneField(code_length=3, num_length=7, help_text="Введіть номер мобільного:")
    date = forms.DateField(widget=SelectDateWidget(years=BIRTH_YEAR_CHOICES), help_text="Оберіть дату:")
    time = TimeField(h_choices=HOURS_CHOICES, m_choices=MINUTES_CHOICES, help_text="Оберіть час:")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Person
        fields = ('last_name', 'first_name', 'city', 'organization_name', 'number', 'date', 'time' )

