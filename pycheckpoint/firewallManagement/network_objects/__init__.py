from restfly.endpoint import APIEndpoint

from .host import HostAPI
from .network import NetworkAPI


class NetworkObjects(APIEndpoint):
    @property
    def host(self):
        """The interface object for the Host Management."""
        return HostAPI(self)

    @property
    def network(self):
        """The interface object for the Network Management."""
        return NetworkAPI(self)
