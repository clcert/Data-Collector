import re
from http.http_process import HTTPProcess

__author__ = 'eduardo'


class WindRiver(HTTPProcess):
    """
    http://www.windriver.com/
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^windriver-webserver/?(?P<version>[\d\.]+)?", re.IGNORECASE)

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
                metadata.service.manufacturer = 'Wind River'
                metadata.service.product = 'Web Server'
                metadata.service.version = match_obj.group('version')

        return metadata
