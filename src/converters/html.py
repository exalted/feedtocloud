#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base_converter import BaseConverter


class HTML(BaseConverter):
    def title(self, text):
        return '<h1>%s</h1>' % text

    def text(self, text):
        return '<p>%s</p>' % text

    def image(self, src):
        return '<img src="%s" alt="Alt Text">' % src

    def list_item(self, text):
        return '<li>%s</li>' % text
