# -*- coding: utf-8 -*-

import httplib
from os import environ

from batch_request import BatchRequest
from create_request import CreateRequest


class Parse(object):
    _connection = httplib.HTTPSConnection(environ['PARSE_HOST'], 443)

    def save(self, entries):
        new_entries = self._filter_already_saved(entries)
        request = BatchRequest([CreateRequest(x) for x in new_entries])
        request.execute(self._connection)

    # TODO: temporary/quick code
    def _filter_already_saved(self, entries):
        import json
        import urllib

        params = urllib.urlencode({
            "where": json.dumps({
                "identifier": {"$in": [x.id for x in entries]}
            })
        })
        url = '%s/classes/Entry?%s' % (environ['PARSE_MOUNT'], params)

        # why the magic number? https://www.parse.com/questions/rest-get-limit
        if len(url) > 7000:
            raise ValueError('The query is too long')

        self._connection.connect()
        self._connection.request('GET', url, '', {
            "Content-Type": "application/json;charset=utf-8",
            "X-Parse-Application-Id": environ['PARSE_APPLICATION_ID']
        })
        response = json.loads(self._connection.getresponse().read())
        results = response['results']

        already_saved = [x['identifier'] for x in results]
        return [x for x in entries if x.id not in already_saved]
