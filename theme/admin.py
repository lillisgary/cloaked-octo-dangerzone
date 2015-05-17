from django.contrib import admin

from mezzanine.pages.admin import PageAdmin
from .models import HomePage, Slide, Portfolio, PortfolioItem, PortfolioItemImage, PortfolioItemCategory
from mezzanine.core.admin import TabularDynamicInlineAdmin

class SlideInline(TabularDynamicInlineAdmin):
    model = Slide

class HomePageAdmin(PageAdmin):
	inlines = (SlideInline,)

class PortfolioItemImageInline(TabularDynamicInlineAdmin):
    model = PortfolioItemImage

class PortfolioItemAdmin(PageAdmin):
    inlines = (PortfolioItemImageInline,)
	
admin.site.register(HomePage, HomePageAdmin)
admin.site.register(Portfolio, PageAdmin)
admin.site.register(PortfolioItemCategory)
admin.site.register(PortfolioItem, PortfolioItemAdmin)
