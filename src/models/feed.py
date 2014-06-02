#!/usr/bin/env python
# -*- coding: utf-8 -*-

import models


class Feed(object):
    def __init__(self, url, parser, adapter, converter):
        self.url       = url
        self.parser    = parser
        self.adapter   = adapter
        self.converter = converter

    @property
    def entries(self):
        entries = list()
        for e in self.parser.parse(self.url).entries:
            entry = models.Entry(e, self.adapter)
            entry = self.converter.convert(entry)
            entries.append(entry)
        return entries
