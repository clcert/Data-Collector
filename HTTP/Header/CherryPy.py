import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class CherryPy(HttpProcess):
    """
    http://www.cherrypy.org/
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^cherrypy/?(?P<version>[\d\.]+)?", re.IGNORECASE)

    def process(self, data, metadata):
        '''
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        '''
        server = HttpProcess.getServer(data)
        if server:
            match_obj = self.re_expr.search(server)
            if match_obj:
                metadata.product = 'CherryPy'
                metadata.version = match_obj.group('version')
        return metadata   
