import re

from http.http_process import HTTPProcess


class YealinkIpPhone(HTTPProcess):
    """
    http://www.yealink.com/product_info.aspx?ProductsCateID=187
    """
    re_expr = re.compile("enterprise\s?ip\s?phone\s?(?P<device>[\w\d-]+)", re.IGNORECASE)

    def process(self, data, metadata):
        www_auth = self.get_header_field(data, 'www_authenticate')

        if www_auth:
            match_obj = self.re_expr.search(www_auth)

            if match_obj:
                metadata.device.manufacturer = 'Yealink'
                metadata.device.product = match_obj.group('device')
                metadata.device.type = 'Ip Phone'

        return metadata
