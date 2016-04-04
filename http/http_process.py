class HTTPProcess(object):

    def process(self, data, metadata):
        raise NotImplementedError("Abstract method")

    @staticmethod
    def get_header_field(data, field):
        header = data.get('header')

        if header:
            return header.get(field)

        return None

    @classmethod
    def all_subclasses(cls):
        return cls.__subclasses__() + [g for s in cls.__subclasses__()
                                       for g in s.all_subclasses()]
