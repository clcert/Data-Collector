import re
from http.http_process import HTTPProcess

__author__ = 'eduardo'


class Thttpd(HTTPProcess):
    """
    http://acme.com/software/thttpd/
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^thttpd/?(?P<version>[\w\.]+)?", re.IGNORECASE)

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
                metadata.service.manufacturer = 'ACME'
                metadata.service.product = 'thttpd'
                metadata.service.version = match_obj.group('version')

        return metadata
