from typing import Union, List

from box import Box

from ..abstract.network_object import NetworkObjectAPI
from ..exception import MandatoryFieldMissing
from pycheckpoint_api.utils import sanitize_secondary_parameters
from pycheckpoint_api.models import Color


class ServiceGTPAPI(NetworkObjectAPI):
    def add(
        self,
        name: str,
        version: str = "V2",
        access_point_name: dict = None,
        allow_usage_of_static_ip: bool = True,
        apply_access_policy_on_user_traffic: dict = None,
        cs_fallback_and_srvcc: bool = True,
        imsi_prefix: dict = None,
        interface_profile: dict = None,
        ldap_group: dict = None,
        ms_isdn: dict = None,
        radio_access_technology: dict = None,
        restoration_and_recovery: bool = True,
        reverse_service: bool = False,
        selection_mode: dict = None,
        trace_management: bool = True,
        tags: Union[str, List[str]] = None,
        **kw
    ) -> Box:
        """
        Create new object.

        Args:
            name (str): Object name. Must be unique in the domain.
            version (str): GTP version
            access_point_name (dict): Match by Access Point Name.
            allow_usage_of_static_ip (bool): Allow usage of static IP addresses.
            apply_access_policy_on_user_traffic (dict): Apply Access Policy on user traffic.
            cs_fallback_and_srvcc (bool): CS Fallback and SRVCC (Relevant for V2 only). Default is True.
            imsi_prefix (dict): Match by IMSI prefix.
            interface_profile (dict): Match only message types relevant to the given GTP interface.
            Relevant only for GTP V1 or V2.
            ldap_group (dict): Match by an LDAP Group.
            ms_isdn (dict): Match by an MS-ISDN.
            restoration_and_recovery (bool): Restoration and Recovery (Relevant for V2 only).
            reverse_service (bool): Accept PDUs from the GGSN/PGW to the SGSN/SGW on a previously established PDP context,
            even if different ports are used.
            selection_mode (dict): Match by a selection mode.
            radio_access_technology (dict): Match by Radio Access Technology.
            trace_management (bool): Trace Management (Relevant for V2 only).
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
                Apply changes ignoring warnings. Default is False
            **ignore-errors (bool, optional):
                Apply changes ignoring errors. You won't be able to publish such a changes.
                If ignore-warnings flag was omitted - warnings will also be ignored. Default is False
        Returns:
            :obj:`Box`: The response from the server
        Examples:
            >>>
        """

        # Main request parameters
        payload = {"name": name}

        if version is not None:
            payload["version"] = version
        if access_point_name is not None:
            payload["access-point-name"] = access_point_name
        if allow_usage_of_static_ip is not None:
            payload["allow-usage-of-static-ip"] = allow_usage_of_static_ip
        if apply_access_policy_on_user_traffic is not None:
            payload[
                "apply-access-policy-on-user-traffic"
            ] = apply_access_policy_on_user_traffic
        if cs_fallback_and_srvcc is not None:
            payload["cs-fallback-and-srvcc"] = cs_fallback_and_srvcc
        if imsi_prefix is not None:
            payload["imsi-prefix"] = imsi_prefix
        if interface_profile is not None:
            payload["interface-profile"] = interface_profile
        if ldap_group is not None:
            payload["ldap-group"] = ldap_group
        if ms_isdn is not None:
            payload["ms-isdn"] = ms_isdn
        if restoration_and_recovery is not None:
            payload["restoration-and-recovery"] = restoration_and_recovery
        if reverse_service is not None:
            payload["reverse-service"] = reverse_service
        if radio_access_technology is not None:
            payload["radio-access-technology"] = radio_access_technology
        if selection_mode is not None:
            payload["selection-mode"] = selection_mode
        if trace_management is not None:
            payload["trace-management"] = trace_management
        if tags is not None:
            payload["tags"] = tags

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

        return self._post("add-service-gtp", json=payload)

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
            >>> firewallManagementApi.service_applications.service_gtp.show(uid="ed997ff8-6709-4d71-a713-99bf01711cd5")
        """
        return self.show_object(endpoint="show-service-gtp", uid=uid, name=name, **kw)

    def set(
        self,
        uid: str = None,
        name: str = None,
        new_name: str = None,
        version: str = "V2",
        access_point_name: dict = None,
        allow_usage_of_static_ip: bool = True,
        apply_access_policy_on_user_traffic: dict = None,
        cs_fallback_and_srvcc: bool = True,
        imsi_prefix: dict = None,
        interface_profile: dict = None,
        ldap_group: dict = None,
        ms_isdn: dict = None,
        radio_access_technology: dict = None,
        restoration_and_recovery: bool = True,
        reverse_service: bool = False,
        selection_mode: dict = None,
        trace_management: bool = True,
        tags: Union[str, List[str]] = None,
        **kw
    ) -> Box:
        """
        Edit existing object using object name or uid.

        Args:
            uid (str): Object unique identifier.
            name (str): Object name.
            new_name (str): New name of the object.
            version (str): GTP version
            access_point_name (dict): Match by Access Point Name.
            allow_usage_of_static_ip (bool): Allow usage of static IP addresses.
            apply_access_policy_on_user_traffic (dict): Apply Access Policy on user traffic.
            cs_fallback_and_srvcc (bool): CS Fallback and SRVCC (Relevant for V2 only). Default is True.
            imsi_prefix (dict): Match by IMSI prefix.
            interface_profile (dict): Match only message types relevant to the given GTP interface.
            Relevant only for GTP V1 or V2.
            ldap_group (dict): Match by an LDAP Group.
            ms_isdn (dict): Match by an MS-ISDN.
            restoration_and_recovery (bool): Restoration and Recovery (Relevant for V2 only).
            reverse_service (bool): Accept PDUs from the GGSN/PGW to the SGSN/SGW on a previously established PDP context,
            even if different ports are used.
            selection_mode (dict): Match by a selection mode.
            radio_access_technology (dict): Match by Radio Access Technology.
            trace_management (bool): Trace Management (Relevant for V2 only).
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
                Apply changes ignoring warnings. Default is False
            **ignore-errors (bool, optional):
                Apply changes ignoring errors. You won't be able to publish such a changes.
                If ignore-warnings flag was omitted - warnings will also be ignored. Default is False
        Returns:
            :obj:`Box`: The response from the server
        Examples:
            >>> firewallManagement.service_applications.service_gtp.set(uid="ed997ff8-6709-4d71-a713-99bf01711cd5",
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
        if version is not None:
            payload["version"] = version
        if access_point_name is not None:
            payload["access-point-name"] = access_point_name
        if allow_usage_of_static_ip is not None:
            payload["allow-usage-of-static-ip"] = allow_usage_of_static_ip
        if apply_access_policy_on_user_traffic is not None:
            payload[
                "apply-access-policy-on-user-traffic"
            ] = apply_access_policy_on_user_traffic
        if cs_fallback_and_srvcc is not None:
            payload["cs-fallback-and-srvcc"] = cs_fallback_and_srvcc
        if imsi_prefix is not None:
            payload["imsi-prefix"] = imsi_prefix
        if interface_profile is not None:
            payload["interface-profile"] = interface_profile
        if ldap_group is not None:
            payload["ldap-group"] = ldap_group
        if ms_isdn is not None:
            payload["ms-isdn"] = ms_isdn
        if restoration_and_recovery is not None:
            payload["restoration-and-recovery"] = restoration_and_recovery
        if reverse_service is not None:
            payload["reverse-service"] = reverse_service
        if radio_access_technology is not None:
            payload["radio-access-technology"] = radio_access_technology
        if selection_mode is not None:
            payload["selection-mode"] = selection_mode
        if trace_management is not None:
            payload["trace-management"] = trace_management
        if tags is not None:
            payload["tags"] = tags

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

        return self._post("set-service-gtp", json=payload)

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
            >>> firewallManagementApi.service_applications.service_gtp.delete(uid="ed997ff8-6709-4d71-a713-99bf01711cd5")
        """
        return self.delete_object(
            endpoint="delete-service-gtp", uid=uid, name=name, **kw
        )

    def show_services_gtp(
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
            filter_results (str): Search expression to filter objects by.
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
            >>> firewallManagementApi.service_applications.service_gtp.show_services_gtp()
        """
        return self.show_objects(
            endpoint="show-services-gtp",
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
