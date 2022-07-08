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
from .time import TimeAPI
from .time_group import TimeGroupAPI
from .dynamic_object import DynamicObjectAPI
from .tag import TagAPI
from .dns_domain import DNSDomainAPI
from .opsec_application import OPSECApplicationAPI
from .lsv_profile import LSVProfileAPI
from .tacacs_server import TacacsServerAPI
from .tacacs_group import TacacsGroupAPI
from .access_point_name import AccessPointNameAPI
from .lsm_gateway import LSMGatewayAPI
from .lsm_cluster import LSMClusterAPI


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

    @property
    def time(self):
        """The interface object for the network objects type "Time" Management."""
        return TimeAPI(self)

    @property
    def time_group(self):
        """The interface object for the network objects type "Time Group" Management."""
        return TimeGroupAPI(self)

    @property
    def dynamic_object(self):
        """The interface object for the network objects type "Dynamic Object" Management."""
        return DynamicObjectAPI(self)

    @property
    def tag(self):
        """The interface object for the network objects type "Tag" Management."""
        return TagAPI(self)

    @property
    def dns_domain(self):
        """The interface object for the network objects type "DNS Domain" Management."""
        return DNSDomainAPI(self)

    @property
    def opsec_application(self):
        """The interface object for the network objects type "OPSEC Application" Management."""
        return OPSECApplicationAPI(self)

    @property
    def lsv_profile(self):
        """The interface object for the network objects type "LSV Profile" Management."""
        return LSVProfileAPI(self)

    @property
    def tacacs_server(self):
        """The interface object for the network objects type "TACACS Server" Management."""
        return TacacsServerAPI(self)

    @property
    def tacacs_group(self):
        """The interface object for the network objects type "TACACS Group" Management."""
        return TacacsGroupAPI(self)

    @property
    def access_point_name(self):
        """The interface object for the network objects type "Access Point Name" Management."""
        return AccessPointNameAPI(self)

    @property
    def lsm_gateway(self):
        """The interface object for the network objects type "LSM Gateway" Management."""
        return LSMGatewayAPI(self)

    @property
    def lsm_cluster(self):
        """The interface object for the network objects type "LSM Cluster" Management."""
        return LSMClusterAPI(self)
