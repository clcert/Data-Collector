import re
from http.http_process import HTTPProcess

__author__ = 'eduardo'


class CameraWebServer(HTTPProcess):
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^camera web server", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        """
        server = self.get_header_field(data, 'server')

        if server:
            if self.re_expr.search(server):
                metadata.service.product = 'Camera Web Server'
                metadata.device.type = 'Camera'

        return metadata
