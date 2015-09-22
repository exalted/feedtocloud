#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

# TODO: don't read from ENV, instead ask params in constructor
from os import environ


# TODO: maybe inherit from `Request`, because `_request` method is pretty much
#       duplicate in both implementations.
class BatchRequest(object):
    def __init__(self, connection, size):
        self.connection = connection
        self.size       = size
        self.requests   = list()

    def include(self, request):
        self.requests.append(request)

    def execute(self):
        self.connection.connect()
        response = list()
        for chunk in BatchRequest.split(self.requests, self.size):
            # TODO: hardcoded request method `POST` ain't cool.
            result = self._request('POST', '/1/batch', {
                "requests": [request.__dict__ for request in chunk]
            })
            response.extend(result)
        return response

    @staticmethod
    def split(l, n):
        for i in xrange(0, len(l), n):
            yield l[i:i + n]

    def _request(self, method, path, requests):
        self.connection.request(method, path, json.dumps(requests), {
            "X-Parse-Application-Id" : environ['PARSE_APPLICATION_ID'],
            "X-Parse-REST-API-Key"   : environ['PARSE_REST_API_KEY'],
            "Content-Type"           : "application/json"
        })
        return json.loads(self.connection.getresponse().read())
