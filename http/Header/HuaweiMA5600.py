import re
from http.http_process import HTTPProcess

__author__ = 'eduardo'


class HuaweiMA5600(HTTPProcess):
    """
    http://carrier.huawei.com/en/products/fixed-access/dslam/
    http://www.alibaba.com/product-detail/Huawei-64-channel-ADSL2-SmartAX-MA5600_60252335687.html?spm=a2700.7724857.29.64.mvYW4x
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^ma5600", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        """
        server = self.get_header_field(data, 'server')

        if server:
            if self.re_expr.search(server):
                metadata.device.manufacturer = 'Huawei'
                metadata.device.product = 'MA5600'
                metadata.device.type = 'IP broadband access device'

        return metadata
