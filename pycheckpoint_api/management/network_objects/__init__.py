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
    def host(self) -> Host:
        """The interface object for the network objects type "Host" Management.

        Returns:
            Host: a Host instance

        Examples:
            >>> firewall.network_objects.host

        """
        return Host(self)

    @property
    def network(self) -> Network:
        """The interface object for the network objects type "Network" Management.

        Returns:
            Network: a Network instance

        Examples:
            >>> firewall.network_objects.network

        """
        return Network(self)

    @property
    def wildcard(self) -> Wildcard:
        """The interface object for the network objects type "Wildcard" Management.

        Returns:
            Wildcard: a Wildcard instance

        Examples:
            >>> firewall.network_objects.wildcard

        """
        return Wildcard(self)

    @property
    def group(self) -> Group:
        """The interface object for the network objects type "Group" Management.

        Returns:
            Group: a Group instance

        Examples:
            >>> firewall.network_objects.group

        """
        return Group(self)

    @property
    def gsn_handover_group(self) -> GSNHandoverGroup:
        """The interface object for the network objects type "GSN Handover Group" Management."

        Returns:
            GSNHandoverGroup: a GSN Handover Group instance

        Examples:
            >>> firewall.network_objects.gsn_handover_group

        """
        return GSNHandoverGroup(self)

    @property
    def address_range(self) -> AddressRange:
        """The interface object for the network objects type "Address Range" Management.

        Returns:
            AddressRange: an Address Range instance

        Examples:
            >>> firewall.network_objects.address_range

        """
        return AddressRange(self)

    @property
    def multicast_address_range(self) -> MulticastAddressRange:
        """The interface object for the network objects type "Multicast Address Range" Management.

        Returns:
            MulticastAddressRange: a Multicast Address Range instance

        Examples:
            >>> firewall.network_objects.multicast_address_range

        """
        return MulticastAddressRange(self)

    @property
    def group_with_exclusion(self) -> GroupWithExclusion:
        """The interface object for the network objects type "Group With Exclusion" Management.

        Returns:
            GroupWithExclusion: a Group With Exclusion instance

        Examples:
            >>> firewall.network_objects.group_with_exclusion

        """
        return GroupWithExclusion(self)

    @property
    def simple_gateway(self) -> SimpleGateway:
        """The interface object for the network objects type "Simple Gateway" Management.

        Returns:
            SimpleGateway: a Simple Gateway instance

        Examples:
            >>> firewall.network_objects.simple_gateway

        """
        return SimpleGateway(self)

    @property
    def simple_cluster(self) -> SimpleCluster:
        """The interface object for the network objects type "Simple Cluster" Management.

        Returns:
            SimpleCluster: a Simple Cluster instance

        Examples:
            >>> firewall.network_objects.simple_cluster

        """
        return SimpleCluster(self)

    @property
    def network_interface(self) -> NetworkInterface:
        """The interface object for the network objects type "Network Interface" Management.

        Returns:
            NetworkInterface: a Network Interface instance

        Examples:
            >>> firewall.network_objects.network_instance

        """
        return NetworkInterface(self)

    @property
    def checkpoint_host(self) -> CheckpointHost:
        """The interface object for the network objects type "Checkpoint Host" Management.

        Returns:
            CheckpointHost: a Checkpoint Host instance

        Examples:
            >>> firewall.network_objects.checkpoint_host

        """
        return CheckpointHost(self)

    @property
    def security_zone(self) -> SecurityZone:
        """The interface object for the network objects type "Security Zone" Management.

        Returns:
            SecurityZone: a Security Zone instance

        Examples:
            >>> firewall.network_objects.security_zone

        """
        return SecurityZone(self)

    @property
    def time(self) -> Time:
        """The interface object for the network objects type "Time" Management.

        Returns:
            Time: a Time instance

        Examples:
            >>> firewall.network_objects.time

        """
        return Time(self)

    @property
    def time_group(self) -> TimeGroup:
        """The interface object for the network objects type "Time Group" Management.

        Returns:
            TimeGroup: a Time Group instance

        Examples:
            >>> firewall.network_objects.time_group

        """
        return TimeGroup(self)

    @property
    def dynamic_object(self) -> DynamicObject:
        """The interface object for the network objects type "Dynamic Object" Management.

        Returns:
            DynamicObject: a Dynamic Object instance

        Examples:
            >>> firewall.network_objects.dynamic_object

        """
        return DynamicObject(self)

    @property
    def tag(self) -> Tag:
        """The interface object for the network objects type "Tag" Management.

        Returns:
            Tag: a Tag instance

        Examples:
            >>> firewall.network_objects.tag

        """
        return Tag(self)

    @property
    def dns_domain(self) -> DNSDomain:
        """The interface object for the network objects type "DNS Domain" Management.

        Returns:
            DNSDomain: a DNS Domain instance

        Examples:
            >>> firewall.network_objects.dns_domain

        """
        return DNSDomain(self)

    @property
    def opsec_application(self) -> OPSECApplication:
        """The interface object for the network objects type "OPSEC Application" Management.

        Returns:
            OPSECApplication: an OPSEC Application instance

        Examples:
            >>> firewall.network_objects.opsec_application

        """
        return OPSECApplication(self)

    @property
    def lsv_profile(self) -> LSVProfile:
        """The interface object for the network objects type "LSV Profile" Management.

        Returns:
            LSVProfile: a LSV Profile instance

        Examples:
            >>> firewall.network_objects.lsv_profile

        """
        return LSVProfile(self)

    @property
    def tacacs_server(self) -> TacacsServer:
        """The interface object for the network objects type "TACACS Server" Management.

        Returns:
            TacacsServer: a TACACS Server instance

        Examples:
            >>> firewall.network_objects.tacacs_server

        """
        return TacacsServer(self)

    @property
    def tacacs_group(self) -> TacacsGroup:
        """The interface object for the network objects type "TACACS Group" Management.

        Returns:
            TacacsGroup: a TACACS Group instance

        Examples:
            >>> firewall.network_objects.tacacs_group

        """
        return TacacsGroup(self)

    @property
    def access_point_name(self) -> AccessPointName:
        """The interface object for the network objects type "Access Point Name" Management.

        Returns:
            AccessPointName: an Access Point Name instance

        Examples:
            >>> firewall.network_objects.access_point_name

        """
        return AccessPointName(self)

    @property
    def lsm_gateway(self) -> LSMGateway:
        """The interface object for the network objects type "LSM Gateway" Management.

        Returns:
            LSMGateway: a LSM Gateway instance

        Examples:
            >>> firewall.network_objects.lsm_gateway

        """
        return LSMGateway(self)

    @property
    def lsm_cluster(self) -> LSMCluster:
        """The interface object for the network objects type "LSM Cluster" Management.

        Returns:
            LSMCluster: a LSM Cluster instance

        Examples:
            >>> firewall.network_objects.lsm_cluster

        """
        return LSMCluster(self)
