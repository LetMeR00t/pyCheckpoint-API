from typing import Union, List

from box import Box

from ..abstract.network_object import NetworkObjectAPI
from ..exception import MandatoryFieldMissing
from pycheckpoint_api.utils import sanitize_secondary_parameters
from pycheckpoint_api.models import Color


class ServiceSCTPAPI(NetworkObjectAPI):
    def add(
        self,
        name: str,
        port: str,
        aggressive_aging: dict = None,
        keep_connections_open_after_policy_installation: bool = None,
        match_for_any: bool = None,
        session_timeout: int = None,
        source_port: str = None,
        sync_connections_on_cluster: bool = None,
        tags: Union[str, List[str]] = None,
        use_default_session_timeout: bool = None,
        **kw
    ) -> Box:
        """
        Create new object.

        Args:
            name (str): Object name. Must be unique in the domain.
            port (str): The number of the port used to provide this service.
            To specify a port range, place a hyphen between the lowest and highest port numbers, for example 44-55.
            aggressive_aging (dict): Sets short (aggressive) timeouts for idle connections.
            keep_connections_open_after_policy_installation (bool): Keep connections open after policy has been installed
            even if they are not allowed under the new policy. This overrides the settings in the Connection Persistence page.
            If you change this property, the change will not affect open connections, but only future connections.
            match_for_any (bool): Indicates whether this service is used when 'Any' is set as the rule's service and there are
            several service objects with the same source port and protocol.
            session_timeout (int): Time (in seconds) before the session times out.
            source_port (str): Port number for the client side service. If specified, only those Source port Numbers will be
            Accepted, Dropped, or Rejected during packet inspection. Otherwise, the source port is not inspected.
            sync_connections_on_cluster (bool): Enables state-synchronized High Availability or Load Sharing on a ClusterXL
            or OPSEC-certified cluster.
            tags (Union(str,List[str])): Collection of tag identifiers.
            use_default_session_timeout (bool): Use default virtual session timeout.
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
                Apply changes ignoring warnings. Default is False
            **ignore-errors (bool, optional):
                Apply changes ignoring errors. You won't be able to publish such a changes.
                If ignore-warnings flag was omitted - warnings will also be ignored. Default is False
        Returns:
            :obj:`Box`: The response from the server
        Examples:
            >>> firewallManagement.service_applications.service_sctp.add(
        name="New_SCTP_Service_1",
        port=5669,
        keep_connections_open_after_policy_installation=False,
        session_timeout=0,
        match_for_any=True,
        sync_connections_on_cluster=True,
        aggressive_aging={"enable": True, "timeout": 360, "use-default-timeout": False})
        """

        # Main request parameters
        payload = {"name": name, "port": port}

        if aggressive_aging is not None:
            payload["aggressive-aging"] = aggressive_aging
        if keep_connections_open_after_policy_installation is not None:
            payload[
                "keep-connections-open-after-policy-installation"
            ] = keep_connections_open_after_policy_installation
        if match_for_any is not None:
            payload["match-for-any"] = match_for_any
        if session_timeout is not None:
            payload["session-timeout"] = session_timeout
        if source_port is not None:
            payload["source-port"] = source_port
        if sync_connections_on_cluster is not None:
            payload["sync-connections-on-cluster"] = sync_connections_on_cluster
        if tags is not None:
            payload["tags"] = tags
        if use_default_session_timeout is not None:
            payload["use-default-session-timeout"] = use_default_session_timeout

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

        return self._post("add-service-sctp", json=payload)

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
            >>> firewallManagementApi.service_applications.service_sctp.show(uid="ed997ff8-6709-4d71-a713-99bf01711cd5")
        """
        return self.show_object(endpoint="show-service-sctp", uid=uid, name=name, **kw)

    def set(
        self,
        uid: str = None,
        name: str = None,
        new_name: str = None,
        port: str = None,
        aggressive_aging: dict = None,
        keep_connections_open_after_policy_installation: bool = None,
        match_for_any: bool = None,
        session_timeout: int = None,
        source_port: str = None,
        sync_connections_on_cluster: bool = None,
        tags: Union[str, List[str]] = None,
        use_default_session_timeout: bool = None,
        **kw
    ) -> Box:
        """
        Edit existing object using object name or uid.

        Args:
            uid (str): Object unique identifier.
            new_name (str): New name of the object.
            name (str): Object name. Must be unique in the domain.
            port (str): The number of the port used to provide this service.
            To specify a port range, place a hyphen between the lowest and highest port numbers, for example 44-55.
            aggressive_aging (dict): Sets short (aggressive) timeouts for idle connections.
            keep_connections_open_after_policy_installation (bool): Keep connections open after policy has been installed
            even if they are not allowed under the new policy. This overrides the settings in the Connection Persistence page.
            If you change this property, the change will not affect open connections, but only future connections.
            match_for_any (bool): Indicates whether this service is used when 'Any' is set as the rule's service and there are
            several service objects with the same source port and protocol.
            session_timeout (int): Time (in seconds) before the session times out.
            source_port (str): Port number for the client side service. If specified, only those Source port Numbers will be
            Accepted, Dropped, or Rejected during packet inspection. Otherwise, the source port is not inspected.
            sync_connections_on_cluster (bool): Enables state-synchronized High Availability or Load Sharing on a ClusterXL
            or OPSEC-certified cluster.
            tags (Union(str,List[str])): Collection of tag identifiers.
            use_default_session_timeout (bool): Use default virtual session timeout.
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
            >>> firewallManagement.service_applications.service_sctp.set(uid="ed997ff8-6709-4d71-a713-99bf01711cd5",
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
        if aggressive_aging is not None:
            payload["aggressive-aging"] = aggressive_aging
        if keep_connections_open_after_policy_installation is not None:
            payload[
                "keep-connections-open-after-policy-installation"
            ] = keep_connections_open_after_policy_installation
        if match_for_any is not None:
            payload["match-for-any"] = match_for_any
        if port is not None:
            payload["port"] = port
        if session_timeout is not None:
            payload["session-timeout"] = session_timeout
        if source_port is not None:
            payload["source-port"] = source_port
        if sync_connections_on_cluster is not None:
            payload["sync-connections-on-cluster"] = sync_connections_on_cluster
        if tags is not None:
            payload["tags"] = tags
        if use_default_session_timeout is not None:
            payload["use-default-session-timeout"] = use_default_session_timeout

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

        return self._post("set-service-sctp", json=payload)

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
            >>> firewallManagementApi.service_applications.service_sctp.delete(uid="ed997ff8-6709-4d71-a713-99bf01711cd5")
        """
        return self.delete_object(
            endpoint="delete-service-sctp", uid=uid, name=name, **kw
        )

    def show_services_sctp(
        self,
        filter: str = None,
        limit: int = 50,
        offset: int = 0,
        order: List[dict] = None,
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
            >>> firewallManagementApi.service_applications.service_sctp.shows_services_sctp()
        """
        return self.show_objects(
            endpoint="show-services-sctp",
            filter=filter,
            limit=limit,
            offset=offset,
            order=order,
            extra_secondary_parameters={
                "show-membership": bool,
                "domains-to-process": List[str],
            },
            **kw
        )
