# -*- coding: utf-8 -*-
from django.shortcuts import render
from booking.forms import PersonForm
from booking.models import Person
from datetime import datetime


def index(request):
    person_list = Person.objects.order_by('-last_name')[:10]
    context_dict = {'persons': person_list}

    # Return response back to the user, updating any cookies that need changed.
    response = render(request, 'booking/index.html', context_dict)

    return response


def person(request, person_last_name_slug):
    context_dict = {}

    try:
        person = Person.objects.get(slug=person_last_name_slug)
        context_dict['person_last_name'] = person.last_name

        # Adds our results list to the template context under name pages.
        context_dict['person_organization_name'] = person.organization_name
        context_dict['person_first_name'] = person.first_name
        context_dict['person_number'] = person.number
        context_dict['person_city'] = person.city
        context_dict['person_date'] = person.date
        context_dict['person_time'] = person.time


        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['person'] = person
    except Person.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    return render(request, 'booking/person.html', context_dict)



def booking_today(request):
    person_list = Person.objects.filter(date=datetime.today())
    context_dict = {'persons': person_list}

    response = render(request, 'booking/booking_today.html', context_dict)
    return response



def add_booking_time(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = PersonForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = PersonForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'booking/add_booking_time.html', {'form': form})
