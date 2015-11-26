import re
from HTTP.HttpProcess import HttpProcess

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
        server = HttpProcess.getServer(data)
        if server:
            if self.re_expr.search(server):
                metadata.product = 'AkamaiGHost'
        return metadata
