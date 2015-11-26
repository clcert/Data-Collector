import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class CrossWebServer(HttpProcess):

    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^cross web server", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        """
        server = data['server']
        if server:
            if self.re_expr.search(server):
                metadata.product = 'Cross Web Server'
        return metadata