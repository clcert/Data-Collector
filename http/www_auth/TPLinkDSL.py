import re

from http.http_process import HTTPProcess


class TPLinkDSL(HTTPProcess):
    """
    http://www.tp-link.com/en/products/details/TL-R860.html
    http://www.tp-link.com/lk/products/details/cat-4762_TL-R460.html
    """

    re_expr = re.compile("tp-link\srouter\s(?P<device>R\d{3})\"", re.IGNORECASE)

    def process(self, data, metadata):
        www_auth = self.get_header_field(data, 'www_authenticate')

        if www_auth:
            match_obj = self.re_expr.search(www_auth)

            if match_obj:
                metadata.device.manufacturer = 'TP-Link'
                metadata.device.product =  match_obj.group('device')
                metadata.device.type = 'DSL Modem'

        return metadata
