import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class IPSharereWeb(HttpProcess):
    """
    Router, modems, cameras, embedded systems, etc
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^ip_sharer web\s?(?P<version>[\d\.]+)?", re.IGNORECASE)

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
                metadata.product = 'IP Sharer Web'
                metadata.version = match_obj.group('version')
        return metadata