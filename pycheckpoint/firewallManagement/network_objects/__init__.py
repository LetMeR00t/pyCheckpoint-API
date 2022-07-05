from restfly.endpoint import APIEndpoint

from .host import HostAPI
from .network import NetworkAPI
from .wildcard import WildcardAPI
from .group import GroupAPI
from .gsn_handover_group import GSNHandoverGroupAPI
from .address_range import AddressRangeAPI
from .multicast_address_range import MulticastAddressRangeAPI
from .group_with_exclusion import GroupWithExclusionAPI
from .simple_gateway import SimpleGatewayAPI
from .simple_cluster import SimpleClusterAPI
from .network_interface import NetworkInterfaceAPI
from .checkpoint_host import CheckpointHostAPI
from .security_zone import SecurityZoneAPI


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

    @property
    def address_range(self):
        """The interface object for the network objects type "Address Range" Management."""
        return AddressRangeAPI(self)

    @property
    def multicast_address_range(self):
        """The interface object for the network objects type "Multicast Address Range" Management."""
        return MulticastAddressRangeAPI(self)

    @property
    def group_with_exclusion(self):
        """The interface object for the network objects type "Group With Exclusion" Management."""
        return GroupWithExclusionAPI(self)

    @property
    def simple_gateway(self):
        """The interface object for the network objects type "Simple Gateway" Management."""
        return SimpleGatewayAPI(self)

    @property
    def simple_cluster(self):
        """The interface object for the network objects type "Simple Cluster" Management."""
        return SimpleClusterAPI(self)

    @property
    def network_interface(self):
        """The interface object for the network objects type "Network Interface" Management."""
        return NetworkInterfaceAPI(self)

    @property
    def checkpoint_host(self):
        """The interface object for the network objects type "Checkpoint Host" Management."""
        return CheckpointHostAPI(self)

    @property
    def security_zone(self):
        """The interface object for the network objects type "Security Zone" Management."""
        return SecurityZoneAPI(self)
