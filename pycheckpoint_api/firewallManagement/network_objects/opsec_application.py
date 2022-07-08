from typing import Union, List

from box import Box

from ..abstract.network_object import NetworkObjectAPI
from ..exception import MandatoryFieldMissing
from pycheckpoint_api.utils import sanitize_secondary_parameters
from pycheckpoint_api.models import Color


class OPSECApplicationAPI(NetworkObjectAPI):
    def add(
        self,
        name: str,
        host: str,
        cpmi: dict = None,
        lea: dict = None,
        one_time_password: str = None,
        tags: Union[str, List[str]] = None,
        **kw
    ) -> Box:
        """
        Create a new OPSEC Application. At least one client entity (LEA, CPMI) must be supplied.

        Args:
            name (str): Object name. Must be unique in the domain.
            host (str): The host where the server is running. Pre-define the host as a network object.
            cpmi (dict): Used to setup the CPMI client entity.
            lea (dict): Used to setup the LEA client entity.
            one_time_password (str): A password required for establishing a Secure Internal Communication (SIC).
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
            >>> firewallManagement.network_objects.opsec_application.add(
        name="MyOpsecApplication",
        host="SomeHost",
        cpmi={
            "enabled": "true",
            "use-administrator-credentials": "false",
            "administrator-profile": "Super User",
        },
        lea={"enabled": "false"},
        one_time_password="SomePassword")
        """

        # Main request parameters
        payload = {"name": name, "host": host}

        if cpmi is not None:
            payload["cpmi"] = cpmi
        if lea is not None:
            payload["lea"] = lea
        if one_time_password is not None:
            payload["one-time-password"] = one_time_password
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

        return self._post("add-opsec-application", json=payload)

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
            >>> firewallManagementApi.network_objects.opsec_application.show(uid="ed997ff8-6709-4d71-a713-99bf01711cd5")
        """
        return self.show_object(
            endpoint="show-opsec-application", uid=uid, name=name, **kw
        )

    def set(
        self,
        uid: str = None,
        name: str = None,
        host: str = None,
        cpmi: dict = None,
        lea: dict = None,
        one_time_password: str = None,
        new_name: str = None,
        tags: Union[str, List[str]] = None,
        **kw
    ) -> Box:
        """
        Edit existing object using object name or uid.

        Args:
            uid (str): Object unique identifier.
            name (str): Object name.
            host (str): The host where the server is running. Pre-define the host as a network object.
            cpmi (dict): Used to setup the CPMI client entity.
            lea (dict): Used to setup the LEA client entity.
            one_time_password (str): A password required for establishing a Secure Internal Communication (SIC).
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
            >>> firewallManagement.network_objects.tag.set(uid="ed997ff8-6709-4d71-a713-99bf01711cd5",
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

        if host is not None:
            payload["host"] = host
        if cpmi is not None:
            payload["cpmi"] = cpmi
        if lea is not None:
            payload["lea"] = lea
        if one_time_password is not None:
            payload["one-time-password"] = one_time_password
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

        return self._post("set-opsec-application", json=payload)

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
            >>> firewallManagementApi.network_objects.opsec_application.delete(uid="ed997ff8-6709-4d71-a713-99bf01711cd5")
        """
        return self.delete_object(
            endpoint="delete-opsec-application", uid=uid, name=name, **kw
        )

    def show_opsec_applications(
        self,
        filter: str = None,
        limit: int = 50,
        offset: int = 0,
        order: List[dict] = None,
        show_as_ranges: bool = False,
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
            order (List[dict]): Sorts results by the given field. By default the results are sorted in the
            descending order by the session publish time.
            show_as_ranges (bool): When true, the group's matched content is displayed as ranges of IP addresses rather
            than network objects. Objects that are not represented using IP addresses are presented as objects.
            The 'members' parameter is omitted from the response and instead the 'ranges' parameter is displayed.
            Default is False.
        Returns:
            :obj:`Box`: The response from the server
        Examples:
            >>> firewallManagementApi.network_objects.opsec_application.shows_opsec_applications()
        """
        return self.show_objects(
            endpoint="show-opsec-applications",
            filter=filter,
            limit=limit,
            offset=offset,
            order=order,
            show_as_ranges=show_as_ranges,
            extra_secondary_parameters={"domains-to-process": List[str]},
            **kw
        )
