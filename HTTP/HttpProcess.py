__author__ = 'eduardo'


class HttpProcess(object):
    protocol = None
    subprotocol = None

    def get_header_field(self, data, field):
        header = data.get('header')

        if header:
            return header.get(field)

        return None

    @classmethod
    def all_subclasses(cls):
        return cls.__subclasses__() + [g for s in cls.__subclasses__()
                                       for g in s.all_subclasses()]
