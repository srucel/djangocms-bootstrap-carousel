# -*- coding: utf-8 -*-

from django.contrib import admin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from django.utils.html import escape
from django.template.response import TemplateResponse
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib import messages
from django.views.decorators.debug import sensitive_post_parameters
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from cmsplugin_bootstrap_carousel.models import *
from cmsplugin_bootstrap_carousel.cms_plugins import CarouselItemInline


"""
It's required to add an admin registration for Link otherwise there will
be no automagical "add" button!
"""

class CarouselAdmin(admin.ModelAdmin):

    inlines = [
        CarouselItemInline,
        ]


admin.site.register(Carousel, CarouselAdmin)

from cms.plugins.link.models import Link
admin.site.register(Link)