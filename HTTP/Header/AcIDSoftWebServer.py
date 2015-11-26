import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class AcIDSoftWebServer(HttpProcess):
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^acidsoftwebserver/?(?P<version>[\w\.]+)?", re.IGNORECASE)

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
                metadata.product = 'AcIDSoftWebServer'
                metadata.version = match_obj.group('version')
                metadata.device_type = 'SCADA' # TODO embedded
        return metadata

