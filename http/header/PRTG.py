import re
from http.http_process import HTTPProcess

__author__ = 'eduardo'


class PRTG(HTTPProcess):
    """
    https://www.paessler.com/prtg
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^prtg/?(?P<version>[\d\.]+)?", re.IGNORECASE)

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
                metadata.service.manufacturer = 'PRTG'
                metadata.service.product = 'Network Monitor'
                metadata.service.version = match_obj.group('version')

        return metadata
