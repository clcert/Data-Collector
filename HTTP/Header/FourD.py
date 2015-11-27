import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class FourD(HttpProcess):
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^(?P<product>4d_v\d+)/?(?P<version>[\d\.]+)?", re.IGNORECASE)

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
                metadata.service.manufacturer = '4D'
                metadata.service.product = match_obj.group('product')
                metadata.service.version = match_obj.group('version')
        return metadata