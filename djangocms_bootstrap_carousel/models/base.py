from os.path import dirname

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext as _

from cms.models.pluginmodel import CMSPlugin

from djangocms_link.models import Link

DEF_SIZE = (800, 600)

class Carousel(CMSPlugin):
    domid = models.CharField(max_length=50, verbose_name=_('name'))
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
        # @TODO any way to make the template folder less static?
        # I don't think so... Maybe iwth django 1.7?
        return 'djangocms_bootstrap_carousel/inc/indicator_{}'.format(INDICATOR_TEMPLATES[self.indicator])

    def copy_relations(self, oldinstance):
        for item in oldinstance.carouselitem_set.all():
            item.pk = None
            item.carousel = self
            item.save()

    def __unicode__(self):
        return self.domid

    def save(self, *args, **kwargs):
        print 'save carousel'
        super(Carousel, self).save(*args, **kwargs)

    class Meta:
        app_label = 'djangocms_bootstrap_carousel'


class CarouselItemAbstract(models.Model):

    """
    Issue. we link to the Link model plugin, but we can't add a "copy_relations"
    method to it of course, so we get a warning all the time...
    Any way to avoid it?
    """
    carousel = models.ForeignKey(Carousel)
    caption_title = models.CharField(max_length=100, blank=True, null=True)
    caption_content = models.TextField(blank=True, null=True)
    link = models.ForeignKey(Link, blank=True, null=True)  # use django reverse or link to a page...

    def save(self, *args, **kwargs):
        print 'save carousel item', self.carousel
        super(CarouselItemAbstract, self).save(*args, **kwargs)

    class Meta:
        abstract = True
        app_label = 'djangocms_bootstrap_carousel'