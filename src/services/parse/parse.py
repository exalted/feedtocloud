#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httplib

from batch_request import BatchRequest
from create_request import CreateRequest


class Parse(object):
    def __init__(self):
        self.connection = httplib.HTTPSConnection('api.parse.com', 443)

    def save(self, entries):
        batch = BatchRequest(self.connection, 50)  # 50 is max allowed by Parse
        for e in entries:
            batch.include(CreateRequest(e))
        batch.execute()
