import unittest
from data.metadata import Metadata
from http.www_auth.CodonicsHorizon import CodonicsHorizon


class CodonicsHorizonTest(unittest.TestCase):
    def test_one(self):
        data = {'header': {'www_authenticate': 'codonics-horizon-imager'}}
        metadata = CodonicsHorizon().process(data, Metadata())

        self.assertEqual(metadata.device.manufacturer, 'Codonics')
        self.assertEqual(metadata.device.type, 'Printer')


if __name__ == '__main__':
    unittest.main()