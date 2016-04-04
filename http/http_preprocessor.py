class HTTPPreprocessor(object):
    @staticmethod
    def parse_headers(data):
        header = data.get('header')

        if header:
            parsed_header = dict()

            for key, value in header.iteritems():
                if key == "null":
                    parsed_header['status_code'] = HTTPPreprocessor.sanitize_header_value(value)
                    continue

                parsed_header[HTTPPreprocessor.sanitize_header_name(key)] = HTTPPreprocessor.sanitize_header_value(
                    value)

            data.pop('header', None)
            data['header'] = parsed_header

        return data

    @staticmethod
    def sanitize_header_name(header_name):
        return header_name.lower().replace('-', '_')

    @staticmethod
    def sanitize_header_value(header_value):
        return ' '.join(header_value).strip()
