import re
from http.http_process import HTTPProcess

__author__ = 'eduardo'


class Squid(HTTPProcess):
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
        server = self.get_header_field(data, 'server')

        if server:
            match_obj = self.re_expr.search(server)

            if match_obj:
                metadata.service.product = 'Squid'
                metadata.service.version = match_obj.group('version')
                metadata.device.os = match_obj.group('os')

        return metadata
