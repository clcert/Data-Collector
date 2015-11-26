import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class Debut(HttpProcess):
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^debut/?(?P<version>[\d\.]+)?", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        """
        server = data['server']
        if server:
            match_obj = self.re_expr.search(server)
            if match_obj:
                metadata.product = 'Debut'
                metadata.version = match_obj.group('version')
                metadata.device_type = 'Printer' # TODO Puede ser una impresora brother
        return metadata
