from django.contrib import admin
from meson.models import DailyMenu
from meson.models import Dish

class DishInline(admin.TabularInline):
	model = Dish
	extra = 6

class DailyMenuAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['name']}),
		('Menu Date', {'fields': ['menu_date']}),
	]
	inlines = [DishInline]
	list_display = ('name', 'menu_date')
	list_filter = ['menu_date']
	search_fields = ['name']
	date_hierarchy = 'menu_date'

admin.site.register(DailyMenu, DailyMenuAdmin)
