import re

from http.http_process import HTTPProcess


class CiscoRV(HTTPProcess):
    """
    http://www.cisco.com/c/en/us/products/routers/rv082-dual-wan-vpn-router/index.html
    """
    re_expr = re.compile("(?P<device>rv\d{3})", re.IGNORECASE)

    def process(self, data, metadata):
        www_auth = self.get_header_field(data, 'www_authenticate')

        if www_auth:
            match_obj = self.re_expr.search(www_auth)

            if match_obj:
                metadata.device.manufacturer = 'Cisco'
                metadata.device.product = match_obj.group('device')
                metadata.device.type = 'VPN Router'

        return metadata
