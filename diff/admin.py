from django.contrib import admin
from .models import InterfaceModel,User
# Register your models here.
class InterfaceAdmin(admin.ModelAdmin):
    list_display = ['cid','testurl','defaulturl','querycount','topn','pn','countrepeat','statusflag','resultflag','threadnum','reason','remark','creater','create_time','status','upload','selfdata']

admin.site.register(InterfaceModel,InterfaceAdmin)
admin.site.register(User)
