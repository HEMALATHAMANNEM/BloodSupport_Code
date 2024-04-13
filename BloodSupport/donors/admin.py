from django.contrib import admin
from .models import Donor
# Register your models here.


class DonorAdmin(admin.ModelAdmin):
    list_display=['firstname','lastname','email','phone','bloodgroup','address']

admin.site.register(Donor,DonorAdmin)