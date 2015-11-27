import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class UcHttpd(HttpProcess):
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^uc-httpd/?\s?(?P<version>[\d\.]+)?", re.IGNORECASE)

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
                metadata.service.product = 'UC httpd'
                metadata.service.version = match_obj.group('version')
                metadata.device.type = 'Camera' # Todo I think
        return metadata