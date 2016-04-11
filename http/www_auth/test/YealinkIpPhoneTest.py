import unittest
from data.metadata import Metadata
from http.www_auth.YealinkIpPhone import YealinkIpPhone


class YealinkIpPhoneTest(unittest.TestCase):
    def test_one(self):
        data = {'header': {'www_authenticate': '"Basic realm=""Enterprise IP phone SIP-T20P"""'}}
        metadata = YealinkIpPhone().process(data, Metadata())

        self.assertEqual(metadata.device.manufacturer, 'Yealink')
        self.assertEqual(metadata.device.product, 'SIP-T20P')
        self.assertEqual(metadata.device.type, 'Ip Phone')


if __name__ == '__main__':
    unittest.main()