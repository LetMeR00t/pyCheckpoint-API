from restfly.endpoint import APIEndpoint

from .service_tcp import ServiceTCP
from .service_udp import ServiceUDP
from .service_icmp import ServiceICMP
from .service_icmp6 import ServiceICMP6
from .service_sctp import ServiceSCTP
from .service_other import ServiceOther
from .service_group import ServiceGroup
from .application_site import ApplicationSite
from .application_site_category import ApplicationSiteCategory
from .application_site_group import ApplicationSiteGroup
from .service_dce_rpc import ServiceDCERPC
from .service_rpc import ServiceRPC
from .service_gtp import ServiceGTP
from .service_citrix_tcp import ServiceCitrixTCP
from .service_compound_tcp import ServiceCompoundTCP


class ServiceApplications(APIEndpoint):
    @property
    def service_tcp(self):
        """The interface object for the network objects type "Service TCP" Management."""
        return ServiceTCP(self)

    @property
    def service_udp(self):
        """The interface object for the network objects type "Service UDP" Management."""
        return ServiceUDP(self)

    @property
    def service_icmp(self):
        """The interface object for the network objects type "Service ICMP" Management."""
        return ServiceICMP(self)

    @property
    def service_icmp6(self):
        """The interface object for the network objects type "Service ICMP6" Management."""
        return ServiceICMP6(self)

    @property
    def service_sctp(self):
        """The interface object for the network objects type "Service SCTP" Management."""
        return ServiceSCTP(self)

    @property
    def service_other(self):
        """The interface object for the network objects type "Service Other" Management."""
        return ServiceOther(self)

    @property
    def service_group(self):
        """The interface object for the network objects type "Service Group" Management."""
        return ServiceGroup(self)

    @property
    def application_site(self):
        """The interface object for the network objects type "Application Site" Management."""
        return ApplicationSite(self)

    @property
    def application_site_category(self):
        """The interface object for the network objects type "Application Site Category" Management."""
        return ApplicationSiteCategory(self)

    @property
    def application_site_group(self):
        """The interface object for the network objects type "Application Site Group" Management."""
        return ApplicationSiteGroup(self)

    @property
    def service_dce_rpc(self):
        """The interface object for the network objects type "Service DCE RPC" Management."""
        return ServiceDCERPC(self)

    @property
    def service_rpc(self):
        """The interface object for the network objects type "Service RPC" Management."""
        return ServiceRPC(self)

    @property
    def service_gtp(self):
        """The interface object for the network objects type "Service GTP" Management."""
        return ServiceGTP(self)

    @property
    def service_citrix_tcp(self):
        """The interface object for the network objects type "Service Citrix TCP" Management."""
        return ServiceCitrixTCP(self)

    @property
    def service_compound_tcp(self):
        """The interface object for the network objects type "Service Compound TCP" Management."""
        return ServiceCompoundTCP(self)
