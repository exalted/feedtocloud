# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

from models import *


class Yeni1Tarif(object):
    def adapt(self, content):
        sections = list()

        tags = BeautifulSoup(content, "lxml").body.children
        for tag in tags:
            if tag.name == 'p':
                try:
                    sections.append(self._extract_text(tag))
                except SectionError:
                    sections.extend(self._extract_images(tag))
            elif tag.name in ['ul', 'ol']:
                sections.extend(self._extract_list_items(tag))

        return sections

    @staticmethod
    def _extract_text(tag):
        text = tag.get_text(strip=True)
        return Text(text)

    @staticmethod
    def _extract_images(tag):
        items = list()
        for descendant in tag.descendants:
            if descendant.name == 'img':
                items.append(Image(descendant['src']))
        return items

    @staticmethod
    def _extract_list_items(tag):
        items = list()
        for item in tag.stripped_strings:
            items.append(ListItem(item))
        return items
