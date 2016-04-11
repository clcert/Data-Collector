import unittest
from data.metadata import Metadata
from http.www_auth.AsusWirelessRouter import AsusWirelessRouter


class AsusWirelessRouterTest(unittest.TestCase):
    def test_one(self):
        data = {'header': {'www_authenticate': '"Basic realm=""RT-N10P"""'}}
        metadata = AsusWirelessRouter().process(data, Metadata())

        self.assertEqual(metadata.device.manufacturer, 'Asus')
        self.assertEqual(metadata.device.product, 'RT-N10P')
        self.assertEqual(metadata.device.type, 'Wireless Router')


if __name__ == '__main__':
    unittest.main()