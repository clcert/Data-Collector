import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class SunGlassFish(HttpProcess):
    """
    https://en.wikipedia.org/wiki/GlassFish
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^sun glassfish enterprise server\s?v?(?P<version>[\d\.]+)?", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        """
        server = data['server']
        if server:
            match_obj = self.re_expr.search(server)
            if match_obj:
                metadata.service.manufacturer = 'Oracle'
                metadata.service.product = 'GlassFish Server'
                metadata.service.version = match_obj.group('version')
        return metadata