import re
from http.http_process import HTTPProcess

__author__ = 'eduardo'


class CrossWebServer(HTTPProcess):#TODO Revisar

    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^cross web server", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        """
        server = self.get_header_field(data, 'server')

        if server:
            if self.re_expr.search(server):
                metadata.service.product = 'Cross Web Server'

        return metadata
