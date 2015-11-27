import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class VivotekCamera(HttpProcess):
    """
    http://www.vivotek.com/
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^vivotek network camera", re.IGNORECASE)

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
                metadata.device.manufacturer = 'Vivotek'
                metadata.device.type = 'Camera'
        return metadata