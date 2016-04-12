import unittest
from data.metadata import Metadata
from http.www_auth.CiscoRV import CiscoRV


class CiscoRVTest(unittest.TestCase):
    def test_one(self):
        data = {'header': {'www_authenticate': '"Basic realm=""RV082"""'}}
        metadata = CiscoRV().process(data, Metadata())

        self.assertEqual(metadata.device.manufacturer, 'Cisco')
        self.assertEqual(metadata.device.product, 'RV082')
        self.assertEqual(metadata.device.type, 'VPN Router')


if __name__ == '__main__':
    unittest.main()