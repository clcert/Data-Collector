import json

__author__ = 'eduardo'


class Metadata(object):

    product = None
    version = None
    os = None
    os_version = None
    device_type = None

    def is_empty(self):
        """
        Verify if metadata is empty
        :return: boolean
        """
        return self.product is None

    def to_json(self):
        data_cleaned = dict((k, v) for k, v in self.__dict__.iteritems() if v)
        return json.dumps(data_cleaned)