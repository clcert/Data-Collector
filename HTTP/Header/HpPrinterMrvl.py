import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class HpPrinterMrvl(HttpProcess):
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^mrvl-R\d_\d", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        """
        server = data['server']
        if server:
            if self.re_expr.search(server):
                metadata.device.manufacturer = 'HP'
                metadata.device.type = 'Printer'
        return metadata