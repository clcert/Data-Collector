import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class NetwaveIPCamera(HttpProcess):

    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^netwave ip camera", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        """
        server = data['server']
        if server:
            if self.re_expr.search(server):
                metadata.product = 'Netwave IP Camera'
                metadata.device_type = 'Camera'
        return metadata