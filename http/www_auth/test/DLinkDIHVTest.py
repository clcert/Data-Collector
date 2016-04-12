import unittest
from data.metadata import Metadata
from http.www_auth.DLinkDIHV import DLinkDIHV


class DLinkDIHVTest(unittest.TestCase):
    def test_one(self):
        data = {'header': {'www_authenticate': '"Basic realm=""DI-804HV"""'}}
        metadata = DLinkDIHV().process(data, Metadata())

        self.assertEqual(metadata.device.manufacturer, 'DLink')
        self.assertEqual(metadata.device.product, 'DI-804HV')
        self.assertEqual(metadata.device.type, 'DSL Modem')


if __name__ == '__main__':
    unittest.main()