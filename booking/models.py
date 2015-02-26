# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.db import IntegrityError
from django.forms import MultiValueField, CharField, ChoiceField, MultiWidget, TextInput, Select



class PhoneWidget(MultiWidget):
    def __init__(self, code_length=3, num_length=7, attrs=None):
        widgets = [TextInput(attrs={'size': code_length, 'maxlength': code_length}),
                   TextInput(attrs={'size': num_length, 'maxlength': num_length})]
        super(PhoneWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.code, value.number]
        else:
            return ['', '']

    def format_output(self, rendered_widgets):
        return '+38' + '(' + rendered_widgets[0] + ') - ' + rendered_widgets[1]


class PhoneField(MultiValueField):
    def __init__(self, code_length, num_length, *args, **kwargs):
        list_fields = [CharField(),
                       CharField()]
        super(PhoneField, self).__init__(list_fields, widget=PhoneWidget(code_length, num_length), *args, **kwargs)

    def compress(self, values):
        return '+38' + values[0] + values[1]



HOURS_CHOICES = [(str(x), x) for x in range(9, 19)]
MINUTES_CHOICES = [(str(x), x) for x in range(0, 60, 10)]

class TimeWidget(MultiWidget):
    def __init__(self, h_choices, m_choices, attrs=None):
        widgets = [Select(choices=h_choices),
                   Select(choices=m_choices)]
        super(TimeWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.hours, value.minutes]
        else:
            return ['', '']


class TimeField(MultiValueField):
    def __init__(self, h_choices, m_choices, *args, **kwargs):
        list_fields = [ChoiceField(choices=h_choices),
                       ChoiceField(choices=m_choices)]
        super(TimeField, self).__init__(list_fields, widget=TimeWidget(h_choices, m_choices),*args, **kwargs)

    def compress(self, values):
        return values[0] + ':' + values[1]


BIRTH_YEAR_CHOICES = ('2015',)



class Person(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=30)
    organization_name = models.CharField(max_length=30, unique=True)
    city = models.CharField(max_length=30)
    number = models.CharField(max_length=30)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.date)+str(self.time))
        super(Person, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.last_name