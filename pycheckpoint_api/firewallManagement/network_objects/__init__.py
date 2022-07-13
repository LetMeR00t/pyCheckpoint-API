from restfly.endpoint import APIEndpoint

from .access_point_name import AccessPointName
from .address_range import AddressRange
from .checkpoint_host import CheckpointHost
from .dns_domain import DNSDomain
from .dynamic_object import DynamicObject
from .group import Group
from .group_with_exclusion import GroupWithExclusion
from .gsn_handover_group import GSNHandoverGroup
from .host import Host
from .lsm_cluster import LSMCluster
from .lsm_gateway import LSMGateway
from .lsv_profile import LSVProfile
from .multicast_address_range import MulticastAddressRange
from .network import Network
from .network_interface import NetworkInterface
from .opsec_application import OPSECApplication
from .security_zone import SecurityZone
from .simple_cluster import SimpleCluster
from .simple_gateway import SimpleGateway
from .tacacs_group import TacacsGroup
from .tacacs_server import TacacsServer
from .tag import Tag
from .time import Time
from .time_group import TimeGroup
from .wildcard import Wildcard


class NetworkObjects(APIEndpoint):
    @property
    def host(self):
        """The interface object for the network objects type "Host" Management."""
        return Host(self)

    @property
    def network(self):
        """The interface object for the network objects type "Network" Management."""
        return Network(self)

    @property
    def wildcard(self):
        """The interface object for the network objects type "Wildcard" Management."""
        return Wildcard(self)

    @property
    def group(self):
        """The interface object for the network objects type "Group" Management."""
        return Group(self)

    @property
    def gsn_handover_group(self):
        """The interface object for the network objects type "GSN Handover Group" Management."""
        return GSNHandoverGroup(self)

    @property
    def address_range(self):
        """The interface object for the network objects type "Address Range" Management."""
        return AddressRange(self)

    @property
    def multicast_address_range(self):
        """The interface object for the network objects type "Multicast Address Range" Management."""
        return MulticastAddressRange(self)

    @property
    def group_with_exclusion(self):
        """The interface object for the network objects type "Group With Exclusion" Management."""
        return GroupWithExclusion(self)

    @property
    def simple_gateway(self):
        """The interface object for the network objects type "Simple Gateway" Management."""
        return SimpleGateway(self)

    @property
    def simple_cluster(self):
        """The interface object for the network objects type "Simple Cluster" Management."""
        return SimpleCluster(self)

    @property
    def network_interface(self):
        """The interface object for the network objects type "Network Interface" Management."""
        return NetworkInterface(self)

    @property
    def checkpoint_host(self):
        """The interface object for the network objects type "Checkpoint Host" Management."""
        return CheckpointHost(self)

    @property
    def security_zone(self):
        """The interface object for the network objects type "Security Zone" Management."""
        return SecurityZone(self)

    @property
    def time(self):
        """The interface object for the network objects type "Time" Management."""
        return Time(self)

    @property
    def time_group(self):
        """The interface object for the network objects type "Time Group" Management."""
        return TimeGroup(self)

    @property
    def dynamic_object(self):
        """The interface object for the network objects type "Dynamic Object" Management."""
        return DynamicObject(self)

    @property
    def tag(self):
        """The interface object for the network objects type "Tag" Management."""
        return Tag(self)

    @property
    def dns_domain(self):
        """The interface object for the network objects type "DNS Domain" Management."""
        return DNSDomain(self)

    @property
    def opsec_application(self):
        """The interface object for the network objects type "OPSEC Application" Management."""
        return OPSECApplication(self)

    @property
    def lsv_profile(self):
        """The interface object for the network objects type "LSV Profile" Management."""
        return LSVProfile(self)

    @property
    def tacacs_server(self):
        """The interface object for the network objects type "TACACS Server" Management."""
        return TacacsServer(self)

    @property
    def tacacs_group(self):
        """The interface object for the network objects type "TACACS Group" Management."""
        return TacacsGroup(self)

    @property
    def access_point_name(self):
        """The interface object for the network objects type "Access Point Name" Management."""
        return AccessPointName(self)

    @property
    def lsm_gateway(self):
        """The interface object for the network objects type "LSM Gateway" Management."""
        return LSMGateway(self)

    @property
    def lsm_cluster(self):
        """The interface object for the network objects type "LSM Cluster" Management."""
        return LSMCluster(self)
