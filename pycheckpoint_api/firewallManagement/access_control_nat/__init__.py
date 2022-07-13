from restfly.endpoint import APIEndpoint

from .access_rule import AccessRule
from .access_section import AccessSection
from .access_layer import AccessLayer


class AccessControlNAT(APIEndpoint):
    @property
    def access_rule(self):
        """The interface object for the objects type "Access Rule" Management."""
        return AccessRule(self)

    @property
    def access_section(self):
        """The interface object for the objects type "Access Section" Management."""
        return AccessSection(self)

    @property
    def access_layer(self):
        """The interface object for the objects type "Access Layer" Management."""
        return AccessLayer(self)
