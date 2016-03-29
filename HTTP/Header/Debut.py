import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class Debut(HttpProcess):# TODO Revisar
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^debut/?(?P<version>[\d\.]+)?", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        """
        server = self.get_header_field(data, 'server')

        if server:
            match_obj = self.re_expr.search(server)

            if match_obj:
                metadata.service.product = 'Debut'
                metadata.service.version = match_obj.group('version')
                metadata.device.type = 'Printer' # TODO Puede ser una impresora brother

        return metadata
