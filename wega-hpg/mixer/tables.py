import decimal

from django.template.loader import render_to_string
from django.utils.html import format_html
import django_tables2 as tables
from django.utils.safestring import mark_safe
from django_tables2 import TemplateColumn

from calc.models import PlantProfile
from wagtail.images.models import Image, Rendition

from mixer.models import Mixer, MixerHistory


class MixerTable(tables.Table):
    class Meta:
        model = Mixer
        template_name = 'django_tables2/bootstrap4.html'
        fields = ['id', 'name', 'status','token']

class MixerHistoryTable(tables.Table):
    class Meta:
        model = MixerHistory
        template_name = 'django_tables2/bootstrap4.html'
        fields = ['id', 'date', ]

class MixerHistorySumTable(tables.Table):
    class Meta:
        model = MixerHistory
        template_name = 'django_tables2/bootstrap4.html'
        fields = []