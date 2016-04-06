import re

from http.http_process import HTTPProcess


class ZnidZhone(HTTPProcess):
    """
    http://www.zhone.com/products/ZNID-GE-24xx/
    """

    re_expr = re.compile('znid24xx', re.IGNORECASE)

    def process(self, data, metadata):

        www_auth = self.get_header_field(data, 'www_authenticate')

        if www_auth:
            if self.re_expr.search(www_auth):
                #TODO i am not sure if fiber modem, dsl modem or modem  metadata.device.type = 'DSL Modem'
                metadata.device.product = 'zNID 24xx Series'
                metadata.device.manufacturer = 'Zhone'

        return metadata
