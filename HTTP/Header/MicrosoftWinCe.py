import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class MicrosoftWinCe(HttpProcess):
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
        server = data['server']
        if server:
            match_obj = self.re_expr.search(server)
            if match_obj:
                metadata.device.os = 'Windows Embedded Compact'
                metadata.device.os_version = match_obj.group('version')
        return metadata