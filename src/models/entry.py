#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import hashlib


class Entry(object):
    def __init__(self, origin, adapter):
        self.raw_content = origin.content[0].value.encode('utf-8')
        self.converted_content = None

        self.digest = hashlib.md5(self.raw_content).hexdigest()
        self.id = origin.id
        self.title = origin.title.encode('utf-8')
        self.summary = origin.summary
        self.tags = [ x.term.encode('utf-8') for x in origin.tags]
        # 9-valued tuple: ( year, month, day, hour, minute, second, day of week, day of year, dst-flag )
        # (Ref: http://stackoverflow.com/questions/686717/python-convert-9-tuple-utc-date-to-mysql-datetime-format)
        self.date = datetime.datetime(*(origin.published_parsed[:6]))
        self.sections = adapter.adapt(self.raw_content)
