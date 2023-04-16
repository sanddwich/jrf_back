from django.contrib import admin

from .models import *

class ArticlesAdmin(admin.ModelAdmin):
  list_display = ['id', 'title', 'info', 'content', 'create_date',
                  'modification_date', 'ispublished', 'awatar', 'category', 'user', 'slug']
  list_display_links = ['id', 'title']
  search_fields = ['title', 'info', 'content']
  list_editable = ['ispublished']
  list_filter = ['ispublished']
  prepopulated_fields = {"slug": ["title"]}

class CategoriesAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'create_date', 'modification_date', 'slug']
  list_display_links = ['id', 'name']
  search_fields = ['name']
  prepopulated_fields = {"slug": ["name"]}

# Register your models here.
admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Categories, CategoriesAdmin)