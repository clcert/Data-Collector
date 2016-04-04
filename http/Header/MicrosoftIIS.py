import re
from http.http_process import HTTPProcess

__author__ = 'eduardo'


class MicrosoftIIS(HTTPProcess):
    """
    https://www.iis.net/
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^microsoft[-\s]?iis/?(?P<version>[\d\.]+)?", re.IGNORECASE)

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
                metadata.service.manufacturer = 'Microsoft'
                metadata.service.product = 'IIS'
                metadata.service.version = match_obj.group('version')
                metadata.device.os = 'Windows'

        return metadata
