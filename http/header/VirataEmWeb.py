import re
from http.http_process import HTTPProcess

__author__ = 'eduardo'


class VirataEmWeb(HTTPProcess):
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^virata-emweb/?(?P<version>[\w\.]+)?", re.IGNORECASE)

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
                metadata.service.manufacturer = "Virata"
                metadata.service.product = 'EmWeb'
                metadata.service.version = match_obj.group('version')
                metadata.device.type = 'Embedded'

        return metadata
