from restfly.endpoint import APIEndpoint

from .application_site import ApplicationSite
from .application_site_category import ApplicationSiteCategory
from .application_site_group import ApplicationSiteGroup
from .service_citrix_tcp import ServiceCitrixTCP
from .service_compound_tcp import ServiceCompoundTCP
from .service_dce_rpc import ServiceDCERPC
from .service_group import ServiceGroup
from .service_gtp import ServiceGTP
from .service_icmp import ServiceICMP
from .service_icmp6 import ServiceICMP6
from .service_other import ServiceOther
from .service_rpc import ServiceRPC
from .service_sctp import ServiceSCTP
from .service_tcp import ServiceTCP
from .service_udp import ServiceUDP


class ServiceApplications(APIEndpoint):
    @property
    def service_tcp(self) -> ServiceTCP:
        """The interface object for the network objects type "Service TCP" Management.

        Returns:
            ServiceTCP: a Service TCP instance

        Examples:
            >>> firewall.service_applications.service_tcp

        """
        return ServiceTCP(self)

    @property
    def service_udp(self) -> ServiceUDP:
        """The interface object for the network objects type "Service UDP" Management.

        Returns:
            ServiceUDP: a Service UDP instance

        Examples:
            >>> firewall.service_applications.service_udp

        """
        return ServiceUDP(self)

    @property
    def service_icmp(self) -> ServiceICMP:
        """The interface object for the network objects type "Service ICMP" Management.

        Returns:
            ServiceICMP: a Service ICMP instance

        Examples:
            >>> firewall.service_applications.service_icmp

        """
        return ServiceICMP(self)

    @property
    def service_icmp6(self) -> ServiceICMP6:
        """The interface object for the network objects type "Service ICMP6" Management.

        Returns:
            ServiceICMP6: a Service ICMPv6 instance

        Examples:
            >>> firewall.service_applications.service_icmp6

        """
        return ServiceICMP6(self)

    @property
    def service_sctp(self) -> ServiceSCTP:
        """The interface object for the network objects type "Service SCTP" Management.

        Returns:
            ServiceSCTP: a Service SCTP instance

        Examples:
            >>> firewall.service_applications.service_sctp

        """
        return ServiceSCTP(self)

    @property
    def service_other(self) -> ServiceOther:
        """The interface object for the network objects type "Service Other" Management.

        Returns:
            ServiceOther: a Service Other instance

        Examples:
            >>> firewall.service_applications.service_other

        """
        return ServiceOther(self)

    @property
    def service_group(self) -> ServiceGroup:
        """The interface object for the network objects type "Service Group" Management.

        Returns:
            ServiceGroup: a Service Group instance

        Examples:
            >>> firewall.service_applications.service_group

        """
        return ServiceGroup(self)

    @property
    def application_site(self) -> ApplicationSite:
        """The interface object for the network objects type "Application Site" Management.

        Returns:
            ApplicationSite: an Application Site instance

        Examples:
            >>> firewall.service_applications.application_site

        """
        return ApplicationSite(self)

    @property
    def application_site_category(self) -> ApplicationSiteCategory:
        """The interface object for the network objects type "Application Site Category" Management.

        Returns:
            ApplicationSiteCategory: an Application Site Category instance

        Examples:
            >>> firewall.service_applications.application_site_category

        """
        return ApplicationSiteCategory(self)

    @property
    def application_site_group(self) -> ApplicationSiteGroup:
        """The interface object for the network objects type "Application Site Group" Management.

        Returns:
            ApplicationSiteGroup: an Application Site Group instance

        Examples:
            >>> firewall.service_applications.application_site_group

        """
        return ApplicationSiteGroup(self)

    @property
    def service_dce_rpc(self) -> ServiceDCERPC:
        """The interface object for the network objects type "Service DCE RPC" Management.

        Returns:
            ServiceDCERPC: a Service DCE RPC instance

        Examples:
            >>> firewall.service_applications.service_dce_rpc

        """
        return ServiceDCERPC(self)

    @property
    def service_rpc(self) -> ServiceRPC:
        """The interface object for the network objects type "Service RPC" Management.

        Returns:
            ServiceRPC: a Service RPC instance

        Examples:
            >>> firewall.service_applications.service_rpc

        """
        return ServiceRPC(self)

    @property
    def service_gtp(self) -> ServiceGTP:
        """The interface object for the network objects type "Service GTP" Management.

        Returns:
            ServiceGTP: a Service GTP instance

        Examples:
            >>> firewall.service_applications.service_gtp

        """
        return ServiceGTP(self)

    @property
    def service_citrix_tcp(self) -> ServiceCitrixTCP:
        """The interface object for the network objects type "Service Citrix TCP" Management.

        Returns:
            ServiceCitrixTCP: a Service Citrix TCP instance

        Examples:
            >>> firewall.service_applications.service_citrix_tcp

        """
        return ServiceCitrixTCP(self)

    @property
    def service_compound_tcp(self) -> ServiceCompoundTCP:
        """The interface object for the network objects type "Service Compound TCP" Management.

        Returns:
            ServiceCompoundTCP: a Service Compound TCP instance

        Examples:
            >>> firewall.service_applications.service_compound_tcp

        """
        return ServiceCompoundTCP(self)
