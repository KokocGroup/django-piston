# coding=utf-8
from __future__ import absolute_import

from django.apps import AppConfig


class PistonConfig(AppConfig):

    name = 'piston'
    verbose_name = u'Piston'

    def ready(self):
        import piston.signals
