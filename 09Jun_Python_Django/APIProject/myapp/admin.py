from django.contrib import admin
from .models import userData

# Register your models here.

class userAdmin(admin.ModelAdmin):
    list_display=['name','email','sub']

admin.site.register(userData,userAdmin)
