from django.contrib import admin
from booking.models import Person

class PersonAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('last_name',)}


admin.site.register(Person, PersonAdmin)


# Register your models here.
