class Normalizer(object):

    def __init__(self, data):
        self.data = data

    def normalize(self):
        new_data = dict()

        if 'ip' in self.data:
            new_data['ip'] = self.data['ip']

        if 'error' in self.data:
            new_data['error'] = self.data['error']

        if 'header' in self.data and len(self.data['header']) != 0:
            new_data['header'] = self.data['header']

        if 'index' in self.data:
            new_data['index'] = self.data['index']

        return new_data
