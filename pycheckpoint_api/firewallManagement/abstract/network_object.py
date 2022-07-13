from restfly.endpoint import APIEndpoint
from box import Box
from typing import List

from ..exception import MandatoryFieldMissing
from pycheckpoint_api.utils import sanitize_secondary_parameters


class NetworkObject(APIEndpoint):
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
            >>> FirewallManagement.network_objects.<OBJECT_TYPE>.show(uid="196e93a9-b90b-4ab1-baa6-124e7289aa20")
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
            >>> FirewallManagement.network_objects.<OBJECT_TYPE>.delete(uid="196e93a9-b90b-4ab1-baa6-124e7289aa20")
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
        filter_results: str = None,
        limit: int = 50,
        offset: int = 0,
        order: List[dict] = None,
        show_as_ranges: bool = None,
        extra_secondary_parameters: dict = None,
        **kw
    ) -> Box:
        """
        Retrieve all objects.

        Args:
            endpoint (str): Endpoint to reach to show the objects
            filter_results (str): Search expression to filter objects by.
            The provided text should be exactly the same as it would be given in SmartConsole Object Explorer.
            The logical operators in the expression ('AND', 'OR') should be provided in capital letters.
            he search involves both a IP search and a textual search in name, comment, tags etc.
            limit (int): The maximal number of returned results. Default to 50 (between 1 and 500)
            offset (int): Number of the results to initially skip. Default to 0
            order (List[dict]): Sorts results by the given field. By default the results are sorted in the
            descending order by the session publish time.
            extra_secondary_parameters (dict): Any additional secondary parameter need to be add in the request
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
            >>> FirewallManagement.network_objects.<OBJECT_TYPE>.shows_objects()
        """

        # Main request parameters
        payload = {}
        if filter_results is not None:
            payload["filter"] = filter_results
        if limit is not None:
            payload["limit"] = limit
        if offset is not None:
            payload["offset"] = offset
        if order is not None:
            payload["order"] = order
        if show_as_ranges is not None:
            payload["show-as-ranges"] = show_as_ranges

        # Secondary parameters
        secondary_parameters = {
            "details-level": str,
            "domains-to-process": List[str],
        }

        if extra_secondary_parameters is not None:
            secondary_parameters.update(extra_secondary_parameters)

        payload.update(sanitize_secondary_parameters(secondary_parameters, **kw))

        return self._post(endpoint, json=payload)
