from typing import List, Union

from box import Box

from pycheckpoint_api.models import Color
from pycheckpoint_api.utils import sanitize_secondary_parameters

from ..abstract.network_object import NetworkObject
from ..exception import MandatoryFieldMissing


class CheckpointHost(NetworkObject):
    def add(
        self,
        name: str,
        ip_address: str = None,
        ipv4_address: str = None,
        ipv6_address: str = None,
        interfaces: Union[dict, List[dict]] = None,
        nat_settings: dict = None,
        one_time_password: str = None,
        hardware: str = None,
        os: str = None,
        version: str = None,
        management_blades: dict = None,
        logs_settings: dict = None,
        save_logs_locally: bool = None,
        send_alerts_to_server: Union[str, List[str]] = None,
        send_logs_to_backup_server: Union[str, List[str]] = None,
        send_logs_to_server: Union[str, List[str]] = None,
        tags: Union[str, List[str]] = None,
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
            interfaces (Union[dict, List[dict]]): Check Point host interfaces.
            nat_settings (dict): NAT settings.
            one_time_password (str): Secure internal connection one time password.
            hardware (str): Hardware name.
            os (str): Operating system name.
            version (str): Check Point host platform version.
            management_blades (dict): Management blades.
            logs_settings (dict): Logs settings.
            save_logs_locally (bool): Save logs locally on the gateway.
            send_alerts_to_server (Union[str, List[str]]): Server(s) to send alerts to.
            send_logs_to_backup_server (Union[str, List[str]]): Backup server(s) to send logs to.
            send_logs_to_server (Union[str, List[str]]): Server(s) to send logs to.
            tags (Union(str,List[str])): Collection of tag identifiers.
        Keyword Args:
            **set-if-exists (bool, optional):
                If another object with the same identifier already exists, it will be updated.
                The command behaviour will be the same as if originally a set command was called.
                Pay attention that original object's fields will be overwritten by the fields
                provided in the request payload!
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
            >>> firewallManagement.network_objects.checkpoint_host.add(
        name="secondarylogserver",
        ipv4_address="5.5.5.5",
        management_blades={
            "network-policy-management": True,
            "logging-and-status": True,
        },)
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

        if hardware is not None:
            payload["hardware"] = hardware
        if interfaces is not None:
            payload["interfaces"] = interfaces
        if nat_settings is not None:
            payload["nat-settings"] = nat_settings
        if one_time_password is not None:
            payload["one-time-password"] = one_time_password
        if os is not None:
            payload["os"] = os
        if version is not None:
            payload["version"] = version
        if management_blades is not None:
            payload["management-blades"] = management_blades
        if logs_settings is not None:
            payload["logs-settings"] = logs_settings
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

        # Secondary parameters
        secondary_parameters = {
            "set-if-exists": bool,
            "color": Color,
            "comments": str,
            "details-level": str,
            "groups": Union[str, List[str]],
            "ignore-warnings": bool,
        }
        payload.update(sanitize_secondary_parameters(secondary_parameters, **kw))

        return self._post("add-checkpoint-host", json=payload)

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
            >>> FirewallManagement.network_objects.checkpoint_host.show(
                uid="9423d36f-2d66-4754-b9e2-e7f4493756d4")
        """
        return self.show_object(
            endpoint="show-checkpoint-host",
            uid=uid,
            name=name,
            **kw,
        )

    def set(
        self,
        uid: str = None,
        name: str = None,
        ip_address: str = None,
        ipv4_address: str = None,
        ipv6_address: str = None,
        interfaces: Union[dict, List[dict]] = None,
        nat_settings: dict = None,
        new_name: str = None,
        one_time_password: str = None,
        hardware: str = None,
        os: str = None,
        version: str = None,
        management_blades: dict = None,
        logs_settings: dict = None,
        save_logs_locally: bool = None,
        send_alerts_to_server: Union[str, List[str]] = None,
        send_logs_to_backup_server: Union[str, List[str]] = None,
        send_logs_to_server: Union[str, List[str]] = None,
        tags: Union[str, List[str]] = None,
        **kw,
    ) -> Box:
        """
        Edit existing object using object name or uid.

        Args:
            uid (str): Object unique identifier.
            name (str): Object name. Must be unique in the domain.
            ip_address (str): 	IPv4 or IPv6 address. If both addresses are required use ipv4-address
            and ipv6-address fields explicitly. Mandatory if "ipv4_address" or "ipv6_address" is not set
            ipv4_address (str): IPv4 address. Mandatory if "ipv_address" or "ipv6_address" is not set
            ipv6_address (str): IPv6 address. Mandatory if "ipv_address" or "ipv4_address" is not set
            interfaces (Union[dict, List[dict]]): Check Point host interfaces.
            nat_settings (dict): NAT settings.
            new_name (str): New name of the object.
            one_time_password (str): Secure internal connection one time password.
            hardware (str): Hardware name.
            os (str): Operating system name.
            version (str): Check Point host platform version.
            management_blades (dict): Management blades.
            logs_settings (dict): Logs settings.
            save_logs_locally (bool): Save logs locally on the gateway.
            send_alerts_to_server (Union[str, List[str]]): Server(s) to send alerts to.
            send_logs_to_backup_server (Union[str, List[str]]): Backup server(s) to send logs to.
            send_logs_to_server (Union[str, List[str]]): Server(s) to send logs to.
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
                Apply changes ignoring warnings. Defaults to False
            **ignore-errors (bool, optional):
                Apply changes ignoring errors. You won't be able to publish such a changes.
                If ignore-warnings flag was omitted - warnings will also be ignored. Defaults to False
        Returns:
            :obj:`Box`: The response from the server
        Examples:
            >>> firewallManagement.network_objects.checkpoint_host.set(
        uid="f50f3810-d16c-4239-88d0-9f37ac581387", ip_address="5.5.5.5")
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

        if hardware is not None:
            payload["hardware"] = hardware
        if interfaces is not None:
            payload["interfaces"] = interfaces
        if nat_settings is not None:
            payload["nat-settings"] = nat_settings
        if new_name is not None:
            payload["new-name"] = new_name
        if one_time_password is not None:
            payload["one-time-password"] = one_time_password
        if os is not None:
            payload["os"] = os
        if version is not None:
            payload["version"] = version
        if management_blades is not None:
            payload["management-blades"] = management_blades
        if logs_settings is not None:
            payload["logs-settings"] = logs_settings
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

        return self._post("set-checkpoint-host", json=payload)

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
            >>> FirewallManagement.network_objects.checkpoint_host.delete(uid="9423d36f-2d66-4754-b9e2-e7f4493756d4")
        """
        return self.delete_object(
            endpoint="delete-checkpoint-host", uid=uid, name=name, **kw
        )

    def show_checkpoint_hosts(
        self,
        filter_results: str = None,
        limit: int = 50,
        offset: int = 0,
        order: List[dict] = None,
        **kw,
    ) -> Box:
        """
        Retrieve all objects.

        Args:
            filter_results (str): Search expression to filter objects by.
            The provided text should be exactly the same as it would be given in SmartConsole Object Explorer.
            The logical operators in the expression ('AND', 'OR') should be provided in capital letters.
            he search involves both a IP search and a textual search in name, comment, tags etc.
            limit (int): The maximal number of returned results. Defaults to 50 (between 1 and 500)
            offset (int): Number of the results to initially skip. Defaults to 0
            order (List[dict]): Sorts results by the given field. By default the results are sorted in the
            descending order by the session publish time.
        Returns:
            :obj:`Box`: The response from the server
        Examples:
            >>> FirewallManagement.network_objects.checkpoint_host.show_checkpoint_hosts()
        """
        return self.show_objects(
            endpoint="show-checkpoint-hosts",
            filter_results=filter_results,
            limit=limit,
            offset=offset,
            order=order,
            extra_secondary_parameters={"show-membership": bool},
            **kw,
        )
