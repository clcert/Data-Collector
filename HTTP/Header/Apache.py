import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class Apache(HttpProcess):
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^apache/?(?P<version>[\d\.]+)?\s?(\((?P<os>\w*)\))?", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        """
        server = HttpProcess.getServer(data)
        if server:
            match_obj = self.re_expr.search(server)
            if match_obj:
                metadata.product = 'Apache'
                metadata.version = match_obj.group('version')
                metadata.os = match_obj.group('os')
        return metadata