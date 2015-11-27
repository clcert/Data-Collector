import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class Interlogix(HttpProcess):
    """
    http://www.interlogix.com/
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^interlogix[\s-]?webs", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        """
        server = data['server']
        if server:
            if self.re_expr.search(server):
                metadata.service.product = 'Interlogix Web'
                metadata.device.manufacturer = 'Interlogix'
                metadata.device.type = 'Camera'
        return metadata