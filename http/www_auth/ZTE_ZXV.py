import re

from http.http_process import HTTPProcess


class ZTE_ZXV(HTTPProcess):
    """
    http://wwwen.zte.com.cn/en/products/access/cpe/201302/t20130204_386351.html
    """

    re_expr = re.compile('zxv10 w300', re.IGNORECASE)

    def process(self, data, metadata):

        www_auth = self.get_header_field(data, 'www_authenticate')

        if www_auth:
            if self.re_expr.search(www_auth):
                metadata.device.product = 'ZXV10 W300'
                metadata.device.type ='DSL Modem'
                metadata.device.manufacturer = 'ZTE'

        return metadata
