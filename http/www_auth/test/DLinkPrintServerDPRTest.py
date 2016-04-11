import unittest
from data.metadata import Metadata
from http.www_auth.DLinkPrintServerDPR import DLinkPrintServerDPR


class DLinkPrintServerDPRTest(unittest.TestCase):
    def test_one(self):
        data = {'header': {'www_authenticate': '"BASIC realm=""DPR-1061"""'}}
        metadata = DLinkPrintServerDPR().process(data, Metadata())

        self.assertEqual(metadata.device.manufacturer, 'DLink')
        self.assertEqual(metadata.device.product, 'DPR-1061')
        self.assertEqual(metadata.device.type, 'Print Server')


if __name__ == '__main__':
    unittest.main()