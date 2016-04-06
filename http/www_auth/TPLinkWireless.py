import re

from http.http_process import HTTPProcess


class TPLinkWireless(HTTPProcess):

    re_expr = re.compile('tp-link\s*wireless.*router\s*(?P<device>[\w\d]+)', re.IGNORECASE)

    def process(self, data, metadata):
        www_auth = self.get_header_field(data, 'www_authenticate')

        if www_auth:
            match_obj = self.re_expr.search(www_auth)

            if match_obj:
                metadata.device.type = 'Wireless Router'
                metadata.device.product = match_obj.group('device')
                metadata.device.manufacturer = 'TP-Link'

        return metadata
