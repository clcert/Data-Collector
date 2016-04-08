import re

from http.http_process import HTTPProcess


class TrendnetCamera(HTTPProcess):
    """
    https://www.trendnet.com/langsp/products/ip-cameras/tv-ip751wc
    https://www.trendnet.com/langsp/products/proddetail?prod=225_TV-IP751WIC
    """

    re_expr = re.compile('(tv-ip\d{3}wi?c?)', re.IGNORECASE)

    def process(self, data, metadata):

        www_auth = self.get_header_field(data, 'www_authenticate')

        if www_auth:
            match_obj = self.re_expr.search(www_auth)

            if match_obj:
                metadata.device.manufacturer = 'TRENDnet'
                metadata.device.type = 'Camera'
                metadata.device.product = match_obj.group(0)

        return metadata
