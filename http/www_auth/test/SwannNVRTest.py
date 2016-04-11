import unittest
from data.metadata import Metadata
from http.www_auth.SwannNVR import SwannNVR


class SwannNVRTest(unittest.TestCase):
    def test_one(self):
        data = {'header': {'www_authenticate': '"Basic realm=""NVR8"""'}}
        metadata = SwannNVR().process(data, Metadata())

        self.assertEqual(metadata.device.manufacturer, 'Swann')
        self.assertEqual(metadata.device.product, 'NVR8')
        self.assertEqual(metadata.device.type, 'DVR')


if __name__ == '__main__':
    unittest.main()