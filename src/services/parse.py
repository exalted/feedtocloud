#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import httplib

from os import environ


class Parse(object):
    def __init__(self):
        self.connection = httplib.HTTPSConnection('api.parse.com', 443)

    def save(self, entries):
        batch = BatchRequest(self.connection, 50)  # 50 is max allowed by Parse
        for e in entries:
            batch.include(Create(e))
        print batch.execute()


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


class Request(object):
    def __init__(self, method, obj=None, **kwargs):
        body = ParseObject.bind(obj) if obj else kwargs['body']
        cls = type(obj) if obj else kwargs['cls']

        self.method = method
        self.path   = '/1/classes/%s' % cls.__name__
        self.body   = body


class Create(Request):
    def __init__(self, obj=None, **kwargs):
        super(Create, self).__init__('POST', obj, **kwargs)


class ParseObject(object):
    @staticmethod
    def bind(entry):
        return {
            'content'           : entry.content,
            'digest'            : entry.digest,
            'identifier'        : entry.id,
            'title'             : entry.title,
            'summary'           : entry.summary,
            'converted_content' : entry.converted_content,
            'tags'              : entry.tags,
            'publishedAt'       : {
                "__type" : "Date",
                "iso"    : entry.published_at.isoformat()
            },
        }
