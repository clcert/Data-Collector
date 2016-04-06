import re

from http.http_process import HTTPProcess


class DLinkDCS(HTTPProcess):
    """
    https://www.mydlink.com/download
    """

    re_expr = re.compile('(?P<device>DCS-[\w\d]+)', re.IGNORECASE)

    def process(self, data, metadata):
        www_auth = self.get_header_field(data, 'www_authenticate')

        if www_auth:
            match_obj = self.re_expr.search(www_auth)

            if match_obj:
                metadata.device.type = 'Camera'
                metadata.device.product = match_obj.group('device')
                metadata.device.manufacturer = 'DLink'

        return metadata
