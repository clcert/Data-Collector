import unittest
from data.metadata import Metadata
from http.www_auth.GenericCamera import GenericCamera


class GenericCameraTest(unittest.TestCase):
    def test_one(self):
        data = {'header': {
            'www_authenticate': '"Basic realm=""Wireless IP Camera"""'}}
        metadata = GenericCamera().process(data, Metadata())

        self.assertEqual(metadata.device.type, 'Camera')

    def test_two(self):
        data = {'header': {
            'www_authenticate': '"Basic realm=""D5110 1.3M IR Dome Camera"""'}}
        metadata = GenericCamera().process(data, Metadata())

        self.assertEqual(metadata.device.type, 'Camera')


if __name__ == '__main__':
    unittest.main()