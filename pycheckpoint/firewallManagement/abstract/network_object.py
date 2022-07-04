from restfly.endpoint import APIEndpoint
from abc import ABC, abstractclassmethod
from box import Box

from ..exception import MandatoryFieldMissing
from pycheckpoint.utils import sanitize_secondary_parameters


class NetworkObjectAPI(ABC, APIEndpoint):
    @abstractclassmethod
    def add(self):
        pass

    def show_object(
        self,
        endpoint: str,
        uid: str = None,
        name: str = None,
        extra_secondary_parameters: dict = None,
        **kw
    ):
        """
        Retrieve existing object using object name or uid.

        Args:
            endpoint (str): Endpoint to reach to show the objects
            uid (str): Object unique identifier.
            name (str): Object name.
            extra_secondary_parameters (dict): Any additional secondary parameter need to be add in the request
        Keyword Args:
            **details-level (str, optional):
                The level of detail for some of the fields in the response can vary from showing only the UID value
                of the object to a fully detailed representation of the object.
        Returns:
            :obj:`Box`: The response from the server
        Examples:
            >>> firewallManagementApi.network_objects.<OBJECT_TYPE>.show(uid="196e93a9-b90b-4ab1-baa6-124e7289aa20")
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

        if extra_secondary_parameters is not None:
            secondary_parameters.update(extra_secondary_parameters)

        payload.update(sanitize_secondary_parameters(secondary_parameters, **kw))

        return self._post(endpoint, json=payload)

    @abstractclassmethod
    def set(self):
        pass

    def delete_object(self, endpoint: str, uid: str = None, name: str = None, **kw):
        """
        Delete existing object using object name or uid.

        Args:
            endpoint (str): Endpoint to reach to show the objects
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
            >>> firewallManagementApi.network_objects.<OBJECT_TYPE>.delete(uid="196e93a9-b90b-4ab1-baa6-124e7289aa20")
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

        return self._post(endpoint, json=payload)

    def show_objects(
        self,
        endpoint: str,
        filter: str = None,
        limit: int = 50,
        offset: int = 0,
        order: list[dict] = None,
        extra_secondary_parameters: dict = None,
        **kw
    ) -> Box:
        """
        Retrieve all objects.

        Args:
            endpoint (str): Endpoint to reach to show the objects
            filter (str): Search expression to filter objects by.
            The provided text should be exactly the same as it would be given in SmartConsole Object Explorer.
            The logical operators in the expression ('AND', 'OR') should be provided in capital letters.
            he search involves both a IP search and a textual search in name, comment, tags etc.
            limit (int): The maximal number of returned results. Default to 50 (between 1 and 500)
            offset (int): Number of the results to initially skip. Default to 0
            order (list[dict]): Sorts results by the given field. By default the results are sorted in the
            descending order by the session publish time.
            extra_secondary_parameters (dict): Any additional secondary parameter need to be add in the request
        Returns:
            :obj:`Box`: The response from the server
        Examples:
            >>> firewallManagementApi.network_objects.<OBJECT_TYPE>.shows_objects()
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
            "details-level": str,
            "domains-to-process": list[str],
        }

        if extra_secondary_parameters is not None:
            secondary_parameters.update(extra_secondary_parameters)

        payload.update(sanitize_secondary_parameters(secondary_parameters, **kw))

        return self._post(endpoint, json=payload)
