#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from os.path import abspath, dirname, join
sys.path.append(join(abspath(dirname(__file__)), 'src'))

from os import environ as ENV


from models import Feed
from adapters import Yeni1Tarif
from converters import Markdown


def main():
    #! TODO: make these configurable
    adapter = Yeni1Tarif()
    converter = Markdown()

    feed = Feed(ENV['FEED_URL'], adapter)
    formatted = feed.convert(converter)

    #! TODO: do something more interesting
    print(formatted)


if __name__ == '__main__':
    sys.exit(main())
