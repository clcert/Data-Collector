import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class MiniHttpd(HttpProcess):
    """
    http://acme.com/software/mini_httpd/
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^mini_httpd/?(?P<version>[\d\.]+)?\s?(\((?P<os>\w+)\))?", re.IGNORECASE)

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
                metadata.product = 'Mini Httpd'
                metadata.version = match_obj.group('version')
                metadata.os = match_obj.group('os')
        return metadata