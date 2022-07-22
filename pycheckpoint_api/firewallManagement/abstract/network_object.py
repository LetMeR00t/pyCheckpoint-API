import logging
import time
from typing import List

from box import Box
from restfly.endpoint import APIEndpoint

from pycheckpoint_api.utils import sanitize_secondary_parameters

from ..exception import MandatoryFieldMissing

logger = logging.getLogger(__name__)


class NetworkObject(APIEndpoint):
    """This class is used to create a common shape for any network object"""

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
            uid (str, optional): Object unique identifier. Defaults to None
            name (str, optional): Object name. Defaults to None
            extra_secondary_parameters (dict): Any additional secondary parameter need to be add in the request
            **kw (dict, optional): Arbitrary keyword arguments for secondary parameters.

        Keyword Args:
            **details-level (str, optional):
                The level of detail for some of the fields in the response can vary from showing only the UID value\
                of the object to a fully detailed representation of the object.

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> firewall.network_objects.<OBJECT_TYPE>.show(uid="196e93a9-b90b-4ab1-baa6-124e7289aa20")

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
            uid (str, optional): Object unique identifier. Defaults to None
            name (str, optional): Object name. Defaults to None
            **kw (dict, optional): Arbitrary keyword arguments for secondary parameters.

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
            >>> firewall.network_objects.<OBJECT_TYPE>.delete(uid="196e93a9-b90b-4ab1-baa6-124e7289aa20")

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
        show_all: bool = False,
        filter_results: str = None,
        limit: int = 50,
        offset: int = 0,
        order: List[dict] = None,
        show_as_ranges: bool = None,
        extra_secondary_parameters: dict = None,
        **kw
    ) -> Box:
        """
        Retrieve objects.

        Args:
            endpoint (str): Endpoint to reach to show the objects
            show_all (bool, optional): Indicates if you want to shown all objects or not. If yes, `offset `will be ignored.\
            Defaults to False
            filter_results (str, optional): Search expression to filter objects by. Defaults to None
            The provided text should be exactly the same as it would be given in SmartConsole Object Explorer.
            The logical operators in the expression ('AND', 'OR') should be provided in capital letters.
            he search involves both a IP search and a textual search in name, comment, tags etc.
            limit (int, optional): The maximal number of returned results. Defaults to 50 (between 1 and 500)
            offset (int, optional): Number of the results to initially skip. Defaults to 0
            order (List[dict], optional): Sorts results by the given field. By default the results are sorted in the
            descending order by the session publish time. Defaults to None
            extra_secondary_parameters (dict, optional): Any additional secondary parameter need to be add in the request
            Defaults to None
            **kw (dict, optional): Arbitrary keyword arguments for secondary parameters.

        Keyword Args:
            **details-level (str, optional):
                The level of detail for some of the fields in the response can vary from showing only the UID value\
                of the object to a fully detailed representation of the object.
            **domains-to-process (List[str], optional):
                Indicates which domains to process the commands on. It cannot be used with the details-level full,\
                must be run from the System Domain only and with ignore-warnings true.\
                Valid values are: CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER.

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> firewall.network_objects.<OBJECT_TYPE>.show_<OBJECT_TYPE>s()

        """
        if show_all:
            return self.show_all_objects(
                endpoint=endpoint,
                filter_results=filter_results,
                limit=limit,
                order=order,
                show_as_ranges=show_as_ranges,
                extra_secondary_parameters=extra_secondary_parameters,
                **kw
            )
        else:
            return self.show_partial_objects(
                endpoint=endpoint,
                filter_results=filter_results,
                limit=limit,
                offset=offset,
                order=order,
                show_as_ranges=show_as_ranges,
                extra_secondary_parameters=extra_secondary_parameters,
                **kw
            )

    def show_partial_objects(
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
        """Retrieve partially objects

        Args:
            endpoint (str): _description_
            filter_results (str, optional): _description_ Defaults to None
            limit (int, optional): _description_ Defaults to 50
            order (List[dict], optional): _description_ Defaults to None
            show_as_ranges (bool, optional): _description_ Defaults to None
            extra_secondary_parameters (dict, optional): _description_ Defaults to None
            **kw (dict, optional): Arbitrary keyword arguments for secondary parameters.

        Keyword Args:
            **details-level (str, optional):
                The level of detail for some of the fields in the response can vary from showing only the UID value\
                of the object to a fully detailed representation of the object.
            **domains-to-process (List[str], optional):
                Indicates which domains to process the commands on. It cannot be used with the details-level full,\
                must be run from the System Domain only and with ignore-warnings true.\
                Valid values are: CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER.

        Returns:
            obj:`Box`: The response from the server

        Examples:
            >>> firewall.network_objects.<OBJECT_TYPE>.show_partial_<OBJECT_TYPE>s()

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

    def show_all_objects(
        self,
        endpoint: str,
        filter_results: str = None,
        limit: int = 50,
        order: List[dict] = None,
        show_as_ranges: bool = None,
        extra_secondary_parameters: dict = None,
        **kw
    ) -> Box:
        """Retrieve all objects

        Args:
            endpoint (str): _description_
            filter_results (str, optional): _description_ Defaults to None
            limit (int, optional): _description_ Defaults to 50
            order (List[dict], optional): _description_ Defaults to None
            show_as_ranges (bool, optional): _description_ Defaults to None
            extra_secondary_parameters (dict, optional): _description_ Defaults to None
            **kw (dict, optional): Arbitrary keyword arguments for secondary parameters.

        Keyword Args:
            **details-level (str, optional):
                The level of detail for some of the fields in the response can vary from showing only the UID value\
                of the object to a fully detailed representation of the object.
            **domains-to-process (List[str], optional):
                Indicates which domains to process the commands on. It cannot be used with the details-level full,\
                must be run from the System Domain only and with ignore-warnings true.\
                Valid values are: CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER.

        Returns:
            obj:`Box`: The response from the server

        Examples:
            >>> firewall.network_objects.<OBJECT_TYPE>.show_all_<OBJECT_TYPE>s()

        """
        all_objects = None

        # Get a timer
        timer_start = time.time()

        # Made a first request to determine the total number of objects
        resp = self.show_partial_objects(
            endpoint=endpoint,
            filter_results=filter_results,
            limit=limit,
            offset=0,
            order=order,
            show_as_ranges=show_as_ranges,
            extra_secondary_parameters=extra_secondary_parameters,
            **kw
        )

        # Add the first results
        all_objects = resp

        # Evaluate the number of requests to be done
        number_requests = int(resp.total / limit) + 1

        logger.info(
            endpoint
            + " - Total: "
            + str(resp.total)
            + " - Number of requests to do: "
            + str(number_requests)
            + " (limit set to "
            + str(limit)
            + "/request) - In progress..."
        )
        logger.debug(
            endpoint
            + " - 1/"
            + str(number_requests)
            + " (limit set to "
            + str(limit)
            + "/request) exported... (offset:0)"
        )

        for i in range(1, number_requests):
            resp = self.show_partial_objects(
                endpoint=endpoint,
                filter_results=filter_results,
                limit=limit,
                offset=i * limit,
                order=order,
                show_as_ranges=show_as_ranges,
                extra_secondary_parameters=extra_secondary_parameters,
                **kw
            )

            logger.debug(
                endpoint
                + " - "
                + str(i + 1)
                + "/"
                + str(number_requests)
                + " (limit set to "
                + str(limit)
                + "/request) exported... (offset:"
                + str(i)
                + ")"
            )

            all_objects.objects += resp.objects

        # Finalize the output
        all_objects.to = all_objects.total

        # End timer
        timer_diff = time.time() - timer_start

        timer_text = ""

        if round(timer_diff % 60) != 0:
            timer_text = (
                str(int(timer_diff / 60)) + "min " + str(round(timer_diff % 60)) + "s)"
            )  # pragma: no cover
        else:
            timer_text = "<1s"

        logger.info(
            endpoint
            + " - Total: "
            + str(resp.total)
            + " - Number of requests done: "
            + str(number_requests)
            + " (limit set to "
            + str(limit)
            + "/request) - Done in "
            + timer_text
        )

        return all_objects
