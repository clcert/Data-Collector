import unittest
from data.metadata import Metadata
from http.www_auth.TPLinkVPN import TPLinkVPN


class TPLinkVPNTest(unittest.TestCase):

    def test_one(self):
        data = {'header': {'www_authenticate': '"Basic realm=""TP-LINK Gigabit Broadband VPN Router R600VPN"""'}}
        metadata = TPLinkVPN().process(data, Metadata())

        self.assertEqual(metadata.device.manufacturer, 'TP-Link')
        self.assertEqual(metadata.device.product, 'R600VPN')
        self.assertEqual(metadata.device.type, 'VPN Router')


if __name__ == '__main__':
    unittest.main()