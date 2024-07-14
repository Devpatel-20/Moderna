from django.contrib import admin
from .models import *

# Register your models here.

class Contactforadmin(admin.ModelAdmin):
  list_display = ["name","email","subject", "message"]
admin.site.register(Contact,Contactforadmin)

class Testimonialforadmin(admin.ModelAdmin):
  list_display = ["name","designation","img","content"]
admin.site.register(Testimonial,Testimonialforadmin)  


class Teamforadmin(admin.ModelAdmin):
    list_display = ["name","designation","img","content"]
admin.site.register(Team,Teamforadmin)  