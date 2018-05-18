from django.contrib import admin
from . import models
import decimal


#========== General Functions ========== 
admin.site.site_title = "Coretabs Online Shop Administration"
admin.site.site_header = "Coretabs Online Shop Administration"


#========== Category Functions ==========
@admin.register(models.Category)			
class CategoryAdmin(admin.ModelAdmin):
	date_hierarchy = 'created_at'
	search_fields = ['name']                  
	list_display = ('id', 'name', 'description',)  
	


#========== Product Functions ==========
def make_price_zero(modeladmin, request, queryset):      #action list option
    queryset.update(price=0)

make_price_zero.short_description = "Make selected products free"

def discount(modeladmin, request, queryset):             #action list option
        for product in queryset:
            discount = decimal.Decimal(product.price) * decimal.Decimal(0.2)
            queryset.update(price=product.price - discount)

discount.short_description = "Make 20%% Discount for selected items"

    
@admin.register(models.Product)			
class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'       
    search_fields = ['name']                   
    list_display = ('name', 'price', 'stock', 'description', 'category',)
    list_filter = ('created_at', 'category',)
    actions = [make_price_zero, discount,]
    






	




