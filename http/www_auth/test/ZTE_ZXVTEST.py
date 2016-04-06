import unittest

from data.metadata import Metadata
from http.www_auth.Netgear import Netgear


class ZTE_ZXVTest(unittest.TestCase):
    def test(self):
        data = {'header': {'www_authenticate': '"Basic realm=""ZXV10 W300"""'}}
        metadata = Netgear().process(data, Metadata())

        self.assertEqual(metadata.device.manufacturer, 'ZTE')
        self.assertEqual(metadata.device.type, 'DSL Modem')
        self.assertEqual(metadata.device.product, 'ZXV10 W300')



if __name__ == '__main__':
    unittest.main()
