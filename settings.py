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

STATICFILES_STORAGE = (
    'django.contrib.staticfiles.storage.ManifestStaticFilesStorage')

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
         {"name": "Takealot", "label": _(u"» Takealot ★"),
          "url": reverse_lazy("wafer_sponsor", args=(1,))},
         {"name": "Oracle", "label": _(u"» Oracle ☆"),
          "url": reverse_lazy("wafer_sponsor", args=(2,))},
         {"name": "Google", "label": _(u"» Google ☆"),
          "url": reverse_lazy("wafer_sponsor", args=(5,))},
         {"name": "OfferZen", "label": _(u"» OfferZen ○"),
          "url": reverse_lazy("wafer_sponsor", args=(3,))},
         {"name": "PSF", "label": _(u"» PSF ○"),
          "url": reverse_lazy("wafer_sponsor", args=(4,))},
         {"name": "Jumo", "label": _(u"» Jumo ○"),
          "url": reverse_lazy("wafer_sponsor", args=(6,))},
         {"name": "Prodigy Finance", "label": _(u"» Prodigy Finance ○"),
          "url": reverse_lazy("wafer_sponsor", args=(7,))},
         {"name": "Prodigy Finance", "label": _(u"» Citiq Prepaid"),
          "url": reverse_lazy("wafer_sponsor", args=(8,))},
         {"name": "sponsors", "label": _("Our sponsors"),
          "url": reverse_lazy("wafer_sponsors")},
         {"name": "packages", "label": _("Sponsorship packages"),
          "url": reverse_lazy("wafer_sponsorship_packages")},
         ]},
    {"menu": "talks", "label": _("Talks"),
     "items": [
         {"name": "schedule", "label": _("Schedule"),
          "url": reverse_lazy("wafer_full_schedule")},
         {"name": "accepted-talks", "label": _("Accepted Talks"),
          "url": reverse_lazy("wafer_users_talks")},
         {"name": "speakers", "label": _("Speakers"),
          "url": reverse_lazy("wafer_talks_speakers")},
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


def ticket_count(exclude=None, include=None):
    """ Return a count of tickets. """
    from wafer.tickets.models import Ticket
    query = Ticket.objects
    if exclude:
        query = query.exclude(type_id__in=exclude)
    if include:
        query = query.filter(type_id__in=include)
    return query.count()


def tickets_sold():
    """ Return number of tickets sold. """
    from wafer.tickets.models import Ticket
    return Ticket.objects.count()


def main_conference_tickets_sold():
    """ Return number of tickets sold for the main conference. """
    TUTORIAL_TICKET_TYPES = [10, 11, 12, 14]
    return ticket_count(exclude=TUTORIAL_TICKET_TYPES)


def web_scrape_tut_sold():
    """ Return number of tickets sold for "Web Scraping: Unleash your Internet
        Viking".
    """
    return ticket_count(include=[11])


def ansible_tut_sold():
    """ Return number of tickets sold for "Ansible Essentials". """
    return ticket_count(include=[12])


def elasticsearch_tut_sold():
    """ Return number of tickets sold for "Don't be afraid to search". """
    return ticket_count(include=[14])


def tutorial_lunch_sold():
    """ Return number of tickets sold for tutorial lunch. """
    return ticket_count(include=[10])


CRISPY_TEMPLATE_PACK = 'bootstrap4'
MARKITUP_FILTER = ('markdown.markdown', {
    'safe_mode': False,
    'extensions': [
        'outline',
        'attr_list',
        'attr_cols',
        'markdown.extensions.tables',
        'variables',
    ],
    'extension_configs': {
        'variables': {
            'vars': {
                'tickets_sold': tickets_sold,
                'main_conference_tickets_sold': main_conference_tickets_sold,
                'web_scrape_tut_sold': web_scrape_tut_sold,
                'ansible_tut_sold': ansible_tut_sold,
                'elasticsearch_tut_sold': elasticsearch_tut_sold,
                'tutorial_lunch_sold': tutorial_lunch_sold,
            },
        },
    },
})
# Use HTTPS jquery URL so it's accessible on HTTPS pages (e.g. editing a talk)
JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.0.3/jquery.min.js'

WAFER_TALKS_OPEN = True
