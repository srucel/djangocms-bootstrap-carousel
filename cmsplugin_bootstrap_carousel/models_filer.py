# coding: utf-8
from django.db import models
from django.utils.translation import ugettext as _

from filer.fields.image import FilerImageField
from djangocms_link.models import Link

class CarouselItem(models.Model):
    carousel = models.ForeignKey(Carousel)
    caption_title = models.CharField(max_length=100, blank=True, null=True)
    caption_content = models.TextField(blank=True, null=True)
    image = FilerImageField(blank=True, null=True)
    link = models.ForeignKey(Link, blank=True, null=True)  # use django reverse or link to a page...
