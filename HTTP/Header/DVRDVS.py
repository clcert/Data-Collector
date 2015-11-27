import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class DVRDVS(HttpProcess):

    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^dvrdvs-webs", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        """
        server = data['server']
        if server:
            if self.re_expr.search(server):
                metadata.service.product = 'DVRDVS Webs'
                metadata.device.type = 'Camera'
        return metadata
