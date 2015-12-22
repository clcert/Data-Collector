from SSH.SshProcess import SshProcess
import Data.Metadata


class Cisco(SshProcess):
    protocol = "SSH"
    subprotocol = "Banner"

    search = "cisco"

    def process(self, data, metadata):
        """
        :type metadata: Data.Metadata
        :type data: dict
        """
        if SshProcess.get_response(data).lower().find(self.search) != -1:
            metadata.device.manufacturer = "Cisco"
        return metadata
