import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class VirataEmWeb(HttpProcess):
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^virata-emweb/?(?P<version>[\w\.]+)?", re.IGNORECASE)

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
                metadata.product = 'Virata EmWeb'
                metadata.product = match_obj.group('version')
        return metadata
