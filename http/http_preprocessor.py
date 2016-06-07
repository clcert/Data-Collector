from http.javascript import Javascript


class HTTPPreprocessor(object):
    @staticmethod
    def preprocess(data):

        if 'header' in data:
            data['raw_header'] = data.get('header')
            data.pop('header', None)

        if 'index' in data:
            data['raw_index'] = data.get('index')
            data.pop('index', None)

        data = HTTPPreprocessor.parse_headers(data)
        data = HTTPPreprocessor.parse_index(data)

        return data

    @staticmethod
    def parse_headers(data):
        header = data.get('raw_header')

        if header:
            parsed_header = dict()

            for key, value in header.iteritems():
                if key == "null":
                    data['status'] = HTTPPreprocessor.sanitize_header_value(value)
                    parsed_header['status_code'] = HTTPPreprocessor.sanitize_header_value(value)
                    continue

                parsed_header[HTTPPreprocessor.sanitize_header_name(key)] = HTTPPreprocessor.sanitize_header_value(
                    value)

            data['parse_header'] = parsed_header

        return data

    @staticmethod
    def parse_index(data):
        index = data.get('raw_index')
        if index is None:
            return data

        javascript = Javascript().parse(index)
        if javascript is not None:
            data['parse_index'] = {'javascripts': javascript}

        return data

    @staticmethod
    def sanitize_header_name(header_name):
        return header_name.lower().replace('-', '_')

    @staticmethod
    def sanitize_header_value(header_value):
        return ' '.join(header_value).strip()
