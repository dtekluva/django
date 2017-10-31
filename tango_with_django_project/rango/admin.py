from django.contrib import admin
from rango.models import Category, Page





class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'Category', 'url')

# Register your models here.



class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# Update the registeration to include this customised interface
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)