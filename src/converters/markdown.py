#!/usr/bin/env python
# -*- coding: utf-8 -*-

from converter import Converter


class Markdown(Converter):
    def __init__(self):
        super(Markdown, self).__init__()

    def title(self, text):
        return '# %s\n' % text

    def text(self, text):
        return '%s\n' % text

    def image(self, src):
        return '![Alt text](%s)\n' % src

    def list_item(self, text):
        return '- %s\n' % text
