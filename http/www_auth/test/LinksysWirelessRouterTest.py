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


if __name__ == '__main__':
    unittest.main()