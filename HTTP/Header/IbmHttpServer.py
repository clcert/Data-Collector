import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class IbmHttpServer(HttpProcess):
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^ibm[\s_]?http[\s_]?server", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        """
        server = HttpProcess.getServer(data)
        if server:
            if self.re_expr.search(server):
                metadata.product = 'IBM HTTP Server'
        return metadata