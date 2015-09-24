#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httplib

from batch_request import BatchRequest
from create_request import CreateRequest


class Parse(object):
    _connection = httplib.HTTPSConnection('api.parse.com', 443)

    def save(self, entries):
        new_entries = self._filter(entries)
        request = BatchRequest([CreateRequest(x) for x in new_entries])
        request.execute(self._connection)

    def _filter(self, entries):
        # TODO: missing implementation
        return entries
