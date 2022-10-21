from django.contrib import admin

# Register your models here.

from . models import design,team
#
admin.site.register(design)
admin.site.register(team)
#
# admin.site.register(work)