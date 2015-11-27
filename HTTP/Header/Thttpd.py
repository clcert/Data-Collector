import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class Thttpd(HttpProcess):
    """
    http://acme.com/software/thttpd/
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^thttpd/?(?P<version>[\w\.]+)?", re.IGNORECASE)

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
                metadata.service.manufacturer = 'ACME'
                metadata.service.product = 'thttpd'
                metadata.service.version = match_obj.group('version')
        return metadata
