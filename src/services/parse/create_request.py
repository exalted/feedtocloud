#!/usr/bin/env python
# -*- coding: utf-8 -*-

from request import Request


class CreateRequest(Request):
    def __init__(self, obj=None, **kwargs):
        super(CreateRequest, self).__init__('POST', obj, **kwargs)
