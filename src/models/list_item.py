# -*- coding: utf-8 -*-

from section import Section


class ListItem(Section):
    def __init__(self, text):
        super(ListItem, self).__init__('list', text)
        self.text = text

    def convert(self, converter):
        return converter.list_item(self.text)
