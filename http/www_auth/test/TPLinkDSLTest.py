import unittest
from data.metadata import Metadata
from http.www_auth.TPLinkDSL import TPLinkDSL


class TPLinkDSLTest(unittest.TestCase):
    def test_one(self):
        data = {'header': {'www_authenticate': '"Basic realm=""TP-LINK Router R860"""'}}
        metadata = TPLinkDSL().process(data, Metadata())

        self.assertEqual(metadata.device.manufacturer, 'TP-Link')
        self.assertEqual(metadata.device.product, 'R860')
        self.assertEqual(metadata.device.type, 'DSL Modem')


if __name__ == '__main__':
    unittest.main()