import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class LiteSpeed(HttpProcess):
    """
    https://www.litespeedtech.com/
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^litespeed", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        """
        server = self.get_header_field(data, 'server')

        if server:
            if self.re_expr.search(server):
                metadata.service.manufacturer = 'LiteSpeed Technologies'
                metadata.service.product = 'LiteSpeed'

        return metadata
