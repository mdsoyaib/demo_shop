from django.contrib import admin

# Register your models here.
from core.models import Category, Product

admin.site.site_header = "Shop Admin Panel"


# admin.site.register(Category)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


# admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'price', 'quantity', 'photo', 'unit_type')
    list_filter = ('category', 'price')
    search_fields = ('name', 'price')
    list_display_links = ('name',)
