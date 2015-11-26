import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class CiscoIOS(HttpProcess):
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^cisco-IOS", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        """
        server = data['server']
        if server:
            if self.re_expr.search(server):
                metadata.product = 'Cisco IOS'
                metadata.device_type = 'Router'
        return metadata