import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class WebSphere(HttpProcess):
    """
    http://www-03.ibm.com/software/products/es/appserv-was
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^websphere application server/?(?P<version>[\d\.]+)?", re.IGNORECASE)

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
                metadata.service.manufacturer = 'IBM'
                metadata.service.product = 'WebSphere Application Server'
                metadata.service.version = match_obj.group('version')
        return metadata