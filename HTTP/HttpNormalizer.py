class HttpNormalizer(object):
    @staticmethod
    def normalize(data):
        new_data = dict()

        if 'ip' in data:
            new_data['ip'] = data['ip']

        if 'error' in data:
            new_data['error'] = data['error']

        if 'header' in data and len(data['header']) != 0:
            new_data['header'] = data['header']

        if 'index' in data:
            new_data['index'] = data['index']

        return new_data
