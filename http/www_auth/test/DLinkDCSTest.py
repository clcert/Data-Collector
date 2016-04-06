import unittest

from data.metadata import Metadata
from http.www_auth.DLInkDCS import DLinkDCS


class DLinkDCSTest(unittest.TestCase):
    def test_one(self):
        data = {'header': {'www_authenticate': '"Basic realm=""DCS-930LB1"""'}}
        metadata = DLinkDCS().process(data, Metadata())
        self.assertEqual(metadata.device.product, 'DCS-930LB1')
        self.assertEqual(metadata.device.manufacturer, 'DLink')
        self.assertEqual(metadata.device.type, 'Camera')

    def test_two(self):
        data = {'header': {'www_authenticate': '"Basic realm=""DCS-930L"""'}}
        metadata = DLinkDCS().process(data, Metadata())
        self.assertEqual(metadata.device.product, 'DCS-930L')
        self.assertEqual(metadata.device.manufacturer, 'DLink')
        self.assertEqual(metadata.device.type, 'Camera')


if __name__ == '__main__':
    unittest.main()
