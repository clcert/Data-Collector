import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class ZKWebServer(HttpProcess):
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
        server = HttpProcess.getServer(data)
        if server:
            if self.re_expr.search(server):
                metadata.product = 'ZK Web Server'
        return metadata