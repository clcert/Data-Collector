import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class EmbedthisAppweb(HttpProcess):
    """
    https://embedthis.com/appweb/
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^embedthis[\s-]?appweb/?(?P<version>[\d\.]+)?", re.IGNORECASE)

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
                metadata.product = 'Appweb Web Server'
                metadata.device_type = 'Embedded'
        return metadata