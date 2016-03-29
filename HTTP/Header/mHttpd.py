import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class mHttpd(HttpProcess):
    """
    http://www.muquit.com/muquit/software/mhttpd/mhttpd.html
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^mhttpd\s?v?(?P<version>[\d\.]+)?", re.IGNORECASE)

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
                metadata.service.product = 'mhttpd'
                metadata.service.version = match_obj.group('version')

        return metadata
