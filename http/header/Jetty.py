import re
from http.http_process import HTTPProcess

__author__ = 'eduardo'


class Jetty(HTTPProcess):
    """
    http://www.eclipse.org/jetty/
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^jetty/?(?P<version>(\([\d\.v]+\))|([\d\.v]+))", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        """
        server = self.get_header_field(data, 'server')

        if server:
            match_obj = self.re_expr.search(server)

            if match_obj:
                metadata.service.manufacturer = 'Eclipse'
                metadata.service.product = 'Jetty'
                metadata.service.version = match_obj.group('version')

        return metadata
