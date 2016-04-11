import unittest
from data.metadata import Metadata
from http.www_auth.WestermoIndustrialRouter import WestermoIndustrialRouter


class WestermoIndustrialRouterTest(unittest.TestCase):
    def test_one(self):
        data = {'header': {'www_authenticate': '"Basic realm=""Westermo MRD-355"""'}}
        metadata = WestermoIndustrialRouter().process(data, Metadata())

        self.assertEqual(metadata.device.manufacturer, 'Westermo')
        self.assertEqual(metadata.device.product, 'MRD-355')
        self.assertEqual(metadata.device.type, 'Industrial Router')


if __name__ == '__main__':
    unittest.main()