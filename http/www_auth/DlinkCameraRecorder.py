import re

from http.http_process import HTTPProcess


class DlinkCameraRecorder(HTTPProcess):
    """
    http://us.dlink.com/products/home-solutions/mydlink-camera-video-recorder/
    """

    re_expr = re.compile("(?P<device>dnr-?[\d\w]+)", re.IGNORECASE)

    def process(self, data, metadata):
        www_auth = self.get_header_field(data, 'www_authenticate')

        if www_auth:
            match_obj = self.re_expr.search(www_auth)

            if match_obj:
                metadata.device.manufacturer = 'DLink'
                metadata.device.product = match_obj.group('device')
                metadata.device.type = 'DVR'

        return metadata
