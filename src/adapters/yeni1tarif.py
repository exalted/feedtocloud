#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

from models import *


class Yeni1Tarif(object):
    def adapt(self, raw_content):
        sections = list()

        tags = BeautifulSoup(raw_content, "lxml").body.children
        for tag in tags:
            if tag.name == 'p':
                try:
                    sections.append(self._extract_text(tag))
                except SectionError:
                    sections.extend(self._extract_images(tag))
            elif tag.name in ['ul', 'ol']:
                sections.extend(self._extract_list_items(tag))

        return sections

    def _extract_text(self, tag):
        text = tag.get_text(strip=True).encode('utf-8')
        return Text(text)

    def _extract_images(self, tag):
        items = list()
        for descendant in tag.descendants:
            if descendant.name == 'img':
                items.append(Image(descendant['src']))
        return items

    def _extract_list_items(self, tag):
        items = list()
        for item in tag.stripped_strings:
            items.append(ListItem(item.encode('utf-8')))
        return items
