#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

from app.models.section import SectionError
from app.models.text import Text
from app.models.image import Image
from app.models.list_item import ListItem


class Yeni1Tarif(object):
    def parse(self, raw_content):
        sections = list()

        tags = BeautifulSoup(raw_content, "lxml").body.children
        for tag in tags:
            if tag.name == 'p':
                try:
                    sections.append(Yeni1Tarif.extract_text(tag))
                except SectionError:
                    sections.extend(Yeni1Tarif.extract_images(tag))
            elif tag.name in ['ul', 'ol']:
                sections.extend(Yeni1Tarif.extract_list_items(tag))

        return sections

    @staticmethod
    def extract_text(tag):
        text = tag.get_text(strip=True).encode('utf-8')
        return Text(text)

    @staticmethod
    def extract_images(tag):
        items = list()
        for descendant in tag.descendants:
            if descendant.name == 'img':
                items.append(Image(descendant['src']))
        return items

    @staticmethod
    def extract_list_items(tag):
        items = list()
        for item in tag.stripped_strings:
            items.append(ListItem(item.encode('utf-8')))
        return items
