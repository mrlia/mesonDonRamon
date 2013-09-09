from django.db import models

class DailyMenu(models.Model):
	name = models.CharField(max_length=200, default="Permanent")
	menu_date = models.DateTimeField('menu date')

	def __unicode__(self):
		return self.name

class Dish(models.Model):
	menu = models.ForeignKey(DailyMenu)
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=1000, default="None")

	def __unicode__(self):
		return self.name
