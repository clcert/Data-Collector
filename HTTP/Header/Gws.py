import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class Gws(HttpProcess):

    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^gws", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        """
        server = data['server']
        if server:
            if self.re_expr.search(server):
                metadata.service.manufacturer = 'Google'
                metadata.service.product = 'Web Server'
        return metadata