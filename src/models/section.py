#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Section(object):
    __metaclass__ = ABCMeta

    def __init__(self, type, content):
        self._check_errors(type, content)

    def _check_errors(self, type, content):
        if type not in ['text', 'image', 'list']:
            raise SectionError('Unknown type "%s".' % type)
        if not content:
            raise SectionError('Empty content.')

    @abstractmethod
    def convert(self, converter):
        pass


class SectionError(Exception):
    pass
