#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import environ as ENV

from os.path import abspath, dirname, join
sys.path.append(join(abspath(dirname(__file__)), 'src'))

import feedparser

from adapters   import Yeni1Tarif
from converters import Markdown, HTML

import models


def main():
    #! TODO: make these configurable
    parser    = feedparser
    adapter   = Yeni1Tarif()
    converter = HTML()

    feed = models.Feed(ENV['FEED_URL'], parser, adapter, converter)
    for e in feed.entries:
        print(e.converted_content)


if __name__ == '__main__':
    sys.exit(main())
