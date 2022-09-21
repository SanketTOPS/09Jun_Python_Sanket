from django.contrib import admin
from .models import userSignup

# Register your models here.

class signupAdmin(admin.ModelAdmin):
    list_display=['firstname','lastname','username','city','state']

admin.site.register(userSignup,signupAdmin)
