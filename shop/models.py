from django.db import models
from django.utils import timezone


class Product(models.Model):
	name = models.CharField(max_length=100)	
	price = models.DecimalField(max_digits=10, decimal_places=2)
	stock = models.PositiveIntegerField()
	created_at = models.DateTimeField(default=timezone.now)
	description = models.TextField(blank=True)
	slug = models.SlugField(unique=True, blank=True)
	category = models.ForeignKey("Category", related_name='products', on_delete=models.CASCADE)

	class Meta:
		ordering = ('name', )


class Category (models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(unique=True, blank=True)	
	created_at = models.DateTimeField(default=timezone.now)
	description = models.TextField(max_length=256)
	

	class Meta:
		ordering = ('name', )

