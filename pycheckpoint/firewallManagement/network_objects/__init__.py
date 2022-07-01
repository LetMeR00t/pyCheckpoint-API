from restfly.endpoint import APIEndpoint

from .host import HostAPI
from .network import NetworkAPI
from .wildcard import WildcardAPI
from .group import GroupAPI


class NetworkObjects(APIEndpoint):
    @property
    def host(self):
        """The interface object for the network objects type "Host" Management."""
        return HostAPI(self)

    @property
    def network(self):
        """The interface object for the network objects type "Network" Management."""
        return NetworkAPI(self)

    @property
    def wildcard(self):
        """The interface object for the network objects type "Wildcard" Management."""
        return WildcardAPI(self)

    @property
    def group(self):
        """The interface object for the network objects type "Group" Management."""
        return GroupAPI(self)
