import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class H264WebCam(HttpProcess):
    """
    http://www.h264soft.com/es/index.html
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^h264webcam", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        """
        server = data['server']
        if server:
            if self.re_expr.search(server):
                metadata.product = 'H264 WebCam'
                metadata.device_type = 'Camera'
        return metadata   
