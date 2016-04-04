import re
from http.http_process import HTTPProcess

__author__ = 'eduardo'


class HikvisionWebs(HTTPProcess):
    """
    http://overseas.hikvision.com/en/
    """

    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^hikvision-?webs", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        """
        server = self.get_header_field(data, 'server')

        if server:
            if self.re_expr.search(server):
                metadata.service.manufacturer = 'Hikvision'
                metadata.service.product = 'Hikvision Webs'
                metadata.device.manufacturer = 'Hikvision'
                metadata.device.type = 'Camera'

        return metadata
