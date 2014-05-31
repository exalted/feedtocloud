#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Section(object):
    def __init__(self, type, content):
        self.type = type
        self.content = content

        self._check_errors()

    def _check_errors(self):
        if self.type not in ['text', 'image', 'list']:
            raise SectionError('Unknown type "%s".' % type)
        if not self.content:
            raise SectionError('Empty content.')


class SectionError(Exception):
    pass
