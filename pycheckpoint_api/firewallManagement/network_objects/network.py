from typing import List, Union

from box import Box

from pycheckpoint_api.models import Color
from pycheckpoint_api.utils import sanitize_secondary_parameters

from ..abstract.network_object import NetworkObject
from ..exception import MandatoryFieldMissing


class Network(NetworkObject):
    def add(
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
        tags: Union[str, List[str]] = None,
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
            nat_settings (dict): NAT settings.
            tags (Union(str,List[str])): Collection of tag identifiers.
            broadcast (str): Allow broadcast address inclusion.
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
                Apply changes ignoring warnings. Defaults to False
            **ignore-errors (bool, optional):
                Apply changes ignoring errors. You won't be able to publish such a changes.
                If ignore-warnings flag was omitted - warnings will also be ignored. Defaults to False
        Returns:
            :obj:`Box`: The response from the server
        Examples:
            >>> FirewallManagement.network_objects.network.add(name="My object")
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
            "groups": Union[str, List[str]],
            "ignore-warnings": bool,
            "ignore-errors": bool,
        }
        payload.update(sanitize_secondary_parameters(secondary_parameters, **kw))

        return self._post("add-network", json=payload)

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
            >>> FirewallManagement.network_objects.network.show(uid="d5e8d56f-2d77-4824-a5d2-c4s7885dd4z7")
        """
        return self.show_object(endpoint="show-network", uid=uid, name=name, **kw)

    def set(
        self,
        uid: str = None,
        name: str = None,
        subnet: str = None,
        subnet4: str = None,
        subnet6: str = None,
        mask_length: str = None,
        mask_length4: str = None,
        mask_length6: str = None,
        subnet_mask: str = None,
        new_name: str = None,
        nat_settings: dict = None,
        tags: Union[str, List[str]] = None,
        broadcast: str = None,
        **kw
    ) -> Box:
        """
        Create new object.

        Args:
            uid (str): Object unique identifier.
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
            new_name (str): New name of the object.
            nat_settings (dict): NAT settings.
            tags (Union(str,List[str])): Collection of tag identifiers.
            broadcast (str): Allow broadcast address inclusion.
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
                Apply changes ignoring warnings. Defaults to False
            **ignore-errors (bool, optional):
                Apply changes ignoring errors. You won't be able to publish such a changes.
                If ignore-warnings flag was omitted - warnings will also be ignored. Defaults to False
        Returns:
            :obj:`Box`: The response from the server
        Examples:
            >>> firewallManagement.network_objects.network.set(uid="d5e8d56f-2d77-4824-a5d2-c4s7885dd4z7",subnet="192.0.2.0",
                subnet_mask="255.255.255.0")
        """

        # Main request parameters
        payload = {}
        if uid is not None:
            payload["uid"] = uid
        elif name is not None:
            payload["name"] = name
        else:
            raise MandatoryFieldMissing("uid or name")

        if subnet is not None:
            payload["subnet"] = subnet
        elif subnet4 is not None:
            payload["subnet4"] = subnet4
        elif subnet6 is not None:
            payload["subnet6"] = subnet6

        if mask_length is not None:
            payload["mask_length"] = mask_length
        elif mask_length4 is not None:
            payload["mask_length4"] = mask_length4
        elif mask_length6 is not None:
            payload["mask_length6"] = mask_length6
        elif subnet_mask is not None:
            payload["subnet_mask"] = subnet_mask

        if nat_settings is not None:
            payload["nat-settings"] = nat_settings
        if new_name is not None:
            payload["new-name"] = new_name
        if tags is not None:
            payload["tags"] = tags
        if broadcast is not None:
            payload["broadcast"] = broadcast

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

        return self._post("set-network", json=payload)

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
                Apply changes ignoring warnings. Defaults to False
            **ignore-errors (bool, optional):
                Apply changes ignoring errors. You won't be able to publish such a changes.
                If ignore-warnings flag was omitted - warnings will also be ignored. Defaults to False
        Returns:
            :obj:`Box`: The response from the server
        Examples:
            >>> FirewallManagement.network_objects.network.delete(uid="d5e8d56f-2d77-4824-a5d2-c4s7885dd4z7")
        """
        return self.delete_object(endpoint="delete-network", uid=uid, name=name, **kw)

    def show_networks(
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
            limit (int): The maximal number of returned results. Defaults to 50 (between 1 and 500)
            offset (int): Number of the results to initially skip. Defaults to 0
            order (List[dict]): Sorts results by the given field. By default the results are sorted in the
            descending order by the session publish time.
        Returns:
            :obj:`Box`: The response from the server
        Examples:
            >>> FirewallManagement.network_objects.network.shows_networks()
        """
        return self.show_objects(
            endpoint="show-networks",
            filter_results=filter_results,
            limit=limit,
            offset=offset,
            order=order,
            extra_secondary_parameters={"show-membership": bool},
            **kw
        )
