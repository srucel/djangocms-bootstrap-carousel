# coding: utf-8
import re
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _
from django.contrib import admin
from django.forms import ModelForm, ValidationError

from models import *

class CarouselForm(ModelForm):
    class Meta:
        model = Carousel

    def clean_domid(self):
        data = self.cleaned_data['domid']
        if not re.match(r'^[a-zA-Z_]\w*$', data):
            raise ValidationError(_("The name must be a single word beginning with a letter"))
        return data

class CarouselItemInline(admin.TabularInline):
    model = CarouselItem

class CarouselPlugin(CMSPluginBase):
    model = Carousel
    form = CarouselForm
    name = _("Bootstrap Carousel")
    render_template = "djangocms_bootstrap_carousel/carousel.html"

    inlines = [
        CarouselItemInline,
        ]

    def render(self, context, instance, placeholder):
        context.update({'instance' : instance})
        return context

plugin_pool.register_plugin(CarouselPlugin)
