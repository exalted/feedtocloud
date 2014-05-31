#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import environ as ENV

from os.path import abspath, dirname, join
sys.path.append(join(abspath(dirname(__file__)), 'src'))

import feedparser

from adapters   import Yeni1Tarif
from converters import Markdown

import models


def main():
    #! TODO: make these configurable
    parser    = feedparser
    adapter   = Yeni1Tarif()
    converter = Markdown()

    feed = models.Feed(ENV['FEED_URL'], parser, adapter)
    entries = feed.entries

    #! TODO: do something more interesting
    # print(entries)
    for e in entries:
        print(converter.convert(e))
        print('-'*50)


if __name__ == '__main__':
    sys.exit(main())
