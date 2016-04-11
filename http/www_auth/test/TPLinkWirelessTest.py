import unittest

from data.metadata import Metadata
from http.www_auth.TPLinkWireless import TPLinkWireless


class TPLinkWirelessTest(unittest.TestCase):
    def test_one(self):
        data = {'header': {'www_authenticate': '"Basic realm=""TP-LINK Wireless Lite N Router WR740N/WR741ND"""'}}
        metadata = TPLinkWireless().process(data, Metadata())
        self.assertEqual(metadata.device.product, 'WR740N')
        self.assertEqual(metadata.device.manufacturer, 'TP-Link')
        self.assertEqual(metadata.device.type, 'Wireless Router')

    def test_two(self):
        data = {'header': {'www_authenticate': '"Basic realm=""TP-LINK Wireless Router WR340G"""'}}
        metadata = TPLinkWireless().process(data, Metadata())
        self.assertEqual(metadata.device.product, 'WR340G')
        self.assertEqual(metadata.device.manufacturer, 'TP-Link')
        self.assertEqual(metadata.device.type, 'Wireless Router')

    def test_three(self):
        data = {'header': {'www_authenticate': '"Basic realm=""TP-LINK Portable Wireless N 3G/4G Router MR3020"""'}}
        metadata = TPLinkWireless().process(data, Metadata())
        self.assertEqual(metadata.device.product, 'MR3020')
        self.assertEqual(metadata.device.manufacturer, 'TP-Link')
        self.assertEqual(metadata.device.type, 'Wireless Router')

    def test_four(self):
        data = {'header': {'www_authenticate': '""TP-LINK Outdoor Wireless Access Point WA7210N"""'}}
        metadata = TPLinkWireless().process(data, Metadata())
        self.assertEqual(metadata.device.product, 'WA7210N')
        self.assertEqual(metadata.device.manufacturer, 'TP-Link')
        self.assertEqual(metadata.device.type, 'Wireless Router')


if __name__ == '__main__':
    unittest.main()
