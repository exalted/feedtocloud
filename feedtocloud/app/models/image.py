#!/usr/bin/env python
# -*- coding: utf-8 -*-

from section import Section


class Image(Section):
    def __init__(self, src):
        super(Image, self).__init__('image', src)

    @property
    def markdown(self):
        return '![Alt text](%s)' % self.content
