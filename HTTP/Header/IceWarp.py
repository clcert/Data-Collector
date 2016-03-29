import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class IceWarp(HttpProcess):
    """
    https://www.icewarp.com/
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^icewarp/?(?P<version>[\d\.]+)?", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        """
        server = self.get_header_field(data, 'server')

        if server:
            match_obj = self.re_expr.search(server)

            if match_obj:
                metadata.service.manufacturer = 'IceWarp'
                metadata.service.product = 'Business Mail Server'
                metadata.service.version = match_obj.group('version')

        return metadata