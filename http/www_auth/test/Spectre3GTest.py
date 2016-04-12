import unittest
from data.metadata import Metadata
from http.www_auth.Spectre3G import Spectre3G


class Spectre3GTest(unittest.TestCase):
    def test_one(self):
        data = {'header': {'www_authenticate': '"Basic realm=""SPECTRE-3G"""'}}
        metadata = Spectre3G().process(data, Metadata())

        self.assertEqual(metadata.device.manufacturer, 'B+B SmartWorx')
        self.assertEqual(metadata.device.product, 'Spectre 3G')
        self.assertEqual(metadata.device.type, 'Industrial Wireless Router')


if __name__ == '__main__':
    unittest.main()