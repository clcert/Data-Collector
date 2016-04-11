import re

from http.http_process import HTTPProcess


class WilmersDataLogger(HTTPProcess):
    """
    Weather
    http://wilmers.net/html_en/html/dataloggers_en.html
    """
    re_expr = re.compile("ndl-?485", re.IGNORECASE)

    def process(self, data, metadata):
        www_auth = self.get_header_field(data, 'www_authenticate')

        if www_auth:
            if self.re_expr.search(www_auth):
                metadata.device.manufacturer = 'Wilmers'
                metadata.device.product = 'blueberry NDL 485'
                metadata.device.type = 'Data Logger'

        return metadata
