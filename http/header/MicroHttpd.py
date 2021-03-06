import re
from http.http_process import HTTPProcess

__author__ = 'eduardo'


class MicroHttpd(HTTPProcess):
    """
    http://acme.com/software/micro_httpd/
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^micro_httpd", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        """
        server = self.get_header_field(data, 'server')
        if server:
            if self.re_expr.search(server):
                metadata.service.manufacturer = 'ACME'
                metadata.service.product = 'Micro Httpd'

        return metadata
