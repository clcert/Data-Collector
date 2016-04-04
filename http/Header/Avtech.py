import re
from http.http_process import HTTPProcess

__author__ = 'eduardo'


class Avtech(HTTPProcess):
    """
    http://www.avtech.com.tw/
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^Linux/(?P<os_version>[\d\.x]+).*Avtech/(?P<version>[\d\.]+)", re.IGNORECASE)

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
                metadata.device.manufacturer = 'Avtech'
                metadata.device.os = 'Linux'
                metadata.device.os_version = match_obj.group('os_version')
                metadata.device.type = 'Camera'

        return metadata

