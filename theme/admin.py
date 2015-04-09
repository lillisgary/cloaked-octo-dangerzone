from django.contrib import admin

from mezzanine.pages.admin import PageAdmin
from .models import HomePage

class HomePageAdmin(PageAdmin):
	pass
	
admin.site.register(HomePage, HomePageAdmin)
