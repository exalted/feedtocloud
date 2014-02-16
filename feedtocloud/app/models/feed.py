#!/usr/bin/env python
# -*- coding: utf-8 -*-

import feedparser

from entry import *


class Feed(object):
    def __init__(self, feed, parser):
        self.feed = feed
        self.parser = parser

    @property
    def entries(self):
        parsed = feedparser.parse(self.feed).entries
        return [Entry(x, self.parser) for x in parsed]
