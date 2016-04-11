import re

from http.http_process import HTTPProcess


class BrickComCamera(HTTPProcess):
    """
    http://es.brickcom.com/products/product-search-COMPARE.php
    """
    re_expr = re.compile("brickcom\s*(?P<device>\w+-[\w\d]+)", re.IGNORECASE)

    def process(self, data, metadata):
        www_auth = self.get_header_field(data, 'www_authenticate')

        if www_auth:
            match_obj = self.re_expr.search(www_auth)

            if match_obj:
                metadata.device.manufacturer = 'Brickcom'
                metadata.device.product = match_obj.group('device')
                metadata.device.type = 'Camera'

        return metadata
