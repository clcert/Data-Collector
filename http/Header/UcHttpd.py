import re
from http.http_process import HTTPProcess

__author__ = 'eduardo'


class UcHttpd(HTTPProcess):
    """
    https://www.micrium.com/
    https://doc.micrium.com/display/httpdoc/About+HTTP-server
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^uc-httpd/?\s?(?P<version>[\d\.]+)?", re.IGNORECASE)

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
                metadata.service.manufacturer = 'Micrium'
                metadata.service.product = 'UC httpd'
                metadata.service.version = match_obj.group('version')
                # metadata.device.type = 'Camera'

        return metadata
