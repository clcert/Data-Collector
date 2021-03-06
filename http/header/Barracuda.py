import re
from http.http_process import HTTPProcess

__author__ = 'eduardo'


class Barracuda(HTTPProcess):
    """
    https://barracudaserver.com/
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^barracudaserver(\.com)?\s?(\((?P<os>\w*)\))?", re.IGNORECASE)

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
                metadata.service.manufacturer = 'Barracuda'
                metadata.service.product = 'Web Server'
                metadata.device.os = match_obj.group('os')

        return metadata
