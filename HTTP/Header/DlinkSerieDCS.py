import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class DlinkSerieDCS(HttpProcess):
    """
    http://www.dlinkla.com/dcs-2120
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^(?P<product>dcs-\d+)", re.IGNORECASE)

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
                metadata.device.type = 'Camera'

        return metadata
