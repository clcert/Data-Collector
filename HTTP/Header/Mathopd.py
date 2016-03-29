import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class Mathopd(HttpProcess):
    """
    http://www.mathopd.org/
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^mathopd/?(?P<version>[\dp\.]+)?", re.IGNORECASE)

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
                metadata.service.product = 'Mathopd'
                metadata.service.version = match_obj.group('version')

        return metadata
