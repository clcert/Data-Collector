

class Juniper:

    def __init__(self):
        pass

    search = "ssh-2.0-netscreen"

    def test(self, data):
        """
        Test if the ssh server has the juniper backdoor
        :param data: SSH information
        :return:
        """
        if 'response' not in data:
            return False

        if data['response'].lower().find(self.search) != -1:
            return True
        return False

