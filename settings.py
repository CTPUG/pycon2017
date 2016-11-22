# -*- encoding: utf-8 -*-
import os

from wafer.settings import *

try:
    from localsettings import *
except ImportError:
    pass

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy

pyconzadir = os.path.dirname(__file__)


STATICFILES_DIRS = (
    os.path.join(pyconzadir, 'static'),
)

TEMPLATES[0]['DIRS'] = (
    os.path.join(pyconzadir, 'templates'),
) + TEMPLATES[0]['DIRS']


WAFER_MENUS += (
    {"menu": "about", "label": _("About"),
     "items": []},
    {"name": "venue", "label": _("Venue"),
     "url": reverse_lazy("wafer_page", args=("venue",))},
    {"menu": "sponsors", "label": _("Sponsors"),
     "items": [
         {"name": "sponsors", "label": _("Our sponsors"),
          "url": reverse_lazy("wafer_sponsors")},
         {"name": "packages", "label": _("Sponsorship packages"),
          "url": reverse_lazy("wafer_sponsorship_packages")},
         ]},
    {"menu": "talks", "label": _("Talks"),
     "items": [
         #{"name": "schedule", "label": _("Schedule"),
         # "url": reverse_lazy("wafer_full_schedule")},
         #{"name": "accepted-talks", "label": _("Accepted Talks"),
         # "url": reverse_lazy("wafer_users_talks")},
         #{"name": "speakers", "label": _("Speakers"),
         # "url": reverse_lazy("wafer_talks_speakers")},
        ]},
    {"menu": "news", "label": _("News"),
     "items": []},
    {"menu": "previous-pycons", "label": _("Past PyConZAs"),
     "items": [
         {"name": "pyconza2012", "label": _("PyConZA 2012"),
          "url": "http://2012.za.pycon.org/"},
         {"name": "pyconza2013", "label": _("PyConZA 2013"),
          "url": "http://2013.za.pycon.org/"},
         {"name": "pyconza2014", "label": _("PyConZA 2014"),
          "url": "http://2014.za.pycon.org/"},
         {"name": "pyconza2015", "label": _("PyConZA 2015"),
          "url": "http://2015.za.pycon.org/"},
         {"name": "pyconza2016", "label": _("PyConZA 2016"),
          "url": "http://2016.za.pycon.org/"},
         ]},
    {"name": "twitter", "label": "Twitter",
     "image": "/static/img/twitter.png",
     "url": "https://twitter.com/pyconza"},
    {"name": "googleplus", "label": "Google+",
     "image": "/static/img/googleplus.png",
     "url": "https://plus.google.com/114279924327039493110"},
    {"name": "facebook", "label": "Facebook",
     "image": "/static/img/facebook.png",
     "url": "https://www.facebook.com/pyconza"},
)


CRISPY_TEMPLATE_PACK = 'bootstrap4'
MARKITUP_FILTER = ('markdown.markdown', {
    'safe_mode': False,
    'extensions': [
        'outline',
        'attr_list',
        'attr_cols',
        'markdown.extensions.tables',
    ],
})
# Use HTTPS jquery URL so it's accessible on HTTPS pages (e.g. editing a talk)
JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.0.3/jquery.min.js'

WAFER_TALKS_OPEN = False
