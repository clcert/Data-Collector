import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class Companion(HttpProcess):

    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^companion web server\s?/?(?P<version>[\d\.]+)?", re.IGNORECASE)

    def process(self, data, metadata):
        '''
        :param data: dict
        :param metadata: Metadata
        '''
        server = HttpProcess.getServer(data)
        if server:
            match_obj = self.re_expr.search(server)
            if match_obj:
                metadata.product = 'Companion Web Server'
                metadata.version = match_obj.group('version')
        return metadata





