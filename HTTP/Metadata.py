import json

__author__ = 'eduardo'


class ServiceMetadata(object):

    def __init__(self):
        self.manufacturer = None
        self.product = None
        self.version = None

    def is_empty(self):
        return not (self.manufacturer or self.product or self.version)


class DeviceMetadata(object):

    def __init__(self):
        self.manufacturer = None
        self.product = None
        self.os = None
        self.os_version = None
        self.type = None

    def is_empty(self):
        return not (self.manufacturer or self.product or self.os or self.os_version or self.type)

class Metadata(object):
    """
    :type service = ServiceMetadata
    :type device = DeviceMetadata
    """
    def __init__(self):
        self.service = ServiceMetadata()
        self.device = DeviceMetadata()

    def is_empty(self):
        """
        Verify if metadata is empty
        :return: boolean
        """
        return self.service.is_empty() and self.device.is_empty()

    def to_json(self):
        data_cleaned = dict((k, v) for k, v in self.__dict__.iteritems() if v)
        return json.dumps(data_cleaned)

