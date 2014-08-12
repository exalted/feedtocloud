#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from os.path import abspath, dirname, join
sys.path.append(join(abspath(dirname(__file__)), 'src'))

from adapters   import Yeni1Tarif
from converters import HTML
from services   import Parse

import sources


def main():
    adapter   = Yeni1Tarif()
    converter = HTML()
    cloud     = Parse()

    from os import environ
    feed = sources.Feed(environ['SOURCE_URL'], adapter)
    for e in feed.entries:
        print(converter.convert(e))

    cloud.save(feed.entries)


if __name__ == '__main__':
    sys.exit(main())
