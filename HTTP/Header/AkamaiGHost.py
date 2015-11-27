import re
from HTTP.HttpProcess import HttpProcess
from HTTP.Metadata import Metadata

__author__ = 'eduardo'


class AkamaiGHost(HttpProcess):

    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^akamaighost", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        """
        server = data['server']
        if server:
            if self.re_expr.search(server):
                metadata.service.manufacturer = 'Akamai'
                metadata.service.product = 'GHost'
        return metadata