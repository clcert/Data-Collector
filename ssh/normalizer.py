class Normalizer(object):
    def __init__(self, data):
        super(Normalizer, self).__init__()
        self.data = data

    def process(self):
        self.__rename_fields()

        return self.data

    def __rename_fields(self):
        if 'response' in self.data:
            self.data['banner'] = self.data['response']
            self.data.pop('response', None)