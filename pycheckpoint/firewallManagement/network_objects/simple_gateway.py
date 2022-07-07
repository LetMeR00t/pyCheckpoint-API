from typing import Union, List

from box import Box

from ..abstract.network_object import NetworkObjectAPI
from ..exception import MandatoryFieldMissing
from pycheckpoint.utils import sanitize_secondary_parameters
from pycheckpoint.models import Color


class SimpleGatewayAPI(NetworkObjectAPI):
    def add(
        self,
        name: str,
        ip_address: str = None,
        ipv4_address: str = None,
        ipv6_address: str = None,
        anti_bot: bool = None,
        anti_virus: bool = None,
        application_control: bool = None,
        content_awareness: bool = None,
        firewall: bool = None,
        firewall_settings: dict = None,
        icap_server: bool = None,
        interfaces: List[dict] = None,
        ips: bool = None,
        logs_settings: dict = None,
        one_time_password: str = None,
        os_name: str = None,
        platform_portal_settings: dict = None,
        save_logs_locally: bool = None,
        send_alerts_to_server: Union[str, List[str]] = None,
        send_logs_to_backup_server: Union[str, List[str]] = None,
        send_logs_to_server: Union[str, List[str]] = None,
        tags: Union[str, List[str]] = None,
        threat_emulation: bool = None,
        threat_extraction: bool = None,
        threat_prevention_mode: str = None,
        url_filtering: bool = None,
        usercheck_portal_settings: dict = None,
        version: str = None,
        vpn: bool = None,
        vpn_settings: dict = None,
        **kw,
    ) -> Box:
        """
        Create new object.

        Args:
            name (str): Object name. Must be unique in the domain.
            ip_address (str): 	IPv4 or IPv6 address. If both addresses are required use ipv4-address
            and ipv6-address fields explicitly. Mandatory if "ipv4_address" or "ipv6_address" is not set
            ipv4_address (str): IPv4 address. Mandatory if "ipv_address" or "ipv6_address" is not set
            ipv6_address (str): IPv6 address. Mandatory if "ipv_address" or "ipv4_address" is not set
            anti_bot (bool): Anti-Bot blade enabled.
            anti_virus (bool): Anti-Virus blade enabled.
            application_control (bool): Application Control blade enabled.
            content_awareness (bool): Content Awareness blade enabled.
            firewall (bool): Firewall blade enabled.
            firewall_settings (dict): N/A
            icap_server (bool): ICAP Server enabled.
            interfaces (List[dict]): Network interfaces.
            ips (bool): Intrusion Prevention System blade enabled.
            logs_settings (dict): N/A
            one_time_password (str): N/A
            os_name (str): Gateway platform operating system.
            platform_portal_settings (dict): Platform portal settings.
            save_logs_locally (bool): Save logs locally on the gateway.
            send_alerts_to_server (Union[str, List[str]]): Server(s) to send alerts to.
            send_logs_to_backup_server (Union[str, List[str]]): Backup server(s) to send logs to.
            send_logs_to_server (Union[str, List[str]]): Server(s) to send logs to.
            tags (Union(str,List[str])): Collection of tag identifiers.
            threat_emulation (bool): Threat Emulation blade enabled.
            threat_extraction (bool): Threat Extraction blade enabled.
            threat_prevention_mode (str): The mode of Threat Prevention to use. When using Autonomous Threat Prevention,
            disabling the Threat Prevention blades is not allowed.
            url_filtering (bool): URL Filtering blade enabled.
            usercheck_portal_settings (dict): UserCheck portal settings.
            version (str): Gateway platform version.
            vpn (bool): VPN blade enabled.
            vpn_settings (dict): Gateway VPN settings.
        Keyword Args:
            **show-portals-certificate (bool, optional):
                Indicates whether to show the portals certificate value in the reply.
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
            >>>     resp = firewallManagement.network_objects.simple_gateway.add(
        name="gw1", ip_address="192.0.2.1")
        """

        # Main request parameters
        payload = {"name": name}
        if ip_address is not None:
            payload["ip-address"] = ip_address
        elif ipv4_address is not None:
            payload["ipv4-address"] = ipv4_address
        elif ipv6_address is not None:
            payload["ipv6-address"] = ipv6_address
        else:
            raise MandatoryFieldMissing("ip_address or ipv4_address or ipv6_address")

        if anti_bot is not None:
            payload["anti-bot"] = anti_bot
        if anti_virus is not None:
            payload["anti-virus"] = anti_virus
        if application_control is not None:
            payload["application-control"] = application_control
        if content_awareness is not None:
            payload["content-awareness"] = content_awareness
        if firewall is not None:
            payload["firewall"] = firewall
        if firewall_settings is not None:
            payload["firewall-settings"] = firewall_settings
        if icap_server is not None:
            payload["icap-server"] = icap_server
        if interfaces is not None:
            payload["interfaces"] = interfaces
        if ips is not None:
            payload["ips"] = ips
        if logs_settings is not None:
            payload["logs-settings"] = logs_settings
        if one_time_password is not None:
            payload["one-time-password"] = one_time_password
        if os_name is not None:
            payload["os-name"] = os_name
        if platform_portal_settings is not None:
            payload["platform-portal-settings"] = platform_portal_settings
        if tags is not None:
            payload["tags"] = tags
        if save_logs_locally is not None:
            payload["save-logs-locally"] = save_logs_locally
        if send_alerts_to_server is not None:
            payload["send-alerts-to-server"] = send_alerts_to_server
        if send_logs_to_backup_server is not None:
            payload["send-logs-to-backup-server"] = send_logs_to_backup_server
        if send_logs_to_server is not None:
            payload["send-logs-to-server"] = send_logs_to_server
        if tags is not None:
            payload["tags"] = tags
        if threat_emulation is not None:
            payload["threat-emulation"] = threat_emulation
        if threat_extraction is not None:
            payload["threat-extraction"] = threat_extraction
        if threat_prevention_mode is not None:
            payload["threat-prevention-mode"] = threat_prevention_mode
        if url_filtering is not None:
            payload["url-filtering"] = url_filtering
        if usercheck_portal_settings is not None:
            payload["usercheck-portal-settings"] = usercheck_portal_settings
        if version is not None:
            payload["version"] = version
        if vpn is not None:
            payload["vpn"] = vpn
        if vpn_settings is not None:
            payload["vpn-settings"] = vpn_settings

        # Secondary parameters
        secondary_parameters = {
            "show-portals-certificate": bool,
            "color": Color,
            "comments": str,
            "details-level": str,
            "groups": Union[str, List[str]],
            "ignore-warnings": bool,
        }
        payload.update(sanitize_secondary_parameters(secondary_parameters, **kw))

        return self._post("add-simple-gateway", json=payload)

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
            >>> firewallManagementApi.network_objects.simple_gateway.show(
                uid="9423d36f-2d66-4754-b9e2-e7f4493756d4")
        """
        return self.show_object(
            endpoint="show-simple-gateway",
            uid=uid,
            name=name,
            extra_secondary_parameters={"show-portals-certificate": bool},
            **kw,
        )

    def set(
        self,
        uid: str = None,
        name: str = None,
        ip_address: str = None,
        ipv4_address: str = None,
        ipv6_address: str = None,
        anti_bot: bool = None,
        anti_virus: bool = None,
        application_control: bool = None,
        content_awareness: bool = None,
        firewall: bool = None,
        firewall_settings: dict = None,
        icap_server: bool = None,
        interfaces: List[dict] = None,
        ips: bool = None,
        logs_settings: dict = None,
        new_name: str = None,
        one_time_password: str = None,
        os_name: str = None,
        platform_portal_settings: dict = None,
        save_logs_locally: bool = None,
        send_alerts_to_server: Union[str, List[str]] = None,
        send_logs_to_backup_server: Union[str, List[str]] = None,
        send_logs_to_server: Union[str, List[str]] = None,
        tags: Union[str, List[str]] = None,
        threat_emulation: bool = None,
        threat_extraction: bool = None,
        threat_prevention_mode: str = None,
        url_filtering: bool = None,
        usercheck_portal_settings: dict = None,
        version: str = None,
        vpn: bool = None,
        vpn_settings: dict = None,
        **kw,
    ) -> Box:
        """
        Edit existing object using object name or uid.

        Args:
            uid (str): Object unique identifier.
            name (str): Object name.
            ip_address (str): IPv4 or IPv6 address. If both addresses are required use ipv4-address
            and ipv6-address fields explicitly. Mandatory if "ipv4_address" or "ipv6_address" is not set
            ipv4_address (str): IPv4 address. Mandatory if "ipv_address" or "ipv6_address" is not set
            ipv6_address (str): IPv6 address. Mandatory if "ipv_address" or "ipv4_address" is not set
            interfaces (Union[dict,List[dict]]): Host interfaces.
            nat_settings (dict): NAT settings.
            new_name (str): New name of the object.
            tags (Union(str,List[str])): Collection of tag identifiers.
            host_servers (dict): Servers Configuration.
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
            >>> firewallManagement.network_objects.simple_gateway.set(uid="9423d36f-2d66-4754-b9e2-e7f4493756d4",
            ip_address="192.0.2.1")
        """

        # Main request parameters
        payload = {}
        if uid is not None:
            payload["uid"] = uid
        elif name is not None:
            payload["name"] = name
        else:
            raise MandatoryFieldMissing("uid or name")

        if ip_address is not None:
            payload["ip-address"] = ip_address
        elif ipv4_address is not None:
            payload["ipv4-address"] = ipv4_address
        elif ipv6_address is not None:
            payload["ipv6-address"] = ipv6_address

        if anti_bot is not None:
            payload["anti-bot"] = anti_bot
        if anti_virus is not None:
            payload["anti-virus"] = anti_virus
        if application_control is not None:
            payload["application-control"] = application_control
        if content_awareness is not None:
            payload["content-awareness"] = content_awareness
        if firewall is not None:
            payload["firewall"] = firewall
        if firewall_settings is not None:
            payload["firewall-settings"] = firewall_settings
        if icap_server is not None:
            payload["icap-server"] = icap_server
        if interfaces is not None:
            payload["interfaces"] = interfaces
        if ips is not None:
            payload["ips"] = ips
        if logs_settings is not None:
            payload["logs-settings"] = logs_settings
        if new_name is not None:
            payload["new-name"] = new_name
        if one_time_password is not None:
            payload["one-time-password"] = one_time_password
        if os_name is not None:
            payload["os-name"] = os_name
        if platform_portal_settings is not None:
            payload["platform-portal-settings"] = platform_portal_settings
        if tags is not None:
            payload["tags"] = tags
        if save_logs_locally is not None:
            payload["save-logs-locally"] = save_logs_locally
        if send_alerts_to_server is not None:
            payload["send-alerts-to-server"] = send_alerts_to_server
        if send_logs_to_backup_server is not None:
            payload["send-logs-to-backup-server"] = send_logs_to_backup_server
        if send_logs_to_server is not None:
            payload["send-logs-to-server"] = send_logs_to_server
        if tags is not None:
            payload["tags"] = tags
        if threat_emulation is not None:
            payload["threat-emulation"] = threat_emulation
        if threat_extraction is not None:
            payload["threat-extraction"] = threat_extraction
        if threat_prevention_mode is not None:
            payload["threat-prevention-mode"] = threat_prevention_mode
        if url_filtering is not None:
            payload["url-filtering"] = url_filtering
        if usercheck_portal_settings is not None:
            payload["usercheck-portal-settings"] = usercheck_portal_settings
        if version is not None:
            payload["version"] = version
        if vpn is not None:
            payload["vpn"] = vpn
        if vpn_settings is not None:
            payload["vpn-settings"] = vpn_settings

        # Secondary parameters
        secondary_parameters = {
            "show-portals-certificate": bool,
            "color": Color,
            "comments": str,
            "details-level": str,
            "groups": Union[str, List[str]],
            "ignore-warnings": bool,
        }
        payload.update(sanitize_secondary_parameters(secondary_parameters, **kw))

        return self._post("set-simple-gateway", json=payload)

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
            >>> firewallManagementApi.network_objects.simple_gateway.delete(uid="9423d36f-2d66-4754-b9e2-e7f4493756d4")
        """
        return self.delete_object(
            endpoint="delete-simple-gateway", uid=uid, name=name, **kw
        )

    def show_simple_gateways(
        self,
        filter: str = None,
        limit: int = 50,
        offset: int = 0,
        order: List[dict] = None,
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
            order (List[dict]): Sorts results by the given field. By default the results are sorted in the
            descending order by the session publish time.
        Returns:
            :obj:`Box`: The response from the server
        Examples:
            >>> firewallManagementApi.network_objects.simple_gateway.show_simple_gateways()
        """
        return self.show_objects(
            endpoint="show-simple-gateways",
            filter=filter,
            limit=limit,
            offset=offset,
            order=order,
            extra_secondary_parameters={"show-membership": bool},
            **kw,
        )
