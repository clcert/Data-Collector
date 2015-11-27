import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class IbmHttpServer(HttpProcess):
    """
    http://www-03.ibm.com/software/products/es/http-servers
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^ibm[\s_]?http[\s_]?server", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        """
        server = data['server']
        if server:
            if self.re_expr.search(server):
                metadata.service.manufacturer = 'IBM'
                metadata.service.product = 'HTTP Server'
        return metadata