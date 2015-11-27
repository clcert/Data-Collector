import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class IPCamera(HttpProcess):
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^ip\s?camera(-?webs)?/?(?P<version>[\d\.]+)?", re.IGNORECASE)

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
                metadata.service.product = 'IP Camera Web'
                metadata.service.version = match_obj.group('version')
                metadata.device.type = 'Camera'
        return metadata