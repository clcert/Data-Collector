import re

from http.http_process import HTTPProcess


class TPLinkLoadBalance(HTTPProcess):
    """
    http://www.tp-link.com/ar/products/details/cat-4910_TL-R480T%2B.html
    http://www.amazon.com/TP-LINK-TL-R470T-Broadband-Changeable-Ethernet/dp/B005SYQBN8
    """

    re_expr = re.compile("tp-link\srouter\s(?P<device>R\d{3}T)", re.IGNORECASE)

    def process(self, data, metadata):
        www_auth = self.get_header_field(data, 'www_authenticate')

        if www_auth:
            match_obj = self.re_expr.search(www_auth)

            if match_obj:
                metadata.device.manufacturer = 'TP-Link'
                metadata.device.product = match_obj.group('device')
                metadata.device.type = 'Load Balance Router'

        return metadata
