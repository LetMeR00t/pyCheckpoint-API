from typing import List, Union

from box import Box

from pycheckpoint_api.models import Color
from pycheckpoint_api.utils import sanitize_secondary_parameters

from ..abstract.network_object import NetworkObject
from ..exception import MandatoryFieldMissing


class ServiceUDP(NetworkObject):
    def add(
        self,
        name: str,
        acccept_replies: bool = None,
        aggressive_aging: dict = None,
        keep_connections_open_after_policy_installation: bool = None,
        match_by_protocol_signature: bool = False,
        match_for_any: bool = None,
        override_default_settings: bool = None,
        port: str = None,
        protocol: str = None,
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
            acccept_replies (bool): N/A
            aggressive_aging (dict): Sets short (aggressive) timeouts for idle connections.
            keep_connections_open_after_policy_installation (bool): Keep connections open after policy has been installed
            even if they are not allowed under the new policy. This overrides the settings in the Connection Persistence page.
            If you change this property, the change will not affect open connections, but only future connections.
            match_by_protocol_signature (bool): A value of true enables matching by the selected protocol's signature -
            the signature identifies the protocol as genuine. Select this option to limit the port to the specified protocol.
            If the selected protocol does not support matching by signature, this field cannot be set to true.
            match_for_any (bool): Indicates whether this service is used when 'Any' is set as the rule's service and there are
            several service objects with the same source port and protocol.
            override_default_settings (bool): Indicates whether this service is a Data Domain service which has been overridden
            port (str): The number of the port used to provide this service.
            To specify a port range, place a hyphen between the lowest and highest port numbers, for example 44-55.
            protocol (str): Select the protocol type associated with the service, and by implication, the management server
            (if any) that enforces Content Security and Authentication for the service.
            Selecting a Protocol Type invokes the specific protocol handlers for each protocol type,
            thus enabling higher level of security by parsing the protocol, and higher level of connectivity
            by tracking dynamic actions (such as opening of ports).
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
                Apply changes ignoring warnings. Defaults to False
            **ignore-errors (bool, optional):
                Apply changes ignoring errors. You won't be able to publish such a changes.
                If ignore-warnings flag was omitted - warnings will also be ignored. Defaults to False
        Returns:
            :obj:`Box`: The response from the server
        Examples:
            >>> firewallManagement.service_applications.service_udp.add(
        name="New_UDP_Service_1",
        port=5669,
        keep_connections_open_after_policy_installation=False,
        session_timeout=0,
        match_for_any=True,
        sync_connections_on_cluster=True,
        aggressive_aging={"enable": True, "timeout": 360, "use-default-timeout": False})
        """

        # Main request parameters
        payload = {"name": name}

        if acccept_replies is not None:
            payload["acccept-replies"] = acccept_replies
        if aggressive_aging is not None:
            payload["aggressive-aging"] = aggressive_aging
        if keep_connections_open_after_policy_installation is not None:
            payload[
                "keep-connections-open-after-policy-installation"
            ] = keep_connections_open_after_policy_installation
        if match_by_protocol_signature is not None:
            payload["match-by-protocol-signature"] = match_by_protocol_signature
        if match_for_any is not None:
            payload["match-for-any"] = match_for_any
        if override_default_settings is not None:
            payload["override-default-settings"] = override_default_settings
        if port is not None:
            payload["port"] = port
        if protocol is not None:
            payload["protocol"] = protocol
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

        return self._post("add-service-udp", json=payload)

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
            >>> FirewallManagement.service_applications.service_udp.show(uid="ed997ff8-6709-4d71-a713-99bf01711cd5")
        """
        return self.show_object(endpoint="show-service-udp", uid=uid, name=name, **kw)

    def set(
        self,
        uid: str = None,
        name: str = None,
        new_name: str = None,
        acccept_replies: bool = None,
        aggressive_aging: dict = None,
        keep_connections_open_after_policy_installation: bool = None,
        match_by_protocol_signature: bool = False,
        match_for_any: bool = None,
        override_default_settings: bool = None,
        port: str = None,
        protocol: str = None,
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
            name (str): Object name.
            new_name (str): New name of the object.
            acccept_replies (bool): N/A
            aggressive_aging (dict): Sets short (aggressive) timeouts for idle connections.
            keep_connections_open_after_policy_installation (bool): Keep connections open after policy has been installed
            even if they are not allowed under the new policy. This overrides the settings in the Connection Persistence page.
            If you change this property, the change will not affect open connections, but only future connections.
            match_by_protocol_signature (bool): A value of true enables matching by the selected protocol's signature -
            the signature identifies the protocol as genuine. Select this option to limit the port to the specified protocol.
            If the selected protocol does not support matching by signature, this field cannot be set to true.
            match_for_any (bool): Indicates whether this service is used when 'Any' is set as the rule's service and there are
            several service objects with the same source port and protocol.
            override_default_settings (bool): Indicates whether this service is a Data Domain service which has been overridden
            port (str): The number of the port used to provide this service.
            To specify a port range, place a hyphen between the lowest and highest port numbers, for example 44-55.
            protocol (str): Select the protocol type associated with the service, and by implication, the management server
            (if any) that enforces Content Security and Authentication for the service.
            Selecting a Protocol Type invokes the specific protocol handlers for each protocol type,
            thus enabling higher level of security by parsing the protocol, and higher level of connectivity
            by tracking dynamic actions (such as opening of ports).
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
                Apply changes ignoring warnings. Defaults to False
            **ignore-errors (bool, optional):
                Apply changes ignoring errors. You won't be able to publish such a changes.
                If ignore-warnings flag was omitted - warnings will also be ignored. Defaults to False
        Returns:
            :obj:`Box`: The response from the server
        Examples:
            >>> firewallManagement.service_applications.service_udp.set(uid="ed997ff8-6709-4d71-a713-99bf01711cd5",
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
        if acccept_replies is not None:
            payload["acccept-replies"] = acccept_replies
        if aggressive_aging is not None:
            payload["aggressive-aging"] = aggressive_aging
        if keep_connections_open_after_policy_installation is not None:
            payload[
                "keep-connections-open-after-policy-installation"
            ] = keep_connections_open_after_policy_installation
        if match_by_protocol_signature is not None:
            payload["match-by-protocol-signature"] = match_by_protocol_signature
        if match_for_any is not None:
            payload["match-for-any"] = match_for_any
        if override_default_settings is not None:
            payload["override-default-settings"] = override_default_settings
        if port is not None:
            payload["port"] = port
        if protocol is not None:
            payload["protocol"] = protocol
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

        return self._post("set-service-udp", json=payload)

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
                Apply changes ignoring warnings. Defaults to False
            **ignore-errors (bool, optional):
                Apply changes ignoring errors. You won't be able to publish such a changes.
                If ignore-warnings flag was omitted - warnings will also be ignored. Defaults to False
        Returns:
            :obj:`Box`: The response from the server
        Examples:
            >>> FirewallManagement.service_applications.service_udp.delete(uid="ed997ff8-6709-4d71-a713-99bf01711cd5")
        """
        return self.delete_object(
            endpoint="delete-service-udp", uid=uid, name=name, **kw
        )

    def show_services_udp(
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
            show_as_ranges (bool, optional): When true, the group's matched content is displayed as ranges of IP addresses rather\
            than network objects. Objects that are not represented using IP addresses are presented as objects.\
            The 'members' parameter is omitted from the response and instead the 'ranges' parameter is displayed.\
            Defaults to False.
        Keyword Args:
            **details-level (str, optional):
                The level of detail for some of the fields in the response can vary from showing only the UID value
                of the object to a fully detailed representation of the object.
            **domains-to-process (List[str], optional):
                Indicates which domains to process the commands on. It cannot be used with the details-level full,
                must be run from the System Domain only and with ignore-warnings true.
                Valid values are: CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER.
            **show-membership (bool, optional):
                Indicates whether to calculate and show "groups" field for every object in reply.
        Returns:
            :obj:`Box`: The response from the server
        Examples:
            >>> FirewallManagement.service_applications.service_udp.shows_services_udp()
        """
        return self.show_objects(
            endpoint="show-services-udp",
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
