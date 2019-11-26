import singer

from tap_kit import TapExecutor
from tap_kit.utils import (transform_write_and_count)

LOGGER = singer.get_logger()


class WalkScoreExecutor(TapExecutor):

    def __init__(self, streams, args, client):
        """
        Args:
            streams (arr[Stream])
            args (dict)
            client (BaseClient)
        """
        super(WalkScoreExecutor, self).__init__(streams, args, client)

        self.url = 'http://api.walkscore.com'
        self.wsapikey = self.client.config['wsapikey']

    def call_full_stream(self, stream):
        """
        Method to call all fully synced streams
        """

        request_config = {
            'url': self.generate_api_url(stream),
            'headers': self.build_headers(),
            'params': None,
            'run': True
        }

        LOGGER.info("Extracting {s} ".format(s=stream))

        self.call_stream(stream, request_config)

    def call_stream(self, stream, request_config):
        for location in self.client.config['locations']:
            request_config['params'] = self.build_params(
                location[0], location[1], location[2])
            res = self.client.make_request(request_config)

            records = res.json()

            if not records:
                records = []
            elif not isinstance(records, list):
                # subsequent methods are expecting a list
                records = [records]

            transform_write_and_count(stream, records)

    def build_params(self, address, lat, lon):
        return {
            "wsapikey": self.wsapikey,
            "transit": 1,
            "bike": 1,
            "format": "json",
            "address": address,
            "lat": lat,
            "lon": lon,
        }

    def build_headers(self):
        """
        Included in all API calls
        """
        return {
            "Accept": "application/json;charset=UTF-8",  # necessary for returning JSON
        }
