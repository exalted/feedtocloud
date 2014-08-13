#!/usr/bin/env python
# -*- coding: utf-8 -*-

from parsers import FeedParser
from converters import HTML


class Feed(object):
    def __init__(self, url, adapter, parser=FeedParser(), converter=HTML()):
        self.url       = url
        self.adapter   = adapter
        self.parser    = parser
        self.converter = converter

    @property
    def entries(self):
        return self.parser.parse(self.url, self.adapter, self.converter)
