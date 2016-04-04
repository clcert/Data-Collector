import re
from http.http_process import HTTPProcess

__author__ = 'eduardo'


class BlueIris(HTTPProcess):
    """
    http://blueirissoftware.com/
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^blueiris-?http/?([\d\.]+)", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        """
        server = self.get_header_field(data, 'server')

        if server:
            if self.re_expr.search(server):
                metadata.service.manufacturer = 'Blue Iris'
                metadata.service.product = 'Blue Iris Video Security'
                metadata.device.type = 'Camera'

        return metadata
