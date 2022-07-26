from typing import List, Union

from box import Box

from pycheckpoint_api.models import Color
from pycheckpoint_api.utils import sanitize_secondary_parameters

from ..abstract.network_object import NetworkObject
from ..exception import MandatoryFieldMissing


class Host(NetworkObject):
    def add(
        self,
        name: str,
        ip_address: str = None,
        ipv4_address: str = None,
        ipv6_address: str = None,
        interfaces: Union[dict, List[dict]] = None,
        nat_settings: dict = None,
        tags: Union[str, List[str]] = None,
        host_servers: dict = None,
        **kw
    ) -> Box:
        """
        Create new object.

        Args:
            name (str): Object name. Must be unique in the domain.
            ip_address (str, optional): IPv4 or IPv6 address. If both addresses are required use ipv4-address\
            and ipv6-address fields explicitly. Mandatory if "ipv4_address" or "ipv6_address" is not set
            ipv4_address (str, optional): IPv4 address. Mandatory if "ipv_address" or "ipv6_address" is not set
            ipv6_address (str, optional): IPv6 address. Mandatory if "ipv_address" or "ipv4_address" is not set
            interfaces (Union[dict,List[dict]], optional): Host interfaces.
            nat_settings (dict, optional): NAT settings.
            tags (Union(str,List[str]), optional): Collection of tag identifiers.
            host_servers (dict, optional): Servers Configuration.

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
                The level of detail for some of the fields in the response can vary from showing only the UID value\
                of the object to a fully detailed representation of the object.
            **groups (Union(str,List[str]), optional):
                Collection of group identifiers.
            **ignore-warnings (bool, optional):
                Apply changes ignoring warnings. Defaults to False
            **ignore-errors (bool, optional):
                Apply changes ignoring errors. You won't be able to publish such a changes.
                If ignore-warnings flag was omitted - warnings will also be ignored. Defaults to False

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> firewall.network_objects.host.add(name="My object")
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
            "groups": Union[str, List[str]],
            "ignore-warnings": bool,
            "ignore-errors": bool,
        }
        payload.update(sanitize_secondary_parameters(secondary_parameters, **kw))

        return self._post("add-host", json=payload)

    def show(self, uid: str = None, name: str = None, **kw) -> Box:
        """
        Retrieve existing object using object name or uid.

        Args:
            uid (str, optional): Object unique identifier.
            name (str, optional): Object name.

        Keyword Args:
            **details-level (str, optional):
                The level of detail for some of the fields in the response can vary from showing only the UID value\
                of the object to a fully detailed representation of the object.

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> firewall.network_objects.host.show(uid="9423d36f-2d66-4754-b9e2-e7f4493756d4")
        """
        return self.show_object(endpoint="show-host", uid=uid, name=name, **kw)

    def set(
        self,
        uid: str = None,
        name: str = None,
        ip_address: str = None,
        ipv4_address: str = None,
        ipv6_address: str = None,
        interfaces: Union[dict, List[dict]] = None,
        nat_settings: dict = None,
        new_name: str = None,
        tags: Union[str, List[str]] = None,
        host_servers: dict = None,
        **kw
    ) -> Box:
        """
        Edit existing object using object name or uid.

        Args:
            uid (str, optional): Object unique identifier.
            name (str, optional): Object name.
            ip_address (str, optional): IPv4 or IPv6 address. If both addresses are required use ipv4-address\
            and ipv6-address fields explicitly. Mandatory if "ipv4_address" or "ipv6_address" is not set
            ipv4_address (str, optional): IPv4 address. Mandatory if "ipv_address" or "ipv6_address" is not set
            ipv6_address (str, optional): IPv6 address. Mandatory if "ipv_address" or "ipv4_address" is not set
            interfaces (Union[dict,List[dict]], optional): Host interfaces.
            nat_settings (dict, optional): NAT settings.
            new_name (str, optional): New name of the object.
            tags (Union(str,List[str]), optional): Collection of tag identifiers.
            host_servers (dict, optional): Servers Configuration.

        Keyword Args:
            **color (Color, optional):
                Color of the object. Should be one of existing colors.
            **comments (str, optional):
                Comments string.
            **details-level (str, optional):
                The level of detail for some of the fields in the response can vary from showing only the UID value\
                of the object to a fully detailed representation of the object.
            **groups (Union(str,List[str]), optional):
                Collection of group identifiers.
            **ignore-warnings (bool, optional):
                Apply changes ignoring warnings. Defaults to False
            **ignore-errors (bool, optional):
                Apply changes ignoring errors. You won't be able to publish such a changes.
                If ignore-warnings flag was omitted - warnings will also be ignored. Defaults to False

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> firewall.network_objects.host.set(uid="9423d36f-2d66-4754-b9e2-e7f4493756d4", ip_address="192.0.2.1")
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
            "groups": Union[str, List[str]],
            "ignore-warnings": bool,
            "ignore-errors": bool,
        }
        payload.update(sanitize_secondary_parameters(secondary_parameters, **kw))

        return self._post("set-host", json=payload)

    def delete(self, uid: str = None, name: str = None, **kw) -> Box:
        """
        Delete existing object using object name or uid.

        Args:
            uid (str, optional): Object unique identifier.
            name (str, optional): Object name.

        Keyword Args:
            **details-level (str, optional):
                The level of detail for some of the fields in the response can vary from showing only the UID value\
                of the object to a fully detailed representation of the object.
            **ignore-warnings (bool, optional):
                Apply changes ignoring warnings. Defaults to False
            **ignore-errors (bool, optional):
                Apply changes ignoring errors. You won't be able to publish such a changes.
                If ignore-warnings flag was omitted - warnings will also be ignored. Defaults to False

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> firewall.network_objects.host.delete(uid="9423d36f-2d66-4754-b9e2-e7f4493756d4")
        """
        return self.delete_object(endpoint="delete-host", uid=uid, name=name, **kw)

    def show_hosts(
        self,
        filter_results: str = None,
        limit: int = 50,
        offset: int = 0,
        order: List[dict] = None,
        **kw
    ) -> Box:
        """
        Retrieve all objects.

        Args:
            filter_results (str, optional): Search expression to filter objects by.\
            The provided text should be exactly the same as it would be given in SmartConsole Object Explorer.\
            The logical operators in the expression ('AND', 'OR') should be provided in capital letters.\
            he search involves both a IP search and a textual search in name, comment, tags etc.
            limit (int, optional): The maximal number of returned results. Defaults to 50 (between 1 and 500)
            offset (int, optional): Number of the results to initially skip. Defaults to 0
            order (List[dict], optional): Sorts results by the given field. By default the results are sorted in the \
            descending order by the session publish time.

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> firewall.network_objects.host.shows_hosts()
        """
        return self.show_objects(
            endpoint="show-hosts",
            filter_results=filter_results,
            limit=limit,
            offset=offset,
            order=order,
            extra_secondary_parameters={"show-membership": bool},
            **kw
        )
