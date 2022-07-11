from restfly.endpoint import APIEndpoint

from .service_tcp import ServiceTCPAPI
from .service_udp import ServiceUDPAPI
from .service_icmp import ServiceICMPAPI
from .service_icmp6 import ServiceICMP6API
from .service_sctp import ServiceSCTPAPI
from .service_other import ServiceOtherAPI
from .service_group import ServiceGroupAPI
from .application_site import ApplicationSiteAPI


class ServiceApplications(APIEndpoint):
    @property
    def service_tcp(self):
        """The interface object for the network objects type "Service TCP" Management."""
        return ServiceTCPAPI(self)

    @property
    def service_udp(self):
        """The interface object for the network objects type "Service UDP" Management."""
        return ServiceUDPAPI(self)

    @property
    def service_icmp(self):
        """The interface object for the network objects type "Service ICMP" Management."""
        return ServiceICMPAPI(self)

    @property
    def service_icmp6(self):
        """The interface object for the network objects type "Service ICMP6" Management."""
        return ServiceICMP6API(self)

    @property
    def service_sctp(self):
        """The interface object for the network objects type "Service SCTP" Management."""
        return ServiceSCTPAPI(self)

    @property
    def service_other(self):
        """The interface object for the network objects type "Service Other" Management."""
        return ServiceOtherAPI(self)

    @property
    def service_group(self):
        """The interface object for the network objects type "Service Group" Management."""
        return ServiceGroupAPI(self)

    @property
    def application_site(self):
        """The interface object for the network objects type "Service Group" Management."""
        return ApplicationSiteAPI(self)
