import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class IPCameraWebServer(HttpProcess):
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^webserver\((ipcamera)(_logo)?\)", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        """
        server = self.get_header_field(data, 'server')

        if server:
            if self.re_expr.search(server):
                # metadata.service.product = 'Web Server'
                metadata.device.type = 'Camera'

        return metadata
