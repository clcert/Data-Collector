import re
from http.http_process import HTTPProcess

__author__ = 'eduardo'


class EmbedthisAppweb(HTTPProcess):
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
        server = self.get_header_field(data, 'server')

        if server:
            match_obj = self.re_expr.search(server)
            if match_obj:
                metadata.service.manufacturer = 'Embedthis'
                metadata.service.product = 'Appweb Web Server'
                metadata.device.type = 'Embedded'

        return metadata
