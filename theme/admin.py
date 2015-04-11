from django.contrib import admin

from mezzanine.pages.admin import PageAdmin
from .models import HomePage, Slide
from mezzanine.core.admin import TabularDynamicInlineAdmin

class SlideInline(TabularDynamicInlineAdmin):
    model = Slide

class HomePageAdmin(PageAdmin):
	inlines = (SlideInline,)
	
admin.site.register(HomePage, HomePageAdmin)
