import re
from http.http_process import HTTPProcess

__author__ = 'eduardo'


class Henry(HTTPProcess):# Todo Revisar
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^henry/?(?P<version>[\d\.]+)?", re.IGNORECASE)

    def process(self, data, metadata):
        '''
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        '''
        server = self.get_header_field(data, 'server')
        if server:
            match_obj = self.re_expr.search(server)

            if match_obj:
                metadata.service.product = 'Henry'
                metadata.service.version = match_obj.group('version')

        return metadata   
