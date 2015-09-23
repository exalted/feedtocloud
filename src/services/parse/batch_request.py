#!/usr/bin/env python
# -*- coding: utf-8 -*-

from request import Request


class BatchRequest(object):
    method = 'POST'
    path   = '/1/batch'

    # Parse allows to create, update, or delete up to 50 objects in one call
    def __init__(self, connection, requests, chunk_size=50):
        assert chunk_size <= 50
        self.connection = connection
        self.requests   = requests
        self.chunk_size = chunk_size

    def execute(self):
        response = list()
        for chunk in BatchRequest.split(self.requests, self.chunk_size):
            result = Request._request(
                self.connection,
                self.method,
                self.path,
                self._body(chunk)
            )
            response.extend(result)
        return response

    def _body(self, requests):
        assert len(requests) <= self.chunk_size
        return { "requests": [BatchRequest._wrap(x) for x in requests] }

    @staticmethod
    def split(l, n):
        for i in xrange(0, len(l), n):
            yield l[i:i + n]

    @staticmethod
    def _wrap(request):
        return {
            "method": request.method,
            "path"  : request.path,
            "body"  : request.body
        }
