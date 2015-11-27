import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class ReeCam(HttpProcess):
    """
    http://www.reecam.net/en/
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^reecam\s?ip\s?camera", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        """
        server = data['server']
        if server:
            match_obj = self.re_expr.search(server)
            if match_obj:
                metadata.device.manufacturer = 'ReeCam'
                metadata.device.product = 'Ip Camera'
                metadata.device.type = 'Camera'
        return metadata