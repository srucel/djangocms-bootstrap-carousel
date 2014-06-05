========================================
Bootstrap carousel plugin for Django CMS
========================================

This plugin lets you easily add *carousel* components (ie. slideshows) into
django-cms pages using `Bootstrap <http://twitter.github.com/bootstrap/>`_.

Forked from https://github.com/xmedia-systems/cmsplugin-bootstrap-carousel/
which is itself a fork of:
https://bitbucket.org/tonioo/cmsplugin-bootstrap-carousel

Requirements
============

* `Django CMS >= 2.2 <http://django-cms.org>`_
* `Bootstrap <http://twitter.github.com/bootstrap/>`_ only tested with v2.*

Works with Django CMS 3.*

Installation
============

To use it into your project, just follow this procedure:

#. Open the *settings.py* file and add ``cmsplugin_bootstrap_carousel`` to the
   ``INSTALLED_APPS`` variable

#. Run the following command::

    $ ./manage.py syncdb


It will adapt to your best-installed file manager - if there is django-filer,
it will use it.

If you are NOT using the djangocms filer plugin:
------------------------------------------------

Images embedded into carousels are automaticaly resized. The default
size is 800x600. To change it, define the following variable into your
configuration file::

  BOOTSTRAP_CAROUSEL_IMGSIZE = (1024, 768)

If you ARE using the djangocms filer plugin:
--------------------------------------------

DOC TO BE COMPLETED

.. note::

    Bootstrap is not included with this plugin.

Usage
=====

Just select "Carousel" as a pluging for a placeholder

Links
-----
To be able to redirect the user to a particular page by clicking on a
slider Image, each image as a ForeignKey to a djangocms-link Link model

Indicators
----------

You can choose to have default bootstrap indicators (the circles) or thumbnails.
Currently Thumbnails work will if you are using the filer plugin, not so well
otherwise.

You can force a width/height from the carousel admin config;
those sizes are then set as a `style` attribute on the main carousel element -
this allows adjusting without modifying the CSS


Versions
========

1.2
---

Width and Height can be forced from the carousel config.


1.0
---

Some code cleanup

0.9
---

 * Added links from each carousel slide
 * Added a thumbnail mode for the indicators (works well with filer, unfinished without)

0.1
---
Original github version