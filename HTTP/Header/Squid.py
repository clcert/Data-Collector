import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class Squid(HttpProcess):
    """
    http://www.squid-cache.org/
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^squid/?(?P<version>[\w\.]+)?\s?(\((?P<os>\w*)\))?", re.IGNORECASE)

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
                metadata.service.product = 'Squid'
                metadata.service.version = match_obj.group('version')
                metadata.device.os = match_obj.group('os')
        return metadata