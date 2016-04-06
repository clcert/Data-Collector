import unittest

from data.metadata import Metadata
from http.www_auth.DSLRouter import DSLRouter


class DSLRouterTest(unittest.TestCase):

    def test_dsl(self):
        data = {'header': {'www_authenticate': '"Basic realm=""DSL Router"""'}}
        metadata = DSLRouter().process(data, Metadata())

        self.assertEqual(metadata.device.type, 'DSL Modem')

    def test_adsl(self):
        data = {'header': {'www_authenticate': '"Basic realm=""ADSL Router"""'}}
        metadata = DSLRouter().process(data, Metadata())

        self.assertEqual(metadata.device.type, 'DSL Modem')


if __name__ == '__main__':
    unittest.main()
