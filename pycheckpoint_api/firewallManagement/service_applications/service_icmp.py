from typing import List, Union

from box import Box

from pycheckpoint_api.models import Color
from pycheckpoint_api.utils import sanitize_secondary_parameters

from ..abstract.network_object import NetworkObject
from ..exception import MandatoryFieldMissing


class ServiceICMP(NetworkObject):
    def add(
        self,
        name: str,
        icmp_code: int = 0,
        icmp_type: int = 0,
        keep_connections_open_after_policy_installation: bool = None,
        tags: Union[str, List[str]] = None,
        **kw
    ) -> Box:
        """
        Create new object.

        Args:
            name (str): Object name. Must be unique in the domain.
            icmp_code (int, optional): As listed in: RFC 792.
            icmp_type (int, optional): As listed in: RFC 792.
            keep_connections_open_after_policy_installation (bool, optional): Keep connections open after policy has \
            been installed even if they are not allowed under the new policy. This overrides the settings in the \
            Connection Persistence page. If you change this property, the change will not affect open connections, \
            but only future connections.
            tags (Union(str,List[str]), optional): Collection of tag identifiers.

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
            >>> firewallManagement.service_applications.service_icmp.add(
            ... name="Icmp1",
            ... port=5669,
            ... keep_connections_open_after_policy_installation=False,
            ... session_timeout=0,
            ... match_for_any=True,
            ... sync_connections_on_cluster=True,
            ... aggressive_aging={"enable": True, "timeout": 360, "use-default-timeout": False},)
        """

        # Main request parameters
        payload = {"name": name}

        if icmp_code is not None:
            payload["icmp-code"] = icmp_code
        if icmp_type is not None:
            payload["icmp-type"] = icmp_type
        if keep_connections_open_after_policy_installation is not None:
            payload[
                "keep-connections-open-after-policy-installation"
            ] = keep_connections_open_after_policy_installation
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

        return self._post("add-service-icmp", json=payload)

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
            >>> FirewallManagement.service_applications.service_icmp.show(uid="ed997ff8-6709-4d71-a713-99bf01711cd5")
        """
        return self.show_object(endpoint="show-service-icmp", uid=uid, name=name, **kw)

    def set(
        self,
        uid: str = None,
        name: str = None,
        new_name: str = None,
        icmp_code: int = 0,
        icmp_type: int = 0,
        keep_connections_open_after_policy_installation: bool = None,
        tags: Union[str, List[str]] = None,
        **kw
    ) -> Box:
        """
        Edit existing object using object name or uid.

        Args:
            uid (str, optional): Object unique identifier.
            name (str, optional): Object name.
            new_name (str, optional): New name of the object.
            icmp_code (int, optional): As listed in: RFC 792.
            icmp_type (int, optional): As listed in: RFC 792.
            keep_connections_open_after_policy_installation (bool, optional): Keep connections open after policy has \
            been installed even if they are not allowed under the new policy. This overrides the settings in the \
            Connection Persistence page. If you change this property, the change will not affect open connections, \
            but only future connections.
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
            >>> firewallManagement.service_applications.service_icmp.set(uid="ed997ff8-6709-4d71-a713-99bf01711cd5",
            new_name="New Service TCP")
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
        if icmp_code is not None:
            payload["icmp-code"] = icmp_code
        if icmp_type is not None:
            payload["icmp-type"] = icmp_type
        if keep_connections_open_after_policy_installation is not None:
            payload[
                "keep-connections-open-after-policy-installation"
            ] = keep_connections_open_after_policy_installation
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

        return self._post("set-service-icmp", json=payload)

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
            >>> FirewallManagement.service_applications.service_icmp.delete(uid="ed997ff8-6709-4d71-a713-99bf01711cd5")
        """
        return self.delete_object(
            endpoint="delete-service-icmp", uid=uid, name=name, **kw
        )

    def show_services_icmp(
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
            show_as_ranges (bool, optional): When true, the group's matched content is displayed as ranges of IP addresses \
            rather than network objects. Objects that are not represented using IP addresses are presented as objects.\
            The 'members' parameter is omitted from the response and instead the 'ranges' parameter is displayed.\
            Defaults to False.

        Keyword Args:
            **details-level (str, optional):
                The level of detail for some of the fields in the response can vary from showing only the UID value\
                of the object to a fully detailed representation of the object.
            **domains-to-process (List[str], optional):
                Indicates which domains to process the commands on. It cannot be used with the details-level full,\
                must be run from the System Domain only and with ignore-warnings true.\
                Valid values are: CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER.
            **show-membership (bool, optional):
                Indicates whether to calculate and show "groups" field for every object in reply.

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> FirewallManagement.service_applications.service_icmp.shows_services_icmp()
        """
        return self.show_objects(
            endpoint="show-services-icmp",
            filter_results=filter_results,
            limit=limit,
            offset=offset,
            order=order,
            extra_secondary_parameters={
                "show-membership": bool,
                "domains-to-process": List[str],
            },
            **kw
        )
