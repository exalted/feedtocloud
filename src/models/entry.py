#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib

from models.image import Image


class Entry(object):
    def __init__(self, **kwargs):
        self._content = None
        self._title   = None
        self._summary = None
        self._tags    = None

        self.content      = kwargs['content']
        self.digest       = hashlib.md5(self.content).hexdigest()

        self.id           = kwargs['id']
        self.title        = kwargs['title']
        self.summary      = kwargs['summary']
        self.tags         = kwargs['tags']
        self.published_at = kwargs['published_at']
        self.sections     = []

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value.encode('utf-8')

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value.encode('utf-8')

    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, value):
        self._summary = value.encode('utf-8')

    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        self._tags = [x.encode('utf-8') for x in value]

    @property
    def preview_image(self):
        for section in self.sections:
            if type(section) is Image:
                return section.src
        return None
