from django.contrib import admin
from .models import post


class postAdmin(admin.ModelAdmin):
    list_display=('title', 'date_created', 'auther')

# Register your models here.
admin.site.register(post, postAdmin)