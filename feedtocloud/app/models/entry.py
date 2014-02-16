#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import hashlib


class Entry(object):
    def __init__(self, origin, parser):
        self._raw_content = origin.content[0].value.encode('utf-8')
        self._digest = hashlib.md5(self._raw_content).hexdigest()

        self.id = origin.id
        self.title = origin.title.encode('utf-8')
        self.summary = origin.summary
        self.tags = [ x.term.encode('utf-8') for x in origin.tags]
        # 9-valued tuple: ( year, month, day, hour, minute, second, day of week, day of year, dst-flag )
        # (Ref: http://stackoverflow.com/questions/686717/python-convert-9-tuple-utc-date-to-mysql-datetime-format)
        self.date = datetime.datetime(*(origin.published_parsed[:6]))

        self.parser = parser

    @property
    def sections(self):
        return self.parser.parse(self._raw_content)

    @property
    def markdown(self):
        return '# %s\n%s' % (
            self.title,
            '\n'.join([x.markdown for x in self.sections])
        )
