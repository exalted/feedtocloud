#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import environ

from os.path import abspath, dirname, join
sys.path.append(join(abspath(dirname(__file__)), 'src'))
sys.path.append(join(abspath(dirname(__file__)), 'lib', 'vendor'))

from adapters import Yeni1Tarif
from services import Parse

import sources


def main():
    adapter   = Yeni1Tarif()
    cloud     = Parse()

    feed = sources.Feed(environ['SOURCE_URL'], adapter)

    cloud.save(feed.entries)


if __name__ == '__main__':
    sys.exit(main())
