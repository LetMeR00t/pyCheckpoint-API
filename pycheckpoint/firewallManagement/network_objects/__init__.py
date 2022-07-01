from restfly.endpoint import APIEndpoint

from .host import HostAPI
from .network import NetworkAPI
from .wildcard import WildcardAPI
from .group import GroupAPI
from .gsn_handover_group import GSNHandoverGroupAPI


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

    @property
    def gsn_handover_group(self):
        """The interface object for the network objects type "GSN Handover Group" Management."""
        return GSNHandoverGroupAPI(self)
