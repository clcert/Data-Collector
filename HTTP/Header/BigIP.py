import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class BigIP(HttpProcess):

    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^bigip", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        """
        server = self.get_header_field(data, 'server')

        if server:
            if self.re_expr.search(server):
                metadata.service.manufacturer = 'F5'
                metadata.service.product = 'BigIP'

        return metadata
