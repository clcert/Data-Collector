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
        server = HttpProcess.getServer(data)
        if server:
            match_obj = self.re_expr.search(server)
            if match_obj:
                metadata.product = 'GoAhead Web Server'
                metadata.version = match_obj.group('version')
                metadata.device_type = 'Embedded'
        return metadata