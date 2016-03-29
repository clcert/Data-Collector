import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class TibetSystem(HttpProcess):
    """
    http://www.tibetsystem.com/eng/index.html
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^tibetsystem\s?server\s?(?P<version>[\d\.]+)?", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        """
        server = self.get_header_field(data, 'server')

        if server:
            match_obj = self.re_expr.search(server)

            if match_obj:
                metadata.service.manufacturer = 'TibetSystem'
                metadata.service.product = 'TibetSystem Server'
                metadata.service.version = match_obj.group('version')
                metadata.device.manufacturer = 'Gnet'
                metadata.device.type = 'Camera'

        return metadata
