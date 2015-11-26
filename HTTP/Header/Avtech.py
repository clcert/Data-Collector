import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class Avtech(HttpProcess):
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^Linux/(?P<os_version>[\d\.x]+).*Avtech/(?P<version>[\d\.]+)", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        """
        server = HttpProcess.getServer(data)
        if server:
            match_obj = self.re_expr.search(server)
            if match_obj:
                metadata.product = 'Avtech'
                metadata.version = match_obj.group('version')
                metadata.os = 'Linux'
                metadata.os_version = match_obj.group('os_version')
                metadata.device_type = 'Camera'
        return metadata

