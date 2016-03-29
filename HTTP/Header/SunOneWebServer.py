import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class SunOneWebServer(HttpProcess):
    """
    https://docs.oracle.com/cd/E19199-01/817-1831-10/agintro.html
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^sun-one-web-server/?(?P<version>[\d\.]+)?", re.IGNORECASE)

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
                metadata.service.manufacturer = 'Sun'
                metadata.service.product = 'ONE Web Server'
                metadata.service.version = match_obj.group('version')

        return metadata
