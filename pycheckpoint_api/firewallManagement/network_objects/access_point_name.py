from typing import List, Union

from box import Box

from pycheckpoint_api.models import Color
from pycheckpoint_api.utils import sanitize_secondary_parameters

from ..abstract.network_object import NetworkObject
from ..exception import MandatoryFieldMissing


class AccessPointName(NetworkObject):
    def add(
        self,
        name: str,
        apn: str,
        enforce_end_user_domain: bool = None,
        block_traffic_other_end_user_domains: bool = None,
        block_traffic_this_end_user_domain: bool = None,
        end_user_domain: str = None,
        tags: Union[str, List[str]] = None,
        **kw
    ) -> Box:
        """
        Create new object.

        Args:
            name (str): Object name. Must be unique in the domain.
            apn (str): APN name.
            enforce_end_user_domain (bool): Enable enforce end user domain.
            block_traffic_other_end_user_domains (bool): Block MS to MS traffic between this and other APN end user domains.
            block_traffic_this_end_user_domain (bool): Block MS to MS traffic within this end user domain.
            end_user_domain (str): End user domain name or UID.
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
                Apply changes ignoring warnings. Defaults to False
            **ignore-errors (bool, optional):
                Apply changes ignoring errors. You won't be able to publish such a changes.
                If ignore-warnings flag was omitted - warnings will also be ignored. Defaults to False
        Returns:
            :obj:`Box`: The response from the server
        Examples:
            >>> FirewallManagement.network_objects.access_point_name.add(name="My object")
        """

        # Main request parameters
        payload = {"name": name, "apn": apn}

        if tags is not None:
            payload["tags"] = tags
        if enforce_end_user_domain is not None:
            payload["enforce-end-user-domain"] = enforce_end_user_domain
        if block_traffic_other_end_user_domains is not None:
            payload[
                "block-traffic-other-end-user-domains"
            ] = block_traffic_other_end_user_domains
        if block_traffic_this_end_user_domain is not None:
            payload[
                "block-traffic-this-end-user-domain"
            ] = block_traffic_this_end_user_domain
        if end_user_domain is not None:
            payload["end-user-domain"] = end_user_domain

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

        return self._post("add-access-point-name", json=payload)

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
            >>> FirewallManagement.network_objects.access_point_name.show(uid="ed997ff8-6709-4d71-a713-99bf01711cd5")
        """
        return self.show_object(
            endpoint="show-access-point-name", uid=uid, name=name, **kw
        )

    def set(
        self,
        uid: str = None,
        name: str = None,
        apn: str = None,
        enforce_end_user_domain: bool = None,
        block_traffic_other_end_user_domains: bool = None,
        block_traffic_this_end_user_domain: bool = None,
        end_user_domain: str = None,
        new_name: str = None,
        tags: Union[str, List[str]] = None,
        **kw
    ) -> Box:
        """
        Edit existing object using object name or uid.

        Args:
            uid (str): Object unique identifier.
            name (str): Object name.
            apn (str): APN name.
            enforce_end_user_domain (bool): Enable enforce end user domain.
            block_traffic_other_end_user_domains (bool): Block MS to MS traffic between this and other APN end user domains.
            block_traffic_this_end_user_domain (bool): Block MS to MS traffic within this end user domain.
            end_user_domain (str): End user domain name or UID.
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
                Apply changes ignoring warnings. Defaults to False
            **ignore-errors (bool, optional):
                Apply changes ignoring errors. You won't be able to publish such a changes.
                If ignore-warnings flag was omitted - warnings will also be ignored. Defaults to False
        Returns:
            :obj:`Box`: The response from the server
        Examples:
            >>> firewallManagement.network_objects.access_point_name.set(uid="ed997ff8-6709-4d71-a713-99bf01711cd5",
            new_name="New Access Point Name")
        """

        # Main request parameters
        payload = {}
        if uid is not None:
            payload["uid"] = uid
        elif name is not None:
            payload["name"] = name
        else:
            raise MandatoryFieldMissing("uid or name")

        if new_name is not None:
            payload["new-name"] = new_name
        if tags is not None:
            payload["tags"] = tags
        if apn is not None:
            payload["apn"] = apn
        if enforce_end_user_domain is not None:
            payload["enforce-end-user-domain"] = enforce_end_user_domain
        if block_traffic_other_end_user_domains is not None:
            payload[
                "block-traffic-other-end-user-domains"
            ] = block_traffic_other_end_user_domains
        if block_traffic_this_end_user_domain is not None:
            payload[
                "block-traffic-this-end-user-domain"
            ] = block_traffic_this_end_user_domain
        if end_user_domain is not None:
            payload["end-user-domain"] = end_user_domain

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

        return self._post("set-access-point-name", json=payload)

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
            >>> FirewallManagement.network_objects.access_point_name.delete(uid="ed997ff8-6709-4d71-a713-99bf01711cd5")
        """
        return self.delete_object(
            endpoint="delete-access-point-name", uid=uid, name=name, **kw
        )

    def show_access_point_names(
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
            >>> FirewallManagement.network_objects.access_point_name.shows_access_point_names()
        """
        return self.show_objects(
            endpoint="show-access-point-names",
            filter_results=filter_results,
            limit=limit,
            offset=offset,
            order=order,
            extra_secondary_parameters={"domains-to-process": List[str]},
            **kw
        )
