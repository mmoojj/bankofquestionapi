from django.contrib import admin
from .models import Quize 
from django.contrib.auth import  get_user_model
# Register your models here.




class UserAdmin(admin.ModelAdmin):
    list_display=[
        'username','first_name', 'last_name','is_active','is_staff','image_tag'
    ]
admin.site.register(get_user_model(),UserAdmin)        

class QuizeAdmin(admin.ModelAdmin):
    list_display=['title','owner','ispublish','date']

admin.site.register(Quize,QuizeAdmin)