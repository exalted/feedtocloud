#!/usr/bin/env python
# -*- coding: utf-8 -*-

import models


class Feed(object):
    def __init__(self, url, parser, adapter):
        self.url = url
        self.parser = parser
        self.adapter = adapter

    @property
    def entries(self):
        entries = list()
        for e in self.parser.parse(self.url).entries:
            sections = self.adapter.adapt(e.content[0].value.encode('utf-8'))
            entries.extend([models.Entry(e, sections)])
        return entries
