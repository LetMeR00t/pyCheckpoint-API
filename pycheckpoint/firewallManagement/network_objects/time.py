from typing import Union

from box import Box

from ..abstract.network_object import NetworkObjectAPI
from ..exception import MandatoryFieldMissing
from pycheckpoint.utils import sanitize_secondary_parameters
from pycheckpoint.models import Color


class TimeAPI(NetworkObjectAPI):
    def add(
        self,
        name: str,
        end: dict = None,
        end_never: bool = None,
        hours_ranges: list[dict] = None,
        start: dict = None,
        start_now: bool = None,
        tags: Union[str, list[str]] = None,
        recurrence: dict = None,
        **kw
    ) -> Box:
        """
        Create new object.

        Args:
            name (str): Object name. Must be unique in the domain.
            end (dict): End time. Note: Each gateway may interpret this time differently according to its time zone.
            end_never (bool): End never.
            hours_ranges (list[dict]): Hours recurrence. Note: Each gateway may interpret this time differently
            according to its time zone.
            start (dict): Starting time. Note: Each gateway may interpret this time differently according to its time zone.
            start_now (bool): Start immediately.
            tags (Union(str,list[str])): Collection of tag identifiers.
            recurrence (dict): Days recurrence.
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
            >>> firewallManagementApi.network_objects.time.add(name="My object")
        """

        # Main request parameters
        payload = {"name": name}

        if end is not None:
            payload["end"] = end
        if end_never is not None:
            payload["end-never"] = end_never
        if hours_ranges is not None:
            payload["hours-ranges"] = hours_ranges
        if start is not None:
            payload["start"] = start
        if start_now is not None:
            payload["start-now"] = start_now
        if recurrence is not None:
            payload["recurrence"] = recurrence
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

        return self._post("add-time", json=payload)

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
            >>> firewallManagementApi.network_objects.time.show(uid="d5e8d56f-2d77-4824-a5d2-c4s7885dd4z7")
        """
        return self.show_object(endpoint="show-time", uid=uid, name=name, **kw)

    def set(
        self,
        uid: str = None,
        name: str = None,
        end: dict = None,
        end_never: bool = None,
        hours_ranges: list[dict] = None,
        start: dict = None,
        start_now: bool = None,
        tags: Union[str, list[str]] = None,
        recurrence: dict = None,
        new_name: str = None,
        **kw
    ) -> Box:
        """
        Create new object.

        Args:
            uid (str): Object unique identifier.
            name (str): Object name. Must be unique in the domain.
            end (dict): End time. Note: Each gateway may interpret this time differently according to its time zone.
            end_never (bool): End never.
            hours_ranges (list[dict]): Hours recurrence. Note: Each gateway may interpret this time differently
            according to its time zone.
            start (dict): Starting time. Note: Each gateway may interpret this time differently according to its time zone.
            start_now (bool): Start immediately.
            tags (Union(str,list[str])): Collection of tag identifiers.
            recurrence (dict): Days recurrence.
            new_name (str): New name of the object.
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
            >>> firewallManagement.network_objects.time.set(uid="d5e8d56f-2d77-4824-a5d2-c4s7885dd4z7",
            new_name="timeObject1")
        """

        # Main request parameters
        payload = {}
        if uid is not None:
            payload["uid"] = uid
        elif name is not None:
            payload["name"] = name
        else:
            raise MandatoryFieldMissing("uid or name")

        if end is not None:
            payload["end"] = end
        if end_never is not None:
            payload["end-never"] = end_never
        if hours_ranges is not None:
            payload["hours-ranges"] = hours_ranges
        if start is not None:
            payload["start"] = start
        if start_now is not None:
            payload["start-now"] = start_now
        if recurrence is not None:
            payload["recurrence"] = recurrence
        if tags is not None:
            payload["tags"] = tags
        if new_name is not None:
            payload["new-name"] = new_name

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

        return self._post("set-time", json=payload)

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
            >>> firewallManagementApi.network_objects.time.delete(uid="d5e8d56f-2d77-4824-a5d2-c4s7885dd4z7")
        """
        return self.delete_object(endpoint="delete-time", uid=uid, name=name, **kw)

    def show_times(
        self,
        filter: str = None,
        limit: int = 50,
        offset: int = 0,
        order: list[dict] = None,
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
            order (list[dict]): Sorts results by the given field. By default the results are sorted in the
            descending order by the session publish time.
        Returns:
            :obj:`Box`: The response from the server
        Examples:
            >>> firewallManagementApi.network_objects.time.shows_times()
        """
        return self.show_objects(
            endpoint="show-times",
            filter=filter,
            limit=limit,
            offset=offset,
            order=order,
            extra_secondary_parameters={"show-membership": bool},
            **kw
        )
