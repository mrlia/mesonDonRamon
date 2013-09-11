import datetime
from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from meson.models import DailyMenu, Dish

def index(request):
	return render(request, 'meson/index.html')

def about(request):
	return render(request, 'meson/about.html')

def menu(request):
    return render(request, 'meson/menu.html')

def menuPermanent(request):
    try:
        permanent_menu = DailyMenu.objects.get(name="Permanent")
    except DailyMenu.DoesNotExist:
        permanent_menu = None
    context = {'permanent_menu': permanent_menu}
    return render(request, 'meson/menuPermanent.html', context)

def menuDaily(request):
    today = datetime.date.today()
    try:
        today_menu = DailyMenu.objects.filter(menu_date__year=today.year, menu_date__month=today.month, menu_date__day=today.day)
    except DailyMenu.DoesNotExist:
        today_menu = None
    context = {'today_menu': today_menu, 'today': today.isoformat()}
    return render(request, 'meson/menuDaily.html', context)

def events(request):
	return render(request, 'meson/events.html')

def booking(request):
	return render(request, 'meson/booking.html')

def contact(request):
	return render(request, 'meson/contact.html')
