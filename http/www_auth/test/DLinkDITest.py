import unittest
from data.metadata import Metadata
from http.www_auth.DLinkDI import DLinkDI


class DLinkDITest(unittest.TestCase):
    def test_one(self):
        data = {'header': {'www_authenticate': '"Basic realm=""DI-824VUP"""'}}
        metadata = DLinkDI().process(data, Metadata())

        self.assertEqual(metadata.device.manufacturer, 'DLink')
        self.assertEqual(metadata.device.product, 'DI-824VUP')
        self.assertEqual(metadata.device.type, 'Wireless Router')


if __name__ == '__main__':
    unittest.main()