from django.contrib import admin
from .models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('title', 'order')
    ordering = ('order', 'title')
    search_fields = ('title', 'content')
    fields = ('title', 'content', 'slug', 'order', 'visible', 'created_at', 'updated_at')
    #fields = ('title', 'content', 'order', 'visible')
    
admin.site.register(Page, PageAdmin)