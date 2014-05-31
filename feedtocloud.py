#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from os.path import abspath, dirname, join
sys.path.append(join(abspath(dirname(__file__)), 'src'))

from os import environ as ENV


from models.feed import Feed
from adapters.yeni1tarif import Yeni1Tarif


def main():
    feed = Feed(ENV['FEED_URL'], Yeni1Tarif())
    run(feed)

def run(feed):
    for blog_post in feed.entries:
        print(blog_post.markdown)


if __name__ == '__main__':
    sys.exit(main())
