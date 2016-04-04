import re
from http.http_process import HTTPProcess

__author__ = 'eduardo'


class DVRDVS(HTTPProcess):

    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^dvrdvs-webs", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        """
        server = self.get_header_field(data, 'server')

        if server:
            if self.re_expr.search(server):
                metadata.service.product = 'DVRDVS Webs'
                metadata.device.type = 'Camera'

        return metadata

