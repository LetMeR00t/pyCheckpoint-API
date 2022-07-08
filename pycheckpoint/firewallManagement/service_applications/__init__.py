from restfly.endpoint import APIEndpoint

from .service_tcp import ServiceTCPAPI
from .service_udp import ServiceUDPAPI


class ServiceApplications(APIEndpoint):
    @property
    def service_tcp(self):
        """The interface object for the network objects type "Service TCP" Management."""
        return ServiceTCPAPI(self)

    @property
    def service_udp(self):
        """The interface object for the network objects type "Service UDP" Management."""
        return ServiceUDPAPI(self)
