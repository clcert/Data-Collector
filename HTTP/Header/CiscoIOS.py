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
        server = self.get_header_field(data, 'server')

        if server:
            if self.re_expr.search(server):
                metadata.service.manufacturer = 'Cisco'
                metadata.service.product = 'IOS'
                metadata.device.manufacturer = 'Cisco'
                metadata.device.type = 'Router'

        return metadata
