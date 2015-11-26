import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class AltavozWeb(HttpProcess):
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^altavoz\s?web(\sServer)?", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        """
        server = data['server']
        if server:
            if self.re_expr.search(server):
                metadata.product = 'Altavoz Web Server'
        return metadata