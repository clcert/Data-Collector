import re

from http.http_process import HTTPProcess


class SwannNVR(HTTPProcess):
    """
    http://www.swann.com/us/swnvk-873008
    """
    re_expr = re.compile("(?P<device>nvr\d+)", re.IGNORECASE)

    def process(self, data, metadata):
        www_auth = self.get_header_field(data, 'www_authenticate')

        if www_auth:
            match_obj = self.re_expr.search(www_auth)

            if match_obj:
                metadata.device.manufacturer = 'Swann'
                metadata.device.product = match_obj.group('device')
                metadata.device.type = 'DVR'

        return metadata
