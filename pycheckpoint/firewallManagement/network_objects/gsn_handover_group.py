from typing import Union

from box import Box
from restfly.endpoint import APIEndpoint

from ..exception import MandatoryFieldMissing
from pycheckpoint.utils import sanitize_secondary_parameters
from pycheckpoint.models import Color


class GSNHandoverGroupAPI(APIEndpoint):
    def add(
        self,
        name: str,
        enforce_gtp: bool = None,
        gtp_rate: int = None,
        members: Union[str, list[str]] = None,
        tags: Union[str, list[str]] = None,
        **kw,
    ) -> Box:
        """
        Create new object.

        Args:
            name (str): Object name. Must be unique in the domain.
            enforce_gtp (bool): Enable enforce GTP signal packet rate limit from this group.
            gtp_rate (int): Limit of the GTP rate in PDU/sec.
            members (Union[str, list[str]]): Collection of Network objects identified by the name or UID.
            tags (Union(str,list[str])): Collection of tag identifiers.
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
            >>> firewallManagementApi.network_objects.gsn_handover_group.add(name="My object")
        """

        # Main request parameters
        payload = {"name": name}
        if enforce_gtp is not None:
            payload["enforce-gtp"] = enforce_gtp
        if gtp_rate is not None:
            payload["gtp-rate"] = gtp_rate
        if members is not None:
            payload["members"] = members
        if tags is not None:
            payload["tags"] = tags

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

        return self._post("add-gsn-handover-group", json=payload)

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
            >>> firewallManagementApi.network_objects.gsn_handover_group.show(uid="f140a9d1-4167-456a-931d-abdaa4c8aa7e")
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

        return self._post("show-gsn-handover-group", json=payload)

    def set(
        self,
        uid: str = None,
        name: str = None,
        enforce_gtp: bool = None,
        gtp_rate: int = None,
        members: Union[dict, str, list[str]] = None,
        new_name: str = None,
        tags: Union[str, list[str]] = None,
        **kw,
    ) -> Box:
        """
        Edit existing object using object name or uid.

        Args:
            uid (str): Object unique identifier.
            name (str): Object name.
            enforce_gtp (bool): Enable enforce GTP signal packet rate limit from this group.
            gtp_rate (int): Limit of the GTP rate in PDU/sec.
            members (Union[dict, str, list[str]]): Collection of Network objects identified by the name or UID.
            new_name (str): New name of the object.
            tags (Union(str,list[str])): Collection of tag identifiers.
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
            >>> firewallManagement.network_objects.gsn_handover_group.set(uid="f140a9d1-4167-456a-931d-abdaa4c8aa7e",
            new_name="gsnhandovergroup")
        """

        # Main request parameters
        payload = {}
        if uid is not None:
            payload["uid"] = uid
        elif name is not None:
            payload["name"] = name
        else:
            raise MandatoryFieldMissing("uid or name")

        if enforce_gtp is not None:
            payload["enforce-gtp"] = enforce_gtp
        if gtp_rate is not None:
            payload["gtp-rate"] = gtp_rate
        if members is not None:
            payload["members"] = members
        if new_name is not None:
            payload["new-name"] = new_name
        if tags is not None:
            payload["tags"] = tags

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

        return self._post("set-gsn-handover-group", json=payload)

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
            >>> firewallManagement.network_objects.gsn_handover_group.delete(uid="f140a9d1-4167-456a-931d-abdaa4c8aa7e")
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

        return self._post("delete-gsn-handover-group", json=payload)

    def show_gsn_handover_groups(
        self,
        filter: str = None,
        limit: int = 50,
        offset: int = 0,
        order: list[dict] = None,
        **kw,
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
            >>> firewallManagementApi.network_objects.group.shows_groups()
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
            "dereference-group-members": bool,
            "show-membership": bool,
            "details-level": str,
            "domains-to-process": list[str],
        }
        payload.update(sanitize_secondary_parameters(secondary_parameters, **kw))

        return self._post("show-gsn-handover-groups", json=payload)
