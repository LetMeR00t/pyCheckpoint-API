from restfly.endpoint import APIEndpoint

from .access_rule import AccessRule


class AccessControlNAT(APIEndpoint):
    @property
    def access_rule(self):
        """The interface object for the objects type "Access Rule" Management."""
        return AccessRule(self)
