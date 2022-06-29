from typing import Union

from box import Box
from restfly.endpoint import APIEndpoint

from .exception import MandatoryFieldMissing
from pycheckpoint.utils import sanitize_value
from pycheckpoint.models import Color


class NetworkAPI(APIEndpoint):
    def add_host(
        self,
        name: str,
        ip_address: str = None,
        ipv4_address: str = None,
        ipv6_address: str = None,
        interfaces: Union[dict, list[dict]] = None,
        nat_settings: dict = None,
        tags: Union[str, list[str]] = None,
        host_servers: dict = None,
        **kw
    ) -> Box:
        """
        Create new object.

        Args:
            name (str): Object name. Must be unique in the domain.
            ip_address (str): 	IPv4 or IPv6 address. If both addresses are required use ipv4-address
            and ipv6-address fields explicitly. Mandatory if "ipv4_address" or "ipv6_address" is not set
            ipv4_address (str): IPv4 address. Mandatory if "ipv_address" or "ipv6_address" is not set
            ipv6_address (str): IPv6 address. Mandatory if "ipv_address" or "ipv4_address" is not set
            interfaces (Union[dict,list[dict]]): Host interfaces.
            nat_settings (dict): NAT settings.
            tags (Union(str,list[str])): Collection of tag identifiers.
            host_servers (dict): Servers Configuration.
        Keyword Args:
            **set-if-exists (bool, optional):
                If another object with the same identifier already exists, it will be updated.
                The command behaviour will be the same as if originally a set command was called.
                Pay attention that original object's fields will be overwritten by the fields provided in the request payload!
            **color (Color, optional):
                Color of the object. Should be one of existing colors.
            **comments (str, optional):
                Comments string.
            **details-level (str, optional):
                The level of detail for some of the fields in the response can vary from showing only the UID value
                of the object to a fully detailed representation of the object.
            **groups (Union(str,list[str])):
                Collection of group identifiers.
            ** ignore-warnings (bool, optional):
                Apply changes ignoring warnings. Default is False
            ** ignore-errors (bool, optional):
                Apply changes ignoring errors. You won't be able to publish such a changes.
                If ignore-warnings flag was omitted - warnings will also be ignored. Default is False
        Returns:
            :obj:`Box`: The authenticated session information.
        Examples:
            >>> firewallManagementApi.session.create(username='admin@example.com',
            ...    password='MyInsecurePassword')
        """

        # Main request parameters
        payload = {"name": name}
        if ip_address is not None:
            payload["ip-address"] = ip_address
        elif ipv4_address is not None:
            payload["ipv4-address"] = ipv4_address
        elif ipv6_address is not None:
            payload["ipv6-address"] = ipv6_address
        else:
            raise MandatoryFieldMissing("ip_address or ipv4_address or ipv6_address")

        if interfaces is not None:
            payload["interfaces"] = interfaces
        if nat_settings is not None:
            payload["nat-settings"] = nat_settings
        if tags is not None:
            payload["tags"] = tags
        if host_servers is not None:
            payload["host-servers"] = host_servers

        # Secondary parameters
        secondary_parameters = {
            "set-if-exists": bool,
            "color": Color,
            "comments": str,
            "details-level": str,
            "groups": Union[str, list[str]],
            "ignore-warnings": bool,
            "ignore-errors": bool,
        }
        for field, type in secondary_parameters.items():
            value = sanitize_value(field=field, t=type, is_mandatory=False, **kw)
            if value is not None:
                payload[field] = value

        return self._post("add-host", json=payload)
