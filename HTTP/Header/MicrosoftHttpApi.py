import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class MicrosoftHttpApi(HttpProcess):
    """
    https://msdn.microsoft.com/en-us/library/windows/desktop/aa364510%28v=vs.85%29.aspx
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^microsoft-httpapi/?(?P<version>[\d\.]+)?", re.IGNORECASE)

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
                metadata.service.product = 'HTTP Server API'
                metadata.service.version = match_obj.group('version')
                metadata.device.os = 'Windows'

        return metadata
