from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.fields import FileField
from mezzanine.pages.models import Page
from mezzanine.core.models import RichText, Orderable
from mezzanine.utils.models import upload_to

class HomePage(Page, RichText):
	
	
	class Meta:
		verbose_name = _("Home page")
		verbose_name_plural = _("Home pages")

class Slide(Orderable):
    '''
    A slide in a slider connected to a HomePage
    '''
    homepage = models.ForeignKey(HomePage, related_name="slides")
    image = FileField(verbose_name=_("Image"),
        upload_to=upload_to("theme.Slide.image", "slider"),
        format="Image", max_length=255, null=True, blank=True)
    featured_image = models.NullBooleanField(blank=True, help_text="The active 1st image to appear")

    
