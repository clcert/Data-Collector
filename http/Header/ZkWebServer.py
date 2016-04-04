import re
from http.http_process import HTTPProcess

__author__ = 'eduardo'


class ZKWebServer(HTTPProcess):
    """
    https://en.wikipedia.org/wiki/ZK_%28framework%29
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^ZK Web(\sServer)?", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        """
        server = self.get_header_field(data, 'server')

        if server:
            if self.re_expr.search(server):
                metadata.service.product = 'ZK Web Server'

        return metadata
