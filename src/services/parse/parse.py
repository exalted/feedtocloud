#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httplib

from batch_request import BatchRequest
from create_request import CreateRequest


class Parse(object):
    def __init__(self):
        self.connection = httplib.HTTPSConnection('api.parse.com', 443)

    def save(self, entries):
        new_entries = self._filter(entries)
        # TODO: clearly making the actual request should be concern of a
        #       separate object. Below same `self.connection` is passed to both
        #       outer `BatchRequest` and inner `CreateRequest` requests,
        #       although only outer connection is used after all.
        BatchRequest(
            self.connection,
            [CreateRequest(self.connection, x) for x in new_entries]
        ).execute()

    def _filter(self, entries):
        # TODO: missing implementation
        return entries
