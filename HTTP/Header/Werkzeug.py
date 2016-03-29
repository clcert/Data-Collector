import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class Werkzeug(HttpProcess):
    """
    http://werkzeug.pocoo.org/
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^werkzeug/?(?P<version>[\d\.]+)?", re.IGNORECASE)

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
                metadata.service.product = 'Werkzeug'
                metadata.service.version = match_obj.group('version')

        return metadata
