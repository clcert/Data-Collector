import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class DNVRS(HttpProcess):
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^dnvrs-webs", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        """
        server = self.get_header_field(data, 'server')

        if server:
            match_obj = self.re_expr.search(server)

            if match_obj:
                metadata.service.product = 'DNVRS Web'
                metadata.device.type = 'Camera'

        return metadata

