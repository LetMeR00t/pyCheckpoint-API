from typing import List, Union

from box import Box

from pycheckpoint_api.models import Color
from pycheckpoint_api.utils import sanitize_secondary_parameters

from ..abstract.network_object import NetworkObject
from ..exception import MandatoryFieldMissing


class Time(NetworkObject):
    def add(
        self,
        name: str,
        end: dict = None,
        end_never: bool = None,
        hours_ranges: List[dict] = None,
        start: dict = None,
        start_now: bool = None,
        tags: Union[str, List[str]] = None,
        recurrence: dict = None,
        **kw
    ) -> Box:
        """
        Create new object.

        Args:
            name (str): Object name. Must be unique in the domain.
            end (dict, optional): End time. Note: Each gateway may interpret this time differently according to its time zone.
            end_never (bool, optional): End never.
            hours_ranges (List[dict], optional): Hours recurrence. Note: Each gateway may interpret this time differently
            according to its time zone.
            start (dict, optional): Starting time. Note: Each gateway may interpret this time differently according to its \
            time zone.
            start_now (bool, optional): Start immediately.
            tags (Union(str,List[str]), optional): Collection of tag identifiers.
            recurrence (dict, optional): Days recurrence.

        Keyword Args:
            **color (Color, optional):
                Color of the object. Should be one of existing colors.
            **comments (str, optional):
                Comments string.
            **details_level (str, optional):
                The level of detail for some of the fields in the response can vary from showing only the UID value\
                of the object to a fully detailed representation of the object.
            **groups (Union(str,List[str]), optional):
                Collection of group identifiers.
            **ignore_warnings (bool, optional):
                Apply changes ignoring warnings. Defaults to False
            **ignore_errors (bool, optional):
                Apply changes ignoring errors. You won't be able to publish such a changes.
                If ignore_warnings flag was omitted - warnings will also be ignored. Defaults to False

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> firewall.network_objects.time.add(name="My object")
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
            "details_level": str,
            "groups": Union[str, List[str]],
            "ignore_warnings": bool,
            "ignore_errors": bool,
        }
        payload.update(sanitize_secondary_parameters(secondary_parameters, **kw))

        return self._post("add-time", json=payload)

    def show(self, uid: str = None, name: str = None, **kw) -> Box:
        """
        Retrieve existing object using object name or uid.

        Args:
            uid (str, optional): Object unique identifier.
            name (str, optional): Object name.

        Keyword Args:
            **details_level (str, optional):
                The level of detail for some of the fields in the response can vary from showing only the UID value\
                of the object to a fully detailed representation of the object.

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> firewall.network_objects.time.show(uid="d5e8d56f-2d77-4824-a5d2-c4s7885dd4z7")
        """
        return self.show_object(endpoint="show-time", uid=uid, name=name, **kw)

    def set(
        self,
        uid: str = None,
        name: str = None,
        end: dict = None,
        end_never: bool = None,
        hours_ranges: List[dict] = None,
        start: dict = None,
        start_now: bool = None,
        tags: Union[str, List[str]] = None,
        recurrence: dict = None,
        new_name: str = None,
        **kw
    ) -> Box:
        """
        Create new object.

        Args:
            uid (str, optional): Object unique identifier.
            name (str, optional): Object name. Must be unique in the domain.
            end (dict, optional): End time. Note: Each gateway may interpret this time differently according to its time zone.
            end_never (bool, optional): End never.
            hours_ranges (List[dict], optional): Hours recurrence. Note: Each gateway may interpret this time differently
            according to its time zone.
            start (dict, optional): Starting time. Note: Each gateway may interpret this time differently according to its \
            time zone.
            start_now (bool, optional): Start immediately.
            tags (Union(str,List[str]), optional): Collection of tag identifiers.
            recurrence (dict, optional): Days recurrence.
            new_name (str, optional): New name of the object.

        Keyword Args:
            **color (Color, optional):
                Color of the object. Should be one of existing colors.
            **comments (str, optional):
                Comments string.
            **details_level (str, optional):
                The level of detail for some of the fields in the response can vary from showing only the UID value\
                of the object to a fully detailed representation of the object.
            **groups (Union(str,List[str]), optional):
                Collection of group identifiers.
            **ignore_warnings (bool, optional):
                Apply changes ignoring warnings. Defaults to False
            **ignore_errors (bool, optional):
                Apply changes ignoring errors. You won't be able to publish such a changes.
                If ignore_warnings flag was omitted - warnings will also be ignored. Defaults to False

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> firewall.network_objects.time.set(uid="d5e8d56f-2d77-4824-a5d2-c4s7885dd4z7",
            ... new_name="timeObject1")
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
            "details_level": str,
            "groups": Union[str, List[str]],
            "ignore_warnings": bool,
            "ignore_errors": bool,
        }
        payload.update(sanitize_secondary_parameters(secondary_parameters, **kw))

        return self._post("set-time", json=payload)

    def delete(self, uid: str = None, name: str = None, **kw) -> Box:
        """
        Delete existing object using object name or uid.

        Args:
            uid (str, optional): Object unique identifier.
            name (str, optional): Object name.

        Keyword Args:
            **details_level (str, optional):
                The level of detail for some of the fields in the response can vary from showing only the UID value\
                of the object to a fully detailed representation of the object.
            **ignore_warnings (bool, optional):
                Apply changes ignoring warnings. Defaults to False
            **ignore_errors (bool, optional):
                Apply changes ignoring errors. You won't be able to publish such a changes.
                If ignore_warnings flag was omitted - warnings will also be ignored. Defaults to False

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> firewall.network_objects.time.delete(uid="d5e8d56f-2d77-4824-a5d2-c4s7885dd4z7")
        """
        return self.delete_object(endpoint="delete-time", uid=uid, name=name, **kw)

    def show_times(
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

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> firewall.network_objects.time.show_times()
        """
        return self.show_objects(
            endpoint="show-times",
            filter_results=filter_results,
            limit=limit,
            offset=offset,
            order=order,
            extra_secondary_parameters={"show_membership": bool},
            **kw
        )
