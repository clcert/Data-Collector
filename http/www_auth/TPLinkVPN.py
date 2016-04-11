import re

from http.http_process import HTTPProcess


class TPLinkVPN(HTTPProcess):
    """
    http://www.tp-link.com/ar/products/details/cat-4909_TL-R600VPN.html
    """
    re_expr = re.compile("tp-link.*vpn\s*router\s*(?P<device>[\w\d]+)", re.IGNORECASE)

    def process(self, data, metadata):
        www_auth = self.get_header_field(data, 'www_authenticate')

        if www_auth:
            match_obj = self.re_expr.search(www_auth)

            if match_obj:
                metadata.device.manufacturer = 'TP-Link'
                metadata.device.product = match_obj.group('device')
                metadata.device.type = 'VPN Router'

        return metadata
