import re
from http.http_process import HTTPProcess

__author__ = 'eduardo'


class SonicWall(HTTPProcess):
    """
    www.sonicwall.com/
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^sonicwall", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        """
        server = self.get_header_field(data, 'server')

        if server:
            if self.re_expr.search(server):
                metadata.service.manufacturer = 'Dell'
                metadata.service.product = 'SonicWall'
                metadata.device.type = 'Firewall'

        return metadata
