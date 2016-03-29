import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class OracleWebCache(HttpProcess):
    """
    http://www.oracle.com/webfolder/technetwork/tutorials/obe/fmw/web_cache/11g/r1/wc_wls/wc_wls.htm
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^oracle(as)?[-\s]?web[-\s]?cache[-\s]?(?P<version>[/\w\.]+)?", re.IGNORECASE)

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
                metadata.service.manufacturer = 'Oracle'
                metadata.service.product = 'Web Cache'
                metadata.service.version = match_obj.group('version')

        return metadata
