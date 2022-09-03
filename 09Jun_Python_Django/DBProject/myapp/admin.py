from django.contrib import admin
from .models import signup_master

# Register your models here.

class signupAdmin(admin.ModelAdmin):
    list_display=['firstname','lastname','dob','email']


admin.site.register(signup_master,signupAdmin)