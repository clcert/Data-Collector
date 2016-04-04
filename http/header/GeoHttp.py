import re
from http.http_process import HTTPProcess

__author__ = 'eduardo'


class GeoHTTP(HTTPProcess):
    """
    http://www.geovision.com.tw
    """

    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^geohttpserver", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return metadata
        """
        server = self.get_header_field(data, 'server')

        if server:
            if self.re_expr.search(server):
                metadata.service.manufacturer = 'GeoVision'
                metadata.service.product = 'Geo Http Server'
                metadata.device.manufacturer = 'GeoVision'
                metadata.device_type = 'Camera'

        return metadata



