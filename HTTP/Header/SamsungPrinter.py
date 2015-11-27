import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class SamsungPrinter(HttpProcess):
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^samsung", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        """
        server = data['server']
        if server:
            if self.re_expr.search(server):
                metadata.device.manufacturer = 'Samsung'
                metadata.device.type = 'Printer'
        return metadata