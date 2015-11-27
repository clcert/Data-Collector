import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class Switch(HttpProcess):

    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^switch", re.IGNORECASE)# TODO remove don't add new infoemation

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        """
        server = data['server']
        if server:
            if self.re_expr.search(server):
                metadata.service.product = 'Switch'
        return metadata