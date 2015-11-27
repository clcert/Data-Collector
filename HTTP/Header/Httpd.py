import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class Httpd(HttpProcess):

    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^httpd", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        """
        server = data['server']
        if server:
            if self.re_expr.search(server):
                metadata.service.manufacturer = 'Apache'
                metadata.service.product = 'httpd'
        return metadata