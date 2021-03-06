import re
from http.http_process import HTTPProcess

__author__ = 'eduardo'


class IbmHTTPServer(HTTPProcess):
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
        server = self.get_header_field(data, 'server')
        if server:
            if self.re_expr.search(server):
                metadata.service.manufacturer = 'IBM'
                metadata.service.product = 'HTTP Server'

        return metadata
