from restfly.endpoint import APIEndpoint

from .service_tcp import ServiceTCPAPI

class ServiceApplications(APIEndpoint):
    @property
    def service_tcp(self):
        """The interface object for the network objects type "Service TCP" Management."""
        return ServiceTCPAPI(self)
