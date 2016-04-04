import unittest

from data.metadata import Metadata
from ssh.banner.OpenSSH import OpenSSH


class OpenSSHTest(unittest.TestCase):

    def test_simple(self):
        data = {'banner': 'SSH-2.0-OpenSSH_4.3'}
        metadata = OpenSSH().process(data, Metadata())
        self.assertEqual(metadata.service.product, "OpenSSH", "Wrong service product")
        self.assertEqual(metadata.service.version, "4.3", "Wrong service version")

    def test_packet_name(self):
        data = {'banner': 'SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2'}
        metadata = OpenSSH().process(data, Metadata())
        self.assertEqual(metadata.service.product, "OpenSSH", "Wrong service product")
        self.assertEqual(metadata.service.version, "6.6.1p1", "Wrong service version")

if __name__ == '__main__':
    unittest.main()
