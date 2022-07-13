from typing import Union, List

from box import Box

from ..abstract.network_object import NetworkObject
from ..exception import MandatoryFieldMissing
from pycheckpoint_api.utils import sanitize_secondary_parameters
from pycheckpoint_api.models import Color


class TacacsServer(NetworkObject):
    def add(
        self,
        name: str,
        server: str,
        secret_key: str = False,
        encryption: bool = False,
        priority: int = 1,
        server_type: str = "TACACS",
        service: str = "TACACS",
        tags: Union[str, List[str]] = None,
        **kw
    ) -> Box:
        """
        Create new object.

        Args:
            name (str): Object name. Must be unique in the domain.
            secret_key (str): The server's secret key. Required only when "server-type" was selected to be "TACACS+".
            server (str): The UID or Name of the host that is the TACACS Server.
            encryption (bool):  Default: false; Is there a secret key defined on the server.
            Must be set true when "server-type" was selected to be "TACACS+".
            priority (int): The priority of the TACACS Server in case it is a member of a TACACS Group.
            server_type (str): Server type, TACACS or TACACS+.
            service (str): Server service, only relevant when "server-type" is TACACS.
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
            >>> FirewallManagement.network_objects.tag.add(name="My object")
        """

        # Main request parameters
        payload = {"name": name, "server": server}

        if server_type == "TACACS+":
            payload["secret-key"] = secret_key
        if encryption is not None:
            payload["encryption"] = encryption
        if priority is not None:
            payload["priority"] = priority
        if server_type is not None:
            payload["server-type"] = server_type
        if tags is not None:
            payload["tags"] = tags
        if service is not None:
            payload["service"] = service

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

        return self._post("add-tacacs-server", json=payload)

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
            >>> FirewallManagement.network_objects.tacacs_server.show(uid="ed997ff8-6709-4d71-a713-99bf01711cd5")
        """
        return self.show_object(endpoint="show-tacacs-server", uid=uid, name=name, **kw)

    def set(
        self,
        server: str,
        uid: str = None,
        name: str = None,
        secret_key: str = False,
        encryption: bool = False,
        priority: int = 1,
        server_type: str = "TACACS",
        service: str = "TACACS",
        new_name: str = None,
        tags: Union[str, List[str]] = None,
        **kw
    ) -> Box:
        """
        Edit existing object using object name or uid.

        Args:
            uid (str): Object unique identifier.
            name (str): Object name.
            secret_key (str): The server's secret key. Required only when "server-type" was selected to be "TACACS+".
            server (str): The UID or Name of the host that is the TACACS Server.
            encryption (bool):  Default: false; Is there a secret key defined on the server.
            Must be set true when "server-type" was selected to be "TACACS+".
            priority (int): The priority of the TACACS Server in case it is a member of a TACACS Group.
            server_type (str): Server type, TACACS or TACACS+.
            service (str): Server service, only relevant when "server-type" is TACACS.
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
            >>> firewallManagement.network_objects.tacacs_server.set(uid="ed997ff8-6709-4d71-a713-99bf01711cd5",
            new_name="New TACACS Server")
        """

        # Main request parameters
        payload = {"server": server}
        if uid is not None:
            payload["uid"] = uid
        elif name is not None:
            payload["name"] = name
        else:
            raise MandatoryFieldMissing("uid or name")

        if server_type == "TACACS+":
            payload["secret-key"] = secret_key
        if encryption is not None:
            payload["encryption"] = encryption
        if priority is not None:
            payload["priority"] = priority
        if server_type is not None:
            payload["server-type"] = server_type
        if service is not None:
            payload["service"] = service
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

        return self._post("set-tacacs-server", json=payload)

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
            >>> FirewallManagement.network_objects.tacacs_server.delete(uid="ed997ff8-6709-4d71-a713-99bf01711cd5")
        """
        return self.delete_object(
            endpoint="delete-tacacs-server", uid=uid, name=name, **kw
        )

    def show_tacacs_servers(
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
            >>> FirewallManagement.network_objects.tacacs_server.shows_tacacs_servers()
        """
        return self.show_objects(
            endpoint="show-tacacs-servers",
            filter_results=filter_results,
            limit=limit,
            offset=offset,
            order=order,
            show_as_ranges=show_as_ranges,
            extra_secondary_parameters={"domains-to-process": List[str]},
            **kw
        )
