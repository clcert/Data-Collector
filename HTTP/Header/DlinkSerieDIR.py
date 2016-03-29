import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class DlinkSerieDIR(HttpProcess):
    """
    http://www.dlinkla.com/dir-850l
    http://www.dlinkla.com/dir-610n-plus
    http://www.dlinkla.com/dir-868l
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^linux,\s?http/([\d\.]+)?,\s?(?P<product>dir-[\w\+]+)\s?ver", re.IGNORECASE)

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
                metadata.device.manufacturer = 'Dlink'
                metadata.device.product = match_obj.group('product')
                metadata.device.type = 'Router'

        return metadata
