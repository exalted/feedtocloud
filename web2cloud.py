#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from os.path import abspath, dirname, join
sys.path.append(join(abspath(dirname(__file__)), 'src'))

from adapters   import Yeni1Tarif
from converters import Markdown, HTML

import sources


def main():
    adapter   = Yeni1Tarif()
    converter = HTML()

    from os import environ as ENV
    feed = sources.Feed(ENV['SOURCE_URL'], adapter)
    for e in feed.entries:
        print(converter.convert(e))


if __name__ == '__main__':
    sys.exit(main())
