from django.contrib import admin

# Register your models here.
from app.models import RegistModel


class RegistAdmin(admin.ModelAdmin):
    list_display = ('id','name','age','gender','created')


admin.site.register(RegistModel, RegistAdmin)