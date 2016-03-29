import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class SpeedTouch(HttpProcess):
    """
    https://support.zen.co.uk/kb/Knowledgebase/ThomsonSpeedTouch-585780WL-Wireless-Setup
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^speed touch webserver/?(?P<version>[\d\.]+)?", re.IGNORECASE)

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
                metadata.service.manufacturer = 'Thomson'
                metadata.service.product = 'Speed Touch Web Server'
                metadata.service.version = match_obj.group('version')
                metadata.device.manufacturer = 'Thomson'
                metadata.device.product = 'Speed Touch'
                metadata.device.type = 'Router'

        return metadata   
