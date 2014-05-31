#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Section(object):
    def __init__(self, type, content):
        self._check_errors(type, content)

    def _check_errors(self, type, content):
        if type not in ['text', 'image', 'list']:
            raise SectionError('Unknown type "%s".' % type)
        if not content:
            raise SectionError('Empty content.')


class SectionError(Exception):
    pass
