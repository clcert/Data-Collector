import unittest

from data.metadata import Metadata
from http.www_auth.TrendnetCamera import TrendnetCamera


class TrendnetCameraTest(unittest.TestCase):
    def test_one(self):
        data = {'header': {'www_authenticate': '"Digest realm=""TV-IP751WIC"",qop=""auth"", nonce=""999632fb9b8a934e5f96d56203513586"""'}}
        metadata = TrendnetCamera().process(data, Metadata())

        self.assertEqual(metadata.device.manufacturer, 'TRENDnet')
        self.assertEqual(metadata.device.type, 'Camera')
        self.assertEqual(metadata.device.product, 'TV-IP751WIC')

    def test_two(self):
        data = {'header': {'www_authenticate': '"Digest realm=""TV-IP751WC"",qop=""auth"", nonce=""8670d0480f06d668a0a8d594fe784969"""'}}
        metadata = TrendnetCamera().process(data, Metadata())

        self.assertEqual(metadata.device.manufacturer, 'TRENDnet')
        self.assertEqual(metadata.device.type, 'Camera')
        self.assertEqual(metadata.device.product, 'TV-IP751WC')

    def test_three(self):
        data = {'header': {'www_authenticate': '"Digest realm=""TV-IP551W"",qop=""auth"", nonce=""7aba7840d1b192d4cc74598e3d5ca223"""'}}
        metadata = TrendnetCamera().process(data, Metadata())

        self.assertEqual(metadata.device.manufacturer, 'TRENDnet')
        self.assertEqual(metadata.device.type, 'Camera')
        self.assertEqual(metadata.device.product, 'TV-IP551W')


if __name__ == '__main__':
    unittest.main()