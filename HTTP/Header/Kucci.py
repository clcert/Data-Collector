import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class Kucci(HttpProcess):# Todo remove don't add new information
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^kucci", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        """
        server = data['server']
        if server:
            if self.re_expr.search(server):
                metadata.service.product = 'Kucci'
        return metadata