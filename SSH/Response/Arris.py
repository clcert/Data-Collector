from SSH.SshProcess import SshProcess
import Data.Metadata


class Arris(SshProcess):
    """
    http://www.surfboard.com/
    """
    protocol = "SSH"
    subprotocol = "Banner"

    search = "arris"
    
    def process(self, data, metadata):
        """
        :type metadata: Metadata.Metadata
        :type data: dict
        """
        if SshProcess.get_response(data).lower().find(self.search) != -1:
            metadata.device.manufacturer = "Arris"
            metadata.device.type = "Cable Modem"
        return metadata

