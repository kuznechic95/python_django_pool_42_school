from django.shortcuts import render
from django.http import HttpResponse

from .models import People, Planets


def display(request):
    try:
        people = People.objects.filter(homeworld__climate__contains='windy')\
                .values('name', 'homeworld__name', 'homeworld__climate')\
                .order_by('name')
    except Exception as exception:
        return HttpResponse(exception)
    return render(request, 'ex09/display.html', {'people': people})

