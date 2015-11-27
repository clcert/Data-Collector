import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class HPILO(HttpProcess):
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^hp[\s-]?ilo[\s-]?server/?(?P<version>[\d\.]+)?", re.IGNORECASE)

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
                metadata.service.manufacturer = 'HP'
                metadata.service.product = 'HP Integrated Lights Out Server'
                metadata.service.version = match_obj.group('version')
                metadata.device.manufacturer = 'HP'
        return metadata