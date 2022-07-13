from typing import Union, List

from box import Box

from ..abstract.network_object import NetworkObject
from ..exception import MandatoryFieldMissing
from pycheckpoint_api.utils import sanitize_secondary_parameters
from pycheckpoint_api.models import Color


class LSVProfile(NetworkObject):
    def add(
        self,
        name: str,
        certificate_authority: str,
        allowed_ip_addresses: Union[str, List[str]] = None,
        restrict_allowed_addresses: bool = False,
        tags: Union[str, List[str]] = None,
        vpn_domain: dict = None,
        **kw
    ) -> Box:
        """
        Create new object.

        Args:
            name (str): Object name. Must be unique in the domain.
            certificate_authority (str): Trusted Certificate authority for establishing trust between VPN peers,
            identified by name or UID.
            allowed_ip_addresses (Union[str, List[str]]): Collection of network objects identified by name or UID
            that represent IP addresses allowed in profile's VPN domain.
            restrict_allowed_addresses (bool): Indicate whether the IP addresses allowed in the VPN Domain
            will be restricted or not, according to allowed-ip-addresses field.
            tags (Union(str,List[str])): Collection of tag identifiers.
            vpn_domain (dict): peers' VPN Domain properties.
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
            >>> firewallManagement.network_objects.lsv_profile.add(
        name="New lsv-profile", certificate_authority="dedicated_profile_certificate")
        """

        # Main request parameters
        payload = {"name": name, "certificate-authority": certificate_authority}

        if allowed_ip_addresses is not None:
            payload["allowed-ip-addresses"] = allowed_ip_addresses
        if tags is not None:
            payload["restrict-allowed-addresses"] = restrict_allowed_addresses
        if tags is not None:
            payload["tags"] = tags
        if vpn_domain is not None:
            payload["vpn-domain"] = vpn_domain

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

        return self._post("add-lsv-profile", json=payload)

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
            >>> FirewallManagement.network_objects.lsv_profile.show(uid="ed997ff8-6709-4d71-a713-99bf01711cd5")
        """
        return self.show_object(endpoint="show-lsv-profile", uid=uid, name=name, **kw)

    def set(
        self,
        uid: str = None,
        name: str = None,
        new_name: str = None,
        certificate_authority: str = None,
        allowed_ip_addresses: Union[str, List[str]] = None,
        restrict_allowed_addresses: bool = False,
        vpn_domain: dict = None,
        tags: Union[str, List[str]] = None,
        **kw
    ) -> Box:
        """
        Edit existing object using object name or uid.

        Args:
            uid (str): Object unique identifier.
            name (str): Object name.
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
            >>> firewallManagement.network_objects.lsv_profile.set(uid="ed997ff8-6709-4d71-a713-99bf01711cd5",
            new_name="New Tag")
        """

        # Main request parameters
        payload = {}
        if uid is not None:
            payload["uid"] = uid
        elif name is not None:
            payload["name"] = name
        else:
            raise MandatoryFieldMissing("uid or name")

        if certificate_authority is not None:
            payload["certificate-authority"] = certificate_authority
        if allowed_ip_addresses is not None:
            payload["allowed-ip-addresses"] = allowed_ip_addresses
        if tags is not None:
            payload["restrict-allowed-addresses"] = restrict_allowed_addresses
        if tags is not None:
            payload["tags"] = tags
        if vpn_domain is not None:
            payload["vpn-domain"] = vpn_domain
        if new_name is not None:
            payload["new-name"] = new_name

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

        return self._post("set-lsv-profile", json=payload)

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
            >>> FirewallManagement.network_objects.lsv_profile.delete(uid="ed997ff8-6709-4d71-a713-99bf01711cd5")
        """
        return self.delete_object(
            endpoint="delete-lsv-profile", uid=uid, name=name, **kw
        )

    def show_lsv_profiles(
        self,
        filter_results: str = None,
        limit: int = 50,
        offset: int = 0,
        order: List[dict] = None,
        show_as_ranges: bool = False,
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
            show_as_ranges (bool): When true, the group's matched content is displayed as ranges of IP addresses rather
            than network objects. Objects that are not represented using IP addresses are presented as objects.
            The 'members' parameter is omitted from the response and instead the 'ranges' parameter is displayed.
            Default is False.
        Keyword Args:
            **details-level (str, optional):
                The level of detail for some of the fields in the response can vary from showing only the UID value
                of the object to a fully detailed representation of the object.
            **domains-to-process (List[str], optional):
                Indicates which domains to process the commands on. It cannot be used with the details-level full,
                must be run from the System Domain only and with ignore-warnings true.
                Valid values are: CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER.
        Returns:
            :obj:`Box`: The response from the server
        Examples:
            >>> FirewallManagement.network_objects.lsv_profile.shows_lsv_profiles()
        """
        return self.show_objects(
            endpoint="show-lsv-profiles",
            filter_results=filter_results,
            limit=limit,
            offset=offset,
            order=order,
            show_as_ranges=show_as_ranges,
            extra_secondary_parameters={"domains-to-process": List[str]},
            **kw
        )
