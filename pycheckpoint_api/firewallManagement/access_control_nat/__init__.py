from restfly.endpoint import APIEndpoint

from .access_layer import AccessLayer
from .access_rule import AccessRule
from .access_section import AccessSection
from .nat_rule import NATRule
from .nat_section import NATSection


class AccessControlNAT(APIEndpoint):
    @property
    def access_rule(self) -> AccessRule:
        """The interface object for the objects type "Access Rule" Management.

        Returns:
            AccessRule: an Access Rule instance

        Examples:
            >>> firewall.access_control_nat.access_rule

        """
        return AccessRule(self)

    @property
    def access_section(self) -> AccessSection:
        """The interface object for the objects type "Access Section" Management.

        Returns:
            AccessSection: an Access Section instance

        Examples:
            >>> firewall.access_control_nat.access_section

        """
        return AccessSection(self)

    @property
    def access_layer(self) -> AccessLayer:
        """The interface object for the objects type "Access Layer" Management.

        Returns:
            AccessLayer: an Access Layer section

        Examples:
            >>> firewall.access_control_nat.access_layer

        """
        return AccessLayer(self)

    @property
    def nat_rule(self) -> NATRule:
        """The interface object for the objects type "NAT Rule" Management.

        Returns:
            NATRule: a NAT Rule instance

        Examples:
            >>> firewall.access_control_nat.nat_rule

        """
        return NATRule(self)

    @property
    def nat_section(self) -> NATSection:
        """The interface object for the objects type "NAT Section" Management.

        Returns:
            NATSection: a NAT Section instance

        Examples:
            >>> firewall.access_control_nat.nat_section

        """
        return NATSection(self)
