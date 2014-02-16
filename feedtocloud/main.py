#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from app.models.feed import Feed
from app.adapters.yeni1tarif import Yeni1Tarif


def main():
    feed = Feed(os.environ['FEED_URL'], Yeni1Tarif())
    run(feed)

def run(feed):
    for blog_post in feed.entries:
        print(blog_post.markdown)


if __name__ == '__main__':
    sys.exit(main())
