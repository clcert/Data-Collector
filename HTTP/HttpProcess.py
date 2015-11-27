__author__ = 'eduardo'


class HttpProcess(object):
    protocol = None
    subprotocol = None

    @staticmethod
    def getServer(data):
        """
        Get the server from the header of http
        :param data: dict
        :return: dict
        """
        if 'header' in data and 'Server' in data['header']:
            return ' '.join(data['header']['Server'])
        raise Exception()

    @staticmethod
    def parse_header(data):
        """
        Parse important values of the header
        :param data: dict
        :return: dict
        """
        if 'header' in data:
            header = data['header']
            if 'Server' in header:
                data['server'] = ' '.join(data['header']['Server'])
            if 'null' in header:
                data['response'] = ' '.join(data['header']['null'])
            if 'Content-type' in header:
                data['content-type'] = ' '.join(data['header']['Content-type'])
            if 'WWW-Authenticate' in header:
                data['www-authenticate'] = ' '.join(data['header']['WWW-Authenticate'])
        return data

    @classmethod
    def all_subclasses(cls):
        return cls.__subclasses__() + [g for s in cls.__subclasses__()
                                       for g in s.all_subclasses()]
