from django.db import models

class DailyMenu(models.Model):
	name = models.CharField(max_length=200)
	menu_date = models.DateTimeField('menu date')

	def __unicode__(self):
		return self.name

class Dish(models.Model):
	menu = models.ForeignKey(DailyMenu)
	name = models.CharField(max_length=200)
	DISH_TYPE_CHOICE = (
		('Dr', 'Drinks'),
		('B', 'Bocatines'),
		('Ta', 'Tapas'),
		('To', 'Tostas'),
		('R', 'Raciones'),
		('1', 'First'),
		('2', 'Second'),
		('De', 'Dessert'),
	)
	dish_type = models.CharField(max_length=10, choices=DISH_TYPE_CHOICE)
	description = models.CharField(max_length=1000, default="None")
	price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

	def __unicode__(self):
		return self.name
