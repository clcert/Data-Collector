import re
from http.http_process import HTTPProcess

__author__ = 'eduardo'


class MicrosoftWinCe(HTTPProcess):
    """
    https://en.wikipedia.org/wiki/Windows_CE
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^microsoft-wince/?(?P<version>[\d\.]+)?", re.IGNORECASE)

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
                metadata.device.os = 'Windows Embedded Compact'
                metadata.device.os_version = match_obj.group('version')

        return metadata
