import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class Gemtek(HttpProcess):
    """
     http://www.gemtek.com.tw
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^gemtek/?(?P<version>[\d\.]+)?", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        """
        server = data['server']
        if server:
            match_obj = self.re_expr.search(server)
            if match_obj:
                metadata.product = 'Gemtek'
                metadata.version = match_obj.group('version')
        return metadata