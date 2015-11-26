import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class RouterWebserver(HttpProcess):
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^router webserver", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        """
        server = data['server']
        if server:
            if self.re_expr.search(server):
                metadata.product = 'Router Webserver'
                metadata.device_type = 'Router'
        return metadata
