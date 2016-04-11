import unittest
from data.metadata import Metadata
from http.www_auth.LinksysWirelessRouter import LinksysWirelessRouter


class LinksysWirelessRouterTest(unittest.TestCase):
    def test_one(self):
        data = {'header': {'www_authenticate': '"Basic realm=""WRT54GL"""'}}
        metadata = LinksysWirelessRouter().process(data, Metadata())

        self.assertEqual(metadata.device.manufacturer, 'Linksys')
        self.assertEqual(metadata.device.product, 'WRT54GL')
        self.assertEqual(metadata.device.type, 'Wireless Router')

    def test_two(self):
        data = {'header': {'www_authenticate': '"Basic realm=""WAP300N"""'}}
        metadata = LinksysWirelessRouter().process(data, Metadata())

        self.assertEqual(metadata.device.manufacturer, 'Linksys')
        self.assertEqual(metadata.device.product, 'WAP300N')
        self.assertEqual(metadata.device.type, 'Wireless Router')

    def test_three(self):
        data = {'header': {'www_authenticate': '"Basic realm=""Linksys WAP54G"""'}}
        metadata = LinksysWirelessRouter().process(data, Metadata())

        self.assertEqual(metadata.device.manufacturer, 'Linksys')
        self.assertEqual(metadata.device.product, 'WAP54G')
        self.assertEqual(metadata.device.type, 'Wireless Router')

    def test_four(self):
        data = {'header': {'www_authenticate': '"Basic realm=""E1200"""'}}
        metadata = LinksysWirelessRouter().process(data, Metadata())

        self.assertEqual(metadata.device.manufacturer, 'Linksys')
        self.assertEqual(metadata.device.product, 'E1200')
        self.assertEqual(metadata.device.type, 'Wireless Router')

    def test_five(self):
        data = {'header': {'www_authenticate': '"Basic realm=""Linksys E2100L"""'}}
        metadata = LinksysWirelessRouter().process(data, Metadata())

        self.assertEqual(metadata.device.manufacturer, 'Linksys')
        self.assertEqual(metadata.device.product, 'E2100L')
        self.assertEqual(metadata.device.type, 'Wireless Router')

    def test_six(self):
        data = {'header': {'www_authenticate': '"Basic realm=""Linksys EA2700""'}}
        metadata = LinksysWirelessRouter().process(data, Metadata())

        self.assertEqual(metadata.device.manufacturer, 'Linksys')
        self.assertEqual(metadata.device.product, 'EA2700')
        self.assertEqual(metadata.device.type, 'Wireless Router')

if __name__ == '__main__':
    unittest.main()