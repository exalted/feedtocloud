#!/usr/bin/env python
# -*- coding: utf-8 -*-

from parsers import FeedParser


class Feed(object):
    def __init__(self, url, adapter, parser=FeedParser()):
        self.url     = url
        self.adapter = adapter
        self.parser  = parser

    @property
    def entries(self):
        return self.parser.parse(self.url, self.adapter)
