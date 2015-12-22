class SshProcess(object):
    protocol = None
    subprotocol = None

    @staticmethod
    def get_response(data):
        """
        :type data: dict
        """
        if 'response' in data:
            return data['response']
        raise Exception()