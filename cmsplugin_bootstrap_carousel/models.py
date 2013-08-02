from os.path import dirname

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext as _

from cms.models.pluginmodel import CMSPlugin


class Carousel(CMSPlugin):
    domid = models.CharField(max_length=50, verbose_name=_('Name'))
    interval = models.IntegerField(default=5000)
    INDICATOR_CHOICES = (
        (0, 'Default', ),
        (1, 'Thumbnails', ),
    )
    indicator = models.IntegerField(choices=INDICATOR_CHOICES, default=0)

    @property
    def indicator_template(self):
        if 'filer' in settings.INSTALLED_APPS:
            THUMBNAILS_TEMPLATE = 'easy_thumbnails.inc.html'
        else:
            THUMBNAILS_TEMPLATE = 'thumbnails.inc.html'

        INDICATOR_TEMPLATES = {
            0: 'default.inc.html',
            1: THUMBNAILS_TEMPLATE,
        }
        return 'cmsplugin_bootstrap_carousel/inc/indicator_{}'.format(INDICATOR_TEMPLATES[self.indicator])

    def copy_relations(self, oldinstance):
        for item in oldinstance.carouselitem_set.all():
            item.pk = None
            item.carousel = self
            item.save()

    def __unicode__(self):
        return self.domid


if 'filer' in settings.INSTALLED_APPS:
    execfile(dirname(__file__)+"/models_filer.py")
else:
    execfile(dirname(__file__)+"/models_default.py")
