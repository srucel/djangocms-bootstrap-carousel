# coding: utf-8

from base import CarouselItemAbstract
from filer.fields.image import FilerImageField

class CarouselItem(CarouselItemAbstract):
    image = FilerImageField(blank=True, null=True)
