import unittest

from data.metadata import Metadata
from ssh.banner.Dropbear import Dropbear


class MyTestCase(unittest.TestCase):
    def test_version_1(self):
        data = {'banner': 'SSH-2.0-dropbear_0.46'}
        metadata = Dropbear().process(data, Metadata())
        self.assertEqual(metadata.service.product, "Dropbear", "Wrong service product")
        self.assertEqual(metadata.service.version, "0.46", "Wrong service version")

    def test_version_2(self):
        data = {'banner': 'SSH-2.0-dropbear_2014.63'}
        metadata = Dropbear().process(data, Metadata())
        self.assertEqual(metadata.service.product, "Dropbear", "Wrong service product")
        self.assertEqual(metadata.service.version, "2014.63", "Wrong service version")


if __name__ == '__main__':
    unittest.main()
