from typing import Union

from box import Box
from restfly.endpoint import APIEndpoint

from .exception import MandatoryFieldMissing
from pycheckpoint.utils import sanitize_secondary_parameters
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
            **ignore-warnings (bool, optional):
                Apply changes ignoring warnings. Default is False
            **ignore-errors (bool, optional):
                Apply changes ignoring errors. You won't be able to publish such a changes.
                If ignore-warnings flag was omitted - warnings will also be ignored. Default is False
        Returns:
            :obj:`Box`: The response from the server
        Examples:
            >>> firewallManagementApi.network.add_host(name="My object")
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
        payload.update(sanitize_secondary_parameters(secondary_parameters, **kw))

        return self._post("add-host", json=payload)

    def show_host(self, uid: str = None, name: str = None, **kw) -> Box:
        """
        Retrieve existing object using object name or uid.

        Args:
            uid (str): Object unique identifier.
            name (str): Object name.
        Keyword Args:
            **details-level (str, optional):
                The level of detail for some of the fields in the response can vary from showing only the UID value
                of the object to a fully detailed representation of the object.
        Returns:
            :obj:`Box`: The response from the server
        Examples:
            >>> firewallManagementApi.network.show_host(uid="9423d36f-2d66-4754-b9e2-e7f4493756d4")
        """

        # Main request parameters
        payload = {}
        if uid is not None:
            payload["uid"] = uid
        elif name is not None:
            payload["name"] = name
        else:
            raise MandatoryFieldMissing("uid or name")

        # Secondary parameters
        secondary_parameters = {"details-level": str}
        payload.update(sanitize_secondary_parameters(secondary_parameters, **kw))

        return self._post("show-host", json=payload)

    def set_host(
        self,
        uid: str = None,
        name: str = None,
        ip_address: str = None,
        ipv4_address: str = None,
        ipv6_address: str = None,
        interfaces: Union[dict, list[dict]] = None,
        nat_settings: dict = None,
        new_name: str = None,
        tags: Union[str, list[str]] = None,
        host_servers: dict = None,
        **kw
    ) -> Box:
        """
        Edit existing object using object name or uid.

        Args:
            uid (str): Object unique identifier.
            name (str): Object name.
            ip_address (str): 	IPv4 or IPv6 address. If both addresses are required use ipv4-address
            and ipv6-address fields explicitly. Mandatory if "ipv4_address" or "ipv6_address" is not set
            ipv4_address (str): IPv4 address. Mandatory if "ipv_address" or "ipv6_address" is not set
            ipv6_address (str): IPv6 address. Mandatory if "ipv_address" or "ipv4_address" is not set
            interfaces (Union[dict,list[dict]]): Host interfaces.
            nat_settings (dict): NAT settings.
            new_name (str): New name of the object.
            tags (Union(str,list[str])): Collection of tag identifiers.
            host_servers (dict): Servers Configuration.
        Keyword Args:
            **color (Color, optional):
                Color of the object. Should be one of existing colors.
            **comments (str, optional):
                Comments string.
            **details-level (str, optional):
                The level of detail for some of the fields in the response can vary from showing only the UID value
                of the object to a fully detailed representation of the object.
            **groups (Union(str,list[str])):
                Collection of group identifiers.
            **ignore-warnings (bool, optional):
                Apply changes ignoring warnings. Default is False
            **ignore-errors (bool, optional):
                Apply changes ignoring errors. You won't be able to publish such a changes.
                If ignore-warnings flag was omitted - warnings will also be ignored. Default is False
        Returns:
            :obj:`Box`: The response from the server
        Examples:
            >>> firewallManagementApi.network.add_host(name="My object")
        """

        # Main request parameters
        payload = {}
        if uid is not None:
            payload["uid"] = uid
        elif name is not None:
            payload["name"] = name
        else:
            raise MandatoryFieldMissing("uid or name")

        if ip_address is not None:
            payload["ip-address"] = ip_address
        elif ipv4_address is not None:
            payload["ipv4-address"] = ipv4_address
        elif ipv6_address is not None:
            payload["ipv6-address"] = ipv6_address

        if interfaces is not None:
            payload["interfaces"] = interfaces
        if nat_settings is not None:
            payload["nat-settings"] = nat_settings
        if new_name is not None:
            payload["new-name"] = new_name
        if tags is not None:
            payload["tags"] = tags
        if host_servers is not None:
            payload["host-servers"] = host_servers

        # Secondary parameters
        secondary_parameters = {
            "color": Color,
            "comments": str,
            "details-level": str,
            "groups": Union[str, list[str]],
            "ignore-warnings": bool,
            "ignore-errors": bool,
        }
        payload.update(sanitize_secondary_parameters(secondary_parameters, **kw))

        return self._post("set-host", json=payload)

    def delete_host(self, uid: str = None, name: str = None, **kw) -> Box:
        """
        Delete existing object using object name or uid.

        Args:
            uid (str): Object unique identifier.
            name (str): Object name.
        Keyword Args:
            **details-level (str, optional):
                The level of detail for some of the fields in the response can vary from showing only the UID value
                of the object to a fully detailed representation of the object.
            **ignore-warnings (bool, optional):
                Apply changes ignoring warnings. Default is False
            **ignore-errors (bool, optional):
                Apply changes ignoring errors. You won't be able to publish such a changes.
                If ignore-warnings flag was omitted - warnings will also be ignored. Default is False
        Returns:
            :obj:`Box`: The response from the server
        Examples:
            >>> firewallManagementApi.network.delete_host(uid="9423d36f-2d66-4754-b9e2-e7f4493756d4")
        """

        # Main request parameters
        payload = {}
        if uid is not None:
            payload["uid"] = uid
        elif name is not None:
            payload["name"] = name
        else:
            raise MandatoryFieldMissing("uid or name")

        # Secondary parameters
        secondary_parameters = {
            "details-level": str,
            "ignore-warnings": bool,
            "ignore-errors": bool,
        }
        payload.update(sanitize_secondary_parameters(secondary_parameters, **kw))

        return self._post("delete-host", json=payload)

    def show_hosts(
        self,
        filter: str = None,
        limit: int = 50,
        offset: int = 0,
        order: list[dict] = None,
        **kw
    ) -> Box:
        """
        Retrieve all objects.

        Args:
            filter (str): Search expression to filter objects by.
            The provided text should be exactly the same as it would be given in SmartConsole Object Explorer.
            The logical operators in the expression ('AND', 'OR') should be provided in capital letters.
            he search involves both a IP search and a textual search in name, comment, tags etc.
            limit (int): The maximal number of returned results. Default to 50 (between 1 and 500)
            offset (int): Number of the results to initially skip. Default to 0
            order (list[dict]): Sorts results by the given field. By default the results are sorted in the
            descending order by the session publish time.
        Returns:
            :obj:`Box`: The response from the server
        Examples:
            >>> firewallManagementApi.network.shows_hosts()
        """

        # Main request parameters
        payload = {}
        if filter is not None:
            payload["filter"] = filter
        if limit is not None:
            payload["limit"] = limit
        if offset is not None:
            payload["offset"] = offset
        if order is not None:
            payload["order"] = order

        # Secondary parameters
        secondary_parameters = {
            "show-membership": bool,
            "details-level": str,
            "domains-to-process": list[str],
        }
        payload.update(sanitize_secondary_parameters(secondary_parameters, **kw))

        return self._post("show-hosts", json=payload)

    def add_network(
        self,
        name: str,
        subnet: str = None,
        subnet4: str = None,
        subnet6: str = None,
        mask_length: str = None,
        mask_length4: str = None,
        mask_length6: str = None,
        subnet_mask: str = None,
        nat_settings: dict = None,
        tags: Union[str, list[str]] = None,
        broadcast: str = None,
        **kw
    ) -> Box:
        """
        Create new object.

        Args:
            name (str): Object name. Must be unique in the domain.
            subnet (str): IPv4 or IPv6 network address. If both addresses are required use subnet4 and
             subnet6 fields explicitly. Mandatory if "subnet4" or "subnet6" is not set
            subnet4 (str): IPv4 network address. Mandatory if "subnet" or "subnet6" is not set
            subnet6 (str): IPv6 network address. Mandatory if "subnet" or "subnet4" is not set
            mask_length (int): IPv4 or IPv6 network mask length. If both masks are required use mask-length4
            and mask-length6 fields explicitly. Instead of IPv4 mask length it is possible to specify IPv4
            mask itself in subnet-mask field. Mandatory if "mask_length4" or "mask_length6" or "subnet_mask" is not set
            mask_length4 (int): IPv4 network mask length.
            Mandatory if "mask_length" or "mask_length4" or "subnet_mask" is not set
            mask_length6 (int): IPv6 network mask length.
            Mandatory if "mask_length" or "mask_length6" or "subnet_mask" is not set
            subnet_mask (str): IPv4 network mask. Mandatory if "mask_length" or "mask_length4" or "mask_length6" is not set
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
            **ignore-warnings (bool, optional):
                Apply changes ignoring warnings. Default is False
            **ignore-errors (bool, optional):
                Apply changes ignoring errors. You won't be able to publish such a changes.
                If ignore-warnings flag was omitted - warnings will also be ignored. Default is False
        Returns:
            :obj:`Box`: The response from the server
        Examples:
            >>> firewallManagementApi.network.add_network(name="My object")
        """

        # Main request parameters
        payload = {"name": name}
        if subnet is not None:
            payload["subnet"] = subnet
        elif subnet4 is not None:
            payload["subnet4"] = subnet4
        elif subnet6 is not None:
            payload["subnet6"] = subnet6
        else:
            raise MandatoryFieldMissing("subnet or subnet4 or subnet6")
        if mask_length is not None:
            payload["mask_length"] = mask_length
        elif mask_length4 is not None:
            payload["mask_length4"] = mask_length4
        elif mask_length6 is not None:
            payload["mask_length6"] = mask_length6
        elif subnet_mask is not None:
            payload["subnet_mask"] = subnet_mask
        else:
            raise MandatoryFieldMissing("mask_length or mask_length4 or mask_length6")

        if nat_settings is not None:
            payload["nat-settings"] = nat_settings
        if tags is not None:
            payload["tags"] = tags
        if broadcast is not None:
            payload["broadcast"] = broadcast

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
        payload.update(sanitize_secondary_parameters(secondary_parameters, **kw))

        return self._post("add-network", json=payload)
