from SSH.SshProcess import SshProcess
import Data.Metadata


class Juniper(SshProcess):

    search = "ssh-2.0-netscreen"

    def test_juniper(self, data):
        """
        Test if the ssh server has the juniper backdoor
        :param data: SSH information
        :return:
        """
        if 'response' not in data:
            raise Exception()

        if data['response'].lower().find(self.search) != -1:
            return True
        return False

