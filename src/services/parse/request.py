#!/usr/bin/env python
# -*- coding: utf-8 -*-

from parse_object import ParseObject


class Request(object):
    def __init__(self, method, obj=None, **kwargs):
        body = ParseObject.bind(obj) if obj else kwargs['body']
        cls = type(obj) if obj else kwargs['cls']

        self.method = method
        self.path   = '/1/classes/%s' % cls.__name__
        self.body   = body
