import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class GlassFish(HttpProcess):
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
        server = data['server']
        if server:
            match_obj = self.re_expr.search(server)
            if match_obj:
                metadata.product = 'GlassFish Server'
                metadata.version = match_obj.group('version')
        return metadata
