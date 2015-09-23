#!/usr/bin/env python
# -*- coding: utf-8 -*-

from request import Request


class CreateRequest(Request):
    method = 'POST'

    def __init__(self, connection, obj):
        # TODO: hardcoded `classes` (i.e., objects) request class.
        #       Parse supports also `users`, `files`, `events`, etc.
        super(CreateRequest, self).__init__(
            connection,
            self.method,
            'classes',
            obj
        )
