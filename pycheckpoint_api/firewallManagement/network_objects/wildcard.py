from typing import List, Union

from box import Box

from pycheckpoint_api.models import Color
from pycheckpoint_api.utils import sanitize_secondary_parameters

from ..abstract.network_object import NetworkObject
from ..exception import MandatoryFieldMissing


class Wildcard(NetworkObject):
    def add(
        self,
        name: str,
        ipv4_address: str = None,
        ipv4_mask_wildcard: str = None,
        ipv6_address: str = None,
        ipv6_mask_wildcard: str = None,
        tags: Union[str, List[str]] = None,
        **kw,
    ) -> Box:
        """
        Create new object.

        Args:
            name (str): Object name. Must be unique in the domain.
            ip_address (str, optional): IPv4 or IPv6 address. If both addresses are required use ipv4-address
            and ipv6-address fields explicitly.
            ipv4_address (str, optional): IPv4 address.
            ipv4_mask_wildcard (str, optional): IPv4 mask wildcard.
            ipv6_address (str, optional): IPv6 address.
            ipv6_mask_wildcard (str, optional): IPv6 mask wildcard.
            tags (Union(str,List[str]), optional): Collection of tag identifiers.
            
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
            >>> firewall.network_objects.wildcard.add(name="My object")
        """

        # Main request parameters
        payload = {"name": name}
        if ipv4_address is not None:
            payload["ipv4-address"] = ipv4_address
        if ipv4_mask_wildcard is not None:
            payload["ipv4-mask-wildcard"] = ipv4_mask_wildcard
        if ipv6_address is not None:
            payload["ipv6-address"] = ipv6_address
        if ipv6_mask_wildcard is not None:
            payload["ipv6-mask-wildcard"] = ipv6_mask_wildcard

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

        return self._post("add-wildcard", json=payload)

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
            >>> firewall.network_objects.wildcard.show(uid="9423d36f-2d66-4754-b9e2-e7f4493756d4")
        """
        return self.show_object(endpoint="show-wildcard", uid=uid, name=name, **kw)

    def set(
        self,
        uid: str = None,
        name: str = None,
        ipv4_address: str = None,
        ipv4_mask_wildcard: str = None,
        ipv6_address: str = None,
        ipv6_mask_wildcard: str = None,
        new_name: str = None,
        tags: Union[str, List[str]] = None,
        **kw,
    ) -> Box:
        """
        Edit existing object using object name or uid.

        Args:
            uid (str, optional): Object unique identifier.
            name (str, optional): Object name.
            ip_address (str, optional): IPv4 or IPv6 address. If both addresses are required use ipv4-address
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
            >>> firewall.network_objects.wildcard.set(name="My object")
        """

        # Main request parameters
        payload = {}
        if uid is not None:
            payload["uid"] = uid
        elif name is not None:
            payload["name"] = name
        else:
            raise MandatoryFieldMissing("uid or name")

        if ipv4_address is not None:
            payload["ipv4-address"] = ipv4_address
        if ipv4_mask_wildcard is not None:
            payload["ipv4-mask-wildcard"] = ipv4_mask_wildcard
        if ipv6_address is not None:
            payload["ipv6-address"] = ipv6_address
        if ipv6_mask_wildcard is not None:
            payload["ipv6-mask-wildcard"] = ipv6_mask_wildcard

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

        return self._post("set-wildcard", json=payload)

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
            >>> firewall.network_objects.wildcard.delete(uid="d8a5e4dd-2a93-4847-aaa8-d5d33a695da5")
        """
        return self.delete_object(endpoint="delete-wildcard", uid=uid, name=name, **kw)

    def show_wildcards(
        self,
        filter_results: str = None,
        limit: int = 50,
        offset: int = 0,
        order: List[dict] = None,
        **kw,
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
            >>> firewall.network_objects.wildcard.shows_wildcards()
        """
        return self.show_objects(
            endpoint="show-wildcards",
            filter_results=filter_results,
            limit=limit,
            offset=offset,
            order=order,
            **kw,
        )
