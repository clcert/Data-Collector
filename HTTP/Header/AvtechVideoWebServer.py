import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class AvtechVideoWebServer(HttpProcess):
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^av-tech av787 video web server", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        """
        server = self.get_header_field(data, 'server')

        if server:
            if self.re_expr.search(server):
                metadata.service.manufacturer = 'Avtech'
                metadata.service.product = 'Video Web Server'
                metadata.device.type = 'Camera'

        return metadata
