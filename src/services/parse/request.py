# -*- coding: utf-8 -*-

import json

# TODO: don't read from environment, instead take params
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
        return '%s/%s/%s' % (environ['PARSE_MOUNT'], self.klass, type(self.obj).__name__)

    @property
    def body(self):
        return self.obj.as_dict()

    @staticmethod
    def _request(connection, method, path, body):
        connection.connect()
        connection.request(method, path, json.dumps(body), {
            "Content-Type": "application/json;charset=utf-8",
            "X-Parse-Application-Id": environ['PARSE_APPLICATION_ID'],
            # TODO: don't hardcode this header, instead either types that inherit
            #       from `Request` have to specify, or (maybe even better) clients
            #       can add/override.
            "X-Parse-Master-Key": environ['PARSE_MASTER_KEY']
        })
        return json.loads(connection.getresponse().read())
