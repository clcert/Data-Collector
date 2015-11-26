import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class DlinkSerieDIR(HttpProcess):
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^linux,\s?http/([\d\.]+)?,\s?(?P<product>dir-[\w\+]+)\s?ver", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        """
        server = data['server']
        if server:
            match_obj = self.re_expr.search(server)
            if match_obj:
                metadata.manufacturer = 'Dlink'
                metadata.product = match_obj.group('product')
                metadata.device_type = 'Router'
        return metadata