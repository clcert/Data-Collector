import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class Boa(HttpProcess):
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^boa/?(?P<version>[\w\.]+)?", re.IGNORECASE)

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
                metadata.service.product = 'Boa'
                metadata.service.version = match_obj.group('version')
        return metadata