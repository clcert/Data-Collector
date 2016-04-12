import re

from http.http_process import HTTPProcess


class GenericDVR(HTTPProcess):
    re_expr = re.compile("dvr", re.IGNORECASE)

    def process(self, data, metadata):
        www_auth = self.get_header_field(data, 'www_authenticate')

        if www_auth:
            match_obj = self.re_expr.search(www_auth)

            if match_obj:
                metadata.device.type = 'DVR'

        return metadata
