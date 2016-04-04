import re
from http.http_process import HTTPProcess

__author__ = 'eduardo'


class GlassFish(HTTPProcess):
    """
    https://glassfish.java.net/
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^glassfish server open source edition(\s+)?(?P<version>[\w\.]+)?", re.IGNORECASE)

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
                metadata.service.manufacturer = 'Oracle'
                metadata.service.product = 'GlassFish Server'
                metadata.service.version = match_obj.group('version')

        return metadata
