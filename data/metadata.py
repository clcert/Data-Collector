__author__ = 'eduardo'


class ServiceMetadata(object):

    def __init__(self):
        self.manufacturer = None
        self.product = None
        self.version = None

    def is_empty(self):
        return not (self.manufacturer or self.product or self.version)

    def to_dict(self):
        if self.is_empty():
            return None
        return dict((k, v) for k, v in self.__dict__.iteritems() if v)

    def merge(self, service):
        if self.manufacturer is None and service.manufacturer is not None:
            self.manufacturer = service.manufacturer

        if self.product is None and service.product is not None:
            self.product = service.product

        if self.version is None and service.version is not None:
            self.version = service.version


class DeviceMetadata(object):

    def __init__(self):
        self.manufacturer = None
        self.product = None
        self.os = None
        self.os_version = None
        self.type = None

    def is_empty(self):
        return not (self.manufacturer or self.product or self.os or self.os_version or self.type)

    def to_dict(self):
        if self.is_empty():
            return None
        return dict((k, v) for k, v in self.__dict__.iteritems() if v)

    def merge(self, device):
        if self.manufacturer is None and device.manufacturer is not None:
            self.manufacturer = device.manufacturer

        if self.product is None and device.product is not None:
            self.product = device.product

        if self.os is None and device.os is not None:
            self.os = device.os

        if self.os_version is None and device.os_version is not None:
            self.os_version = device.os_version

        if self.type is None and device.type is not None:
            self.type = device.type


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

    def to_dict(self):
        return {'service': self.service.to_dict(), 'device': self.device.to_dict()}

    def merge(self, metadata):
        self.service.merge(metadata.service)
        self.device.merge(metadata.device)

