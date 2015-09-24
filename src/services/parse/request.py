#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

# TODO: don't read from ENV, instead take params
from os import environ


class Request(object):
    def __init__(self, method, klass, obj):
        self.method = method
        self.klass = klass
        self.obj = obj

    def execute(self, connection):
        return Request._request(
            connection,
            self.method,
            self.path,
            self.body
        )

    @property
    def path(self):
        return '/1/%s/%s' % (self.klass, type(self.obj).__name__)

    @property
    def body(self):
        return self.obj.as_dict()

    @staticmethod
    def _request(connection, method, path, body):
        connection.connect()
        connection.request(method, path, json.dumps(body), {
            "X-Parse-Application-Id": environ['PARSE_APPLICATION_ID'],
            "X-Parse-REST-API-Key": environ['PARSE_REST_API_KEY'],
            "Content-Type": "application/json"
        })
        return json.loads(connection.getresponse().read())
