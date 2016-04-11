import re

from http.http_process import HTTPProcess


class AsusWirelessRouter(HTTPProcess):
    """
    https://www.asus.com/Networking/RTN66U/
    """
    re_expr = re.compile("\"(?P<device>rt[-\d\w]+)", re.IGNORECASE)

    def process(self, data, metadata):
        www_auth = self.get_header_field(data, 'www_authenticate')

        if www_auth:
            match_obj = self.re_expr.search(www_auth)

            if match_obj:
                metadata.device.manufacturer = 'Asus'
                metadata.device.product = match_obj.group('device')
                metadata.device.type = 'Wireless Router'

        return metadata
