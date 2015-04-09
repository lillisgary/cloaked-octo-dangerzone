from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.pages.models import Page
from mezzanine.core.models import RichText

class HomePage(Page, RichText):
	
	class Meta:
		verbose_name = _("Home page")
		verbose_name_plural = _("Home pages")
