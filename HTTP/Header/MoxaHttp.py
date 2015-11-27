import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class MoxaHttp(HttpProcess):
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^moxahttp/?(?P<version>[\d\.]+)?", re.IGNORECASE)

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
                metadata.service.manufacturer = 'Moxa'
                metadata.service.product = 'Http'
                metadata.service.version = match_obj.group('version')
        return metadata