import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class HikvisionWebs(HttpProcess):
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
        server = data['server']
        if server:
            if self.re_expr.search(server):
                metadata.product = 'Hikvision Webs'
                metadata.device_type = 'Camera'
        return metadata