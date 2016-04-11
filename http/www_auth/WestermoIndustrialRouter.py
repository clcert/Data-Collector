import re

from http.http_process import HTTPProcess


class WestermoIndustrialRouter(HTTPProcess):
    """
    http://www.westermo.com/web/web_en_idc_com.nsf/alldocuments/29821514BB878417C1257D8800502F47
    http://www.westermo.com/web/web_en_idc_com.nsf/alldocuments/AB3ABDFBDB2D5F51C12578F500488D5F
    """
    re_expr = re.compile("westermo\s?(?P<device>mrd-?\d{3})", re.IGNORECASE)

    def process(self, data, metadata):
        www_auth = self.get_header_field(data, 'www_authenticate')

        if www_auth:
            match_obj = self.re_expr.search(www_auth)

            if match_obj:
                metadata.device.manufacturer = 'Westermo'
                metadata.device.product = match_obj.group('device')
                metadata.device.type = 'Industrial Router'

        return metadata
