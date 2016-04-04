import re
from http.http_process import HTTPProcess

__author__ = 'eduardo'


class Alphapd(HTTPProcess):# TODO Remove class not add new information
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^alphapd", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return metadata
        """
        server = self.get_header_field(data, 'server')

        if server:
            if self.re_expr.search(server):
                metadata.service.product = 'Alphapd'

        return metadata
