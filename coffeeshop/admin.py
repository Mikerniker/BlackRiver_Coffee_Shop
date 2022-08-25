from django.contrib import admin
from .models import Coffee


class CoffeeAdmin(admin.ModelAdmin):
    list_display = ('coffee', 'status', 'team_member')


# Register your models here.
admin.site.register(Coffee, CoffeeAdmin)

