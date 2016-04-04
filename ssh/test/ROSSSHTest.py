import unittest

from data.metadata import Metadata
from ssh.banner.ROSSSH import ROSSSH


class ROSSSHTest(unittest.TestCase):

    def test_simple(self):
        data = {'banner': 'SSH-2.0-ROSSSH'}
        metadata = ROSSSH().process(data, Metadata())
        self.assertEqual(metadata.device.os, "Router OS", "Wrong device os")
        self.assertEqual(metadata.device.type, "Router Board", "Wrong type product")


if __name__ == '__main__':
    unittest.main()



