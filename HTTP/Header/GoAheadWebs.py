import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class GoAheadWebs(HttpProcess):
    """
    https://embedthis.com/goahead/
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^goahead(-webs)?/?(?P<version>[\d\.]+)?", re.IGNORECASE)

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
                metadata.service.manufacturer = 'Embedthis'
                metadata.service.product = 'GoAhead Web Server'
                metadata.service.version = match_obj.group('version')
                metadata.device.type = 'Embedded'

        return metadata
