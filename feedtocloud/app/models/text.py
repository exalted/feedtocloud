#!/usr/bin/env python
# -*- coding: utf-8 -*-

from section import Section

class Text(Section):
    def __init__(self, text):
        super(Text, self).__init__('text', text)

    @property
    def markdown(self):
        return self.content
