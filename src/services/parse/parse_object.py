#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: this doesn't belong here, rename to sth like `Entry(Object)`
#       and move it away.
class ParseObject(object):
    @staticmethod
    def bind(entry):
        return {
            'content'          : entry.content,
            'digest'           : entry.digest,
            'identifier'       : entry.id,
            'title'            : entry.title,
            'summary'          : entry.summary,
            'convertedContent' : entry.converted_content,
            'previewUrl'       : entry.preview_url,
            'tags'             : entry.tags,
            'publishedAt'      : {
                "__type" : "Date",
                "iso"    : entry.published_at.isoformat()
            },
        }
