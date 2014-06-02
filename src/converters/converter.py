#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Converter(object):
    __metaclass__ = ABCMeta

    def convert(self, entry):
        return '%s\n%s' % (
            self.title(entry.title),
            '\n'.join([x.convert(self).encode('utf-8') for x in entry.sections])
        )

    @abstractmethod
    def title(self, text):
        pass

    @abstractmethod
    def text(self, text):
        pass

    @abstractmethod
    def image(self, src):
        pass

    @abstractmethod
    def list_item(self, text):
        pass
