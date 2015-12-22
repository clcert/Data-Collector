from SSH.SshProcess import SshProcess
import Data.Metadata


class ROSSSH(SshProcess):
    """
    http://www.mikrotik.com/software
    """

    protocol = "SSH"
    subprotocol = "Banner"

    search = "rosssh"

    def process(self, data, metadata):
        """
        :type metadata: Metadata.Metadata
        :type data: dict
        """
        if SshProcess.get_response(data).lower().find(self.search) != -1:
            metadata.device.manufacturer = "Mikrotik"
            metadata.device.os = "RouterOS"
            metadata.device.type = "Router"
        return metadata
