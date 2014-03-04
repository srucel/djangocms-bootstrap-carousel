# -*- coding: utf-8 -*-

__author__="scrosta"
__date__ ="$2013 Feb 22 18:08:52$"

from django.conf import settings

from base import Carousel

if 'filer' in settings.INSTALLED_APPS:
    from models_filer import CarouselItem
else:
    from models_default import CarouselItem


__all__ = [
    # IPR
    'Carousel', 'CarouselItem',
]
