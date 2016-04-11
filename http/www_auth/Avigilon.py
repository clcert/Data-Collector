import re

from http.http_process import HTTPProcess


class Avigilon(HTTPProcess):
    """
    http://avigilon.com/products/
    """
    re_expr = re.compile("avigilon", re.IGNORECASE)

    def process(self, data, metadata):
        www_auth = self.get_header_field(data, 'www_authenticate')

        if www_auth:
            if self.re_expr.search(www_auth):
                metadata.device.manufacturer = 'Avigilon'

        return metadata
