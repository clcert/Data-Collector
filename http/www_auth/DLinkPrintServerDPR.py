import re

from http.http_process import HTTPProcess


class DLinkPrintServerDPR(HTTPProcess):
    """
    http://www.dlink.com/es/es/home-solutions/connect/print-servers/dpr-1061-3-port-multifunction-print-server
    http://www.dlink.com/es/es/home-solutions/connect/print-servers/dpr-1020-usb-multifunction-print-server
    """
    re_expr = re.compile("(?P<device>dpr-?\d+)", re.IGNORECASE)

    def process(self, data, metadata):
        www_auth = self.get_header_field(data, 'www_authenticate')

        if www_auth:
            match_obj = self.re_expr.search(www_auth)

            if match_obj:
                metadata.device.manufacturer = 'DLink'
                metadata.device.product = match_obj.group('device')
                metadata.device.type = 'Print Server'

        return metadata
