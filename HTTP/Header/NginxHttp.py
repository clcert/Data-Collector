import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class Nginx(HttpProcess):
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^nginx/?(?P<version>[\d\.]+)?\s?(\((?P<os>\w*)\))?", re.IGNORECASE)

    def process(self, data, metadata): # TODO Check the admin field
        """
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        """
        server = data['server']
        if server:
            match_obj = self.re_expr.search(server)
            if match_obj:
                metadata.product = 'Nginx'
                metadata.version = match_obj.group('version')
                metadata.os = match_obj.group('os')
        return metadata