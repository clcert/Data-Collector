import re

from http.http_process import HTTPProcess


class LinksysWirelessRouter(HTTPProcess):
    """
    http://www.linksys.com/es/support-product?pid=01t80000003KO7WAAW
    http://www.linksys.com/es/p/P-E1200/
    http://www.linksys.com/es/p/P-EA4500/
    http://www.linksys.com/ar/support-article?articleNum=135241
    """
    re_expr = re.compile("(\"|(linksys))?\s*(?P<device>(wap\d{2,3}\w)|(wrt[\d\w]+)|(ea?\d+l?))", re.IGNORECASE)

    def process(self, data, metadata):
        www_auth = self.get_header_field(data, 'www_authenticate')

        if www_auth:
            match_obj = self.re_expr.search(www_auth)

            if match_obj:
                metadata.device.manufacturer = "Linksys"
                metadata.device.product = match_obj.group('device')
                metadata.device.type = "Wireless Router"

        return metadata
