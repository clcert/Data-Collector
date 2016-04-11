import re

from http.http_process import HTTPProcess


class SonyVideoCommunication(HTTPProcess):
    """
    http://www.manualslib.com/manual/377217/Sony-Pcs-Xg80.html
    """
    re_expr = re.compile("(?P<device>pcs-[\w\d]+)", re.IGNORECASE)

    def process(self, data, metadata):
        www_auth = self.get_header_field(data, 'www_authenticate')

        if www_auth:
            match_obj = self.re_expr.search(www_auth)

            if match_obj:
                metadata.device.manufacturer = 'Sony'
                metadata.device.product = match_obj.group('device')
                metadata.device.type = 'Video Communication System'

        return metadata
