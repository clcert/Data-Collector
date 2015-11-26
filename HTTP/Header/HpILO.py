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
        server = HttpProcess.getServer(data)
        if server:
            match_obj = self.re_expr.search(server)
            if match_obj:
                metadata.product = 'HP Integrated Lights Out Server'
                metadata.version = match_obj.group('version')
        return metadata