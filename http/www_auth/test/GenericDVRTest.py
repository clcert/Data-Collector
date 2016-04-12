import unittest
from data.metadata import Metadata
from http.www_auth.GenericDVR import GenericDVR


class GenericDVRTest(unittest.TestCase):
    def test_one(self):
        data = {'header': {'www_authenticate': '"Basic realm=""DVR"""'}}
        metadata = GenericDVR().process(data, Metadata())

        self.assertEqual(metadata.device.type, 'DVR')


if __name__ == '__main__':
    unittest.main()