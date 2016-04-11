import unittest
from data.metadata import Metadata
from http.www_auth.Avigilon import Avigilon


class AvigilonTest(unittest.TestCase):
    def test_one(self):
        data = {'header': {'www_authenticate': '"Digest realm=""Avigilon-101506026692""'}}
        metadata = Avigilon().process(data, Metadata())

        self.assertEqual(metadata.device.manufacturer, 'Avigilon')


if __name__ == '__main__':
    unittest.main()