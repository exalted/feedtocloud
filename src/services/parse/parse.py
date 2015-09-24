# -*- coding: utf-8 -*-

import httplib

from batch_request import BatchRequest
from create_request import CreateRequest


class Parse(object):
    _connection = httplib.HTTPSConnection('api.parse.com', 443)

    def save(self, entries):
        new_entries = self._filter_already_saved(entries)
        request = BatchRequest([CreateRequest(x) for x in new_entries])
        request.execute(self._connection)

    # TODO: temporary/quick code
    def _filter_already_saved(self, entries):
        import json
        import urllib
        from os import environ

        params = urllib.urlencode({
            "where": json.dumps({
                "identifier": {"$in": [x.id for x in entries]}
            })
        })
        self._connection.connect()
        self._connection.request('GET', '/1/classes/Entry?%s' % params, '', {
            "X-Parse-Application-Id": environ['PARSE_APPLICATION_ID'],
            "X-Parse-REST-API-Key": environ['PARSE_REST_API_KEY']
        })
        response = json.loads(self._connection.getresponse().read())
        results = response['results']

        already_saved = [x['identifier'] for x in results]
        return [x for x in entries if x.id not in already_saved]
