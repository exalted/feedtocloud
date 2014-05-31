#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BaseConverter(object):
    def convert(self, entry):
        return '%s\n%s' % (
            self.title(entry.title),
            '\n'.join([x.convert(self) for x in entry.sections])
        )
