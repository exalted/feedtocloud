#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import hashlib


class Entry(object):
    def __init__(self, entry, sections):
        self._raw_content = entry.content[0].value.encode('utf-8')

        self.digest = hashlib.md5(self._raw_content).hexdigest()

        self.id = entry.id
        self.title = entry.title.encode('utf-8')
        self.summary = entry.summary
        self.tags = [ x.term.encode('utf-8') for x in entry.tags]
        # 9-valued tuple: ( year, month, day, hour, minute, second, day of week, day of year, dst-flag )
        # (Ref: http://stackoverflow.com/questions/686717/python-convert-9-tuple-utc-date-to-mysql-datetime-format)
        self.date = datetime.datetime(*(entry.published_parsed[:6]))

        self.sections = sections
