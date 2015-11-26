import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class GeoHttp(HttpProcess):
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
        server = data['server']
        if server:
            if self.re_expr.search(server):
                metadata.product = 'Geo Http Server'
                metadata.device_type = 'Camera' # TODO segun la pagina web
        return metadata



