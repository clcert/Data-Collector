import unittest

from data.metadata import Metadata
from ssh.banner.RomSShell import RomSShell


class RomSShellTest(unittest.TestCase):

    def test_simple(self):
        data = {'banner': 'SSH-2.0-RomSShell_4.31'}
        metadata = RomSShell().process(data, Metadata())
        self.assertEqual(metadata.service.product, "RomSShell", "Wrong service product")
        self.assertEqual(metadata.service.version, "4.31", "Wrong service version")
        self.assertEqual(metadata.service.manufacturer, "Allegro", "Wrong service manufacturer")


if __name__ == '__main__':
    unittest.main()