import re

from http.http_process import HTTPProcess


class BelkinNetCam(HTTPProcess):
    """
    http://www.belkin.com/us/Products/home-automation/c/netcam/
    """
    re_expr = re.compile("netcam", re.IGNORECASE)

    def process(self, data, metadata):
        www_auth = self.get_header_field(data, 'www_authenticate')

        if www_auth:
            if self.re_expr.search(www_auth):
                metadata.device.manufacturer = 'Belkin'
                metadata.device.type = 'Camera'

        return metadata
