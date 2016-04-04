import re
from http.http_process import HTTPProcess

__author__ = 'eduardo'


class VivotekCamera(HTTPProcess):
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
        server = self.get_header_field(data, 'server')

        if server:
            match_obj = self.re_expr.search(server)

            if match_obj:
                metadata.device.manufacturer = 'Vivotek'
                metadata.device.type = 'Camera'

        return metadata
