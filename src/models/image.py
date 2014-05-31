#!/usr/bin/env python
# -*- coding: utf-8 -*-

from section import Section


class Image(Section):
    def __init__(self, src):
        super(Image, self).__init__('image', src)
        self.src = src

    def convert(self, converter):
        return converter.image(self.src)
