#!/usr/bin/env python
# -*- coding: utf-8 -*-

from section import Section

class ListItem(Section):
    def __init__(self, text):
        super(ListItem, self).__init__('list', text)

    @property
    def markdown(self):
        return '- %s' % self.content
