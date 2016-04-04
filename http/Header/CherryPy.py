import re
from http.http_process import HTTPProcess

__author__ = 'eduardo'


class CherryPy(HTTPProcess):
    """
    http://www.cherrypy.org/
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^cherrypy/?(?P<version>[\d\.]+)?", re.IGNORECASE)

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
                metadata.service.manufacturer = 'CherryPy'
                metadata.service.product = 'CherryPy'
                metadata.service.version = match_obj.group('version')

        return metadata   
