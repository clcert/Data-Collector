import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class Com3(HttpProcess):
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^3com/?(?P<version>[\w\.]+)?", re.IGNORECASE)

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
                metadata.product = '3Com'
                metadata.version = match_obj.group('version')
                metadata.device_type = 'Router'
        return metadata