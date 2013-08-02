# coding: utf-8
import os
from django.db import models
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils.translation import ugettext as _

from cms.plugins.link.models import Link
from PIL import Image
from cStringIO import StringIO

DEF_SIZE = (800, 600)

class CarouselItem(models.Model):
    carousel = models.ForeignKey('Carousel')
    caption_title = models.CharField(max_length=100, blank=True, null=True)
    caption_content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="uploads/", blank=True, null=True)
    link = models.ForeignKey(Link, blank=True, null=True)  # use django reverse or link to a page...

    def save(self, *args, **kwargs):
        if self.image:
            # resize image to the BOOTSTRAP_CAROUSEL_IMGSIZE (or DEF_SIZE as a default)
            img = Image.open(self.image.file)
            if img.mode not in ('L', 'RGB'):
                img = img.convert('RGB')
            size = getattr(settings, 'BOOTSTRAP_CAROUSEL_IMGSIZE', DEF_SIZE)
            img.thumbnail(size, Image.ANTIALIAS)

            temp_handle = StringIO()
            img.save(temp_handle, 'png')
            temp_handle.seek(0)

            suf = SimpleUploadedFile(os.path.split(self.image.name)[-1],
                                     temp_handle.read(), content_type='image/png')
            fname = "%s.png" % os.path.splitext(self.image.name)[0]
            self.image.save(fname, suf, save=False)

        super(CarouselItem, self).save()
