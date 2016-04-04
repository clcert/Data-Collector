import re
from http.http_process import HTTPProcess

__author__ = 'eduardo'


class Com3(HTTPProcess):
    """
    https://es.wikipedia.org/wiki/3Com
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^3com/?(?P<version>[\w\.]+)?", re.IGNORECASE)

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
                metadata.device.manufacturer = '3Com'
                metadata.device.type = 'Router'

        return metadata
