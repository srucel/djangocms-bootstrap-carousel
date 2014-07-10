from setuptools import setup
import os

setup(
    name='djangocms-bootstrap-carousel',
    packages=['djangocms_bootstrap_carousel',],

    package_data={
        '': [
            'templates/djangocms_bootstrap_carousel/*.html',
            'templates/djangocms_bootstrap_carousel/inc/*.html',
            'models/*.py',
        ]
    },

    version='1.3',
    description='Bootstrap carousel plugin for django-cms',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    author='Antoine Nguyen',
    author_email='tonio@ngyn.org',
    maintainer='Stefano Crosta',
    maintainer_email='stefano@digitalemagine.com',
    url='https://github.com/digitalemagine/djangocms-bootstrap-carousel',
    license='BSD',
    keywords=['django', 'django-cms', 'bootstrap', 'carousel'],
    classifiers=[
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Framework :: Django'
        ],
    include_package_data=True,
    zip_safe=True,
#    install_requires=['Django-CMS>=3.0'],
    )
