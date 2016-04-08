import unittest
from data.metadata import Metadata
from http.www_auth.TPLinkLoadBalance import TPLinkLoadBalance


class TPLinkLoadBalanceTest(unittest.TestCase):
    def test_one(self):
        data = {'header': {'www_authenticate': '"Basic realm=""TP-LINK Router R480T+"""'}}
        metadata = TPLinkLoadBalance().process(data, Metadata())

        self.assertEqual(metadata.device.manufacturer, 'TP-Link')
        self.assertEqual(metadata.device.product, 'R480T')
        self.assertEqual(metadata.device.type, 'Load Balance Router')


if __name__ == '__main__':
    unittest.main()