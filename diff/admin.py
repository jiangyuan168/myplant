from django.contrib import admin
from .models import InterfaceModel
# Register your models here.
class InterfaceAdmin(admin.ModelAdmin):
    list_display = ['testurl','defaulturl','querycount','topn','pn','countrepeat','statusflag','resultflag','threadnum','reason','remark','creater']

admin.site.register(InterfaceModel,InterfaceAdmin)
