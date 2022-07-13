from typing import Union, List

from box import Box

from ..abstract.network_object import NetworkObject
from ..exception import MandatoryFieldMissing
from pycheckpoint_api.utils import sanitize_secondary_parameters
from pycheckpoint_api.models import Color


class MulticastAddressRange(NetworkObject):
    def add(
        self,
        name: str,
        ip_address: str = None,
        ipv4_address: str = None,
        ipv6_address: str = None,
        ip_address_first: str = None,
        ipv4_address_first: str = None,
        ipv6_address_first: str = None,
        ip_address_last: str = None,
        ipv4_address_last: str = None,
        ipv6_address_last: str = None,
        nat_settings: dict = None,
        tags: Union[str, List[str]] = None,
        **kw
    ) -> Box:
        """
        Create new object.

        Args:
            name (str): Object name. Must be unique in the domain.
            ip_address (str): IPv4 or IPv6 address. If both addresses are required use ipv4-address
            and ipv6-address fields explicitly.
            ipv4_address (str): IPv4 address.
            ipv6_address (str): IPv6 address.
            ip_address_first (str): First IP address in the range. If both IPv4 and IPv6 address ranges are required,
            use the ipv4-address-first and the ipv6-address-first fields instead.
            ipv4_address_first (str): First IPv4 address in the range.
            ipv6_address_first (str): First IPv6 address in the range.
            ip_address_last (str): 	Last IP address in the range. If both IPv4 and IPv6 address ranges are required,
            use the ipv4-address-last and the ipv6-address-last fields instead.
            ipv4_address_last (str): Last IPv4 address in the range.
            ipv6_address_last (str): Last IPv6 address in the range.
            tags (Union(str,List[str])): Collection of tag identifiers.
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
            **groups (Union(str,List[str])):
                Collection of group identifiers.
            **ignore-warnings (bool, optional):
                Apply changes ignoring warnings. Default is False
            **ignore-errors (bool, optional):
                Apply changes ignoring errors. You won't be able to publish such a changes.
                If ignore-warnings flag was omitted - warnings will also be ignored. Default is False
        Returns:
            :obj:`Box`: The response from the server
        Examples:
            >>> firewallManagement.network_objects.multicast_address_range.add(name="New Multicast Address Range",
            ip_address_first="224.0.0.1",ip_address_last="224.0.0.4")
        """

        # Main request parameters
        payload = {"name": name}

        if ip_address is not None:
            payload["ip-address"] = ip_address
        elif ipv4_address_first is not None:
            payload["ipv4-address"] = ipv4_address
        elif ipv6_address_first is not None:
            payload["ipv6-address"] = ipv6_address
        if ip_address_first is not None:
            payload["ip-address-first"] = ip_address_first
        elif ipv4_address_first is not None:
            payload["ipv4-address-first"] = ipv4_address_first
        elif ipv6_address_first is not None:
            payload["ipv6-address-first"] = ipv6_address_first
        if ip_address_last is not None:
            payload["ip-address-last"] = ip_address_last
        elif ipv4_address_last is not None:
            payload["ipv4-address-last"] = ipv4_address_last
        elif ipv6_address_last is not None:
            payload["ipv6-address-last"] = ipv6_address_last

        if tags is not None:
            payload["tags"] = tags

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

        return self._post("add-multicast-address-range", json=payload)

    def show(self, uid: str = None, name: str = None, **kw) -> Box:
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
            >>> FirewallManagement.network_objects.multicast_address_range.show(uid="196e93a9-b90b-4ab1-baa6-124e7289aa20")
        """
        return self.show_object(
            endpoint="show-multicast-address-range", uid=uid, name=name, **kw
        )

    def set(
        self,
        uid: str = None,
        name: str = None,
        ip_address: str = None,
        ipv4_address: str = None,
        ipv6_address: str = None,
        ip_address_first: str = None,
        ipv4_address_first: str = None,
        ipv6_address_first: str = None,
        ip_address_last: str = None,
        ipv4_address_last: str = None,
        ipv6_address_last: str = None,
        new_name: str = None,
        nat_settings: dict = None,
        tags: Union[str, List[str]] = None,
        **kw
    ) -> Box:
        """
        Create new object.

        Args:
            name (str): Object name. Must be unique in the domain.
            ip_address (str): IPv4 or IPv6 address. If both addresses are required use ipv4-address
            and ipv6-address fields explicitly.
            ipv4_address (str): IPv4 address.
            ipv6_address (str): IPv6 address.
            ip_address_first (str): First IP address in the range. If both IPv4 and IPv6 address ranges are required,
            use the ipv4-address-first and the ipv6-address-first fields instead.
            ipv4_address_first (str): First IPv4 address in the range.
            ipv6_address_first (str): First IPv6 address in the range.
            ip_address_last (str): 	Last IP address in the range. If both IPv4 and IPv6 address ranges are required,
            use the ipv4-address-last and the ipv6-address-last fields instead.
            ipv4_address_last (str): Last IPv4 address in the range.
            ipv6_address_last (str): Last IPv6 address in the range.
            new_name (str): New name of the object.
            tags (Union(str,List[str])): Collection of tag identifiers.
        Keyword Args:
            **color (Color, optional):
                Color of the object. Should be one of existing colors.
            **comments (str, optional):
                Comments string.
            **details-level (str, optional):
                The level of detail for some of the fields in the response can vary from showing only the UID value
                of the object to a fully detailed representation of the object.
            **groups (Union(str,List[str])):
                Collection of group identifiers.
            **ignore-warnings (bool, optional):
                Apply changes ignoring warnings. Default is False
            **ignore-errors (bool, optional):
                Apply changes ignoring errors. You won't be able to publish such a changes.
                If ignore-warnings flag was omitted - warnings will also be ignored. Default is False
        Returns:
            :obj:`Box`: The response from the server
        Examples:
            >>> firewallManagement.network_objects.multicast_address_range.set(uid="faff3fdf-01b9-4c58-97dc-176c409b5bc1",
            new_name="New Multicast Address Range",ip_address_first="224.0.0.1",ip_address_last="224.0.0.4")
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
        elif ipv4_address_first is not None:
            payload["ipv4-address"] = ipv4_address
        elif ipv6_address_first is not None:
            payload["ipv6-address"] = ipv6_address

        if ip_address_first is not None:
            payload["ip-address-first"] = ip_address_first
        if ipv4_address_first is not None:
            payload["ipv4-address-first"] = ipv4_address_first
        if ipv6_address_first is not None:
            payload["ipv6-address-first"] = ipv6_address_first

        if ip_address_last is not None:
            payload["ip-address-last"] = ip_address_last
        if ipv4_address_last is not None:
            payload["ipv4-address-last"] = ipv4_address_last
        if ipv6_address_last is not None:
            payload["ipv6-address-last"] = ipv6_address_last

        if new_name is not None:
            payload["new-name"] = new_name
        if tags is not None:
            payload["tags"] = tags

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

        return self._post("set-multicast-address-range", json=payload)

    def delete(self, uid: str = None, name: str = None, **kw) -> Box:
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
            >>> FirewallManagement.network_objects.multicast_address_range.delete(
                uid="196e93a9-b90b-4ab1-baa6-124e7289aa20")
        """
        return self.delete_object(
            endpoint="delete-multicast-address-range", uid=uid, name=name, **kw
        )

    def show_multicast_address_ranges(
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
            filter_results (str): Search expression to filter objects by.
            The provided text should be exactly the same as it would be given in SmartConsole Object Explorer.
            The logical operators in the expression ('AND', 'OR') should be provided in capital letters.
            he search involves both a IP search and a textual search in name, comment, tags etc.
            limit (int): The maximal number of returned results. Default to 50 (between 1 and 500)
            offset (int): Number of the results to initially skip. Default to 0
            order (List[dict]): Sorts results by the given field. By default the results are sorted in the
            descending order by the session publish time.
        Returns:
            :obj:`Box`: The response from the server
        Examples:
            >>> FirewallManagement.network_objects.network.show_multicast_address_ranges()
        """
        return self.show_objects(
            endpoint="show-multicast-address-ranges",
            filter_results=filter_results,
            limit=limit,
            offset=offset,
            order=order,
            extra_secondary_parameters={"show-membership": bool},
            **kw
        )
