# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Section(object):
    __metaclass__ = ABCMeta

    def __init__(self, _type, content):
        self._check_errors(_type, content)

    @staticmethod
    def _check_errors(_type, content):
        if _type not in ['text', 'image', 'list']:
            raise SectionError('Unknown type "%s".' % _type)
        if not content:
            raise SectionError('Empty content.')

    @abstractmethod
    def convert(self, converter):
        pass


class SectionError(Exception):
    pass
