import re

from http.http_process import HTTPProcess


class Spectre3G(HTTPProcess):
    """
    http://www.bb-smartcellular.com/
    """
    re_expr = re.compile("spectre-3g", re.IGNORECASE)

    def process(self, data, metadata):
        www_auth = self.get_header_field(data, 'www_authenticate')

        if www_auth:
            if self.re_expr.search(www_auth):
                metadata.device.manufacturer = 'B+B SmartWorx'
                metadata.device.product = 'Spectre 3G'
                metadata.device.type = 'Industrial Wireless Router'

        return metadata
