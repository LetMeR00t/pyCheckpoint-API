from typing import List, Union

from box import Box
from restfly.endpoint import APIEndpoint

from pycheckpoint_api.models import Color
from pycheckpoint_api.utils import sanitize_secondary_parameters

from ..exception import MandatoryFieldMissing


class PolicyPackage(APIEndpoint):
    def add(
        self,
        name: str,
        access: bool = None,
        desktop_security: bool = None,
        installation_targets: Union[str, List[str]] = None,
        qos: bool = None,
        qos_policy_type: str = None,
        tags: Union[str, List[str]] = None,
        threat_prevention: bool = None,
        vpn_traditional_mode: bool = None,
        **kw,
    ) -> Box:
        """Create new object.

        Args:
            name (str): Object name. Must be unique in the domain.
            access (bool, optional): True - enables, False - disables access & NAT policies, empty - nothing is changed. \
            Defaults to None
            desktop_security (bool, optional): True - enables, False - disables Desktop security policy, empty - nothing \
            is changed. Defaults to None
            installation_targets (Union[str, List[str]], optional): Which Gateways identified by the name or UID to install \
            the policy on. Defaults to None
            qos (bool, optional): True - enables, False - disables QoS policy, empty - nothing is changed. Defaults to None
            qos_policy_type (str, optional): QoS policy type. Defaults to None
            tags (Union[str, List[str]], optional): Collection of tag identifiers. Defaults to None
            threat_prevention (bool, optional): True - enables, False - disables Threat policy, empty - nothing is changed. \
            Defaults to None
            vpn_traditional_mode (bool, optional): True - enables, False - disables VPN traditional mode, empty - nothing is \
            changed. Defaults to None
            **kw (dict, optional): Arbitrary keyword arguments for secondary parameters.

        Keyword Args:
            **color (Color, optional):
                Color of the object. Should be one of existing colors.
            **comments (str, optional):
                Comments string.
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
            >>> management.policy.package.add(
            ... name="New_Standard_Package_1",
            ... comments="My Comments",
            ... color=Color.GREEN,
            ... threat_prevention=False,
            ... access=True,
            ... desktop_security=False,
            ... installation_targets="all",
            ... qos=False,
            ... qos_policy_type="recommanded",
            ... tags=["t1"],
            ... vpn_traditional_mode=False)

        """
        # Main request parameters
        payload = {"name": name}

        if access is not None:
            payload["access"] = access
        if desktop_security is not None:
            payload["desktop-security"] = desktop_security
        if installation_targets is not None:
            payload["installation-targets"] = installation_targets
        if qos is not None:
            payload["qos"] = qos
        if qos_policy_type is not None:
            payload["qos-policy-type"] = qos_policy_type
        if tags is not None:
            payload["tags"] = tags
        if threat_prevention is not None:
            payload["threat-prevention"] = threat_prevention
        if vpn_traditional_mode is not None:
            payload["vpn-traditional-mode"] = vpn_traditional_mode

        # Secondary parameters
        secondary_parameters = {
            "color": Color,
            "comments": str,
            "details-level": str,
            "ignore-warnings": bool,
            "ignore-errors": bool,
        }
        payload.update(sanitize_secondary_parameters(secondary_parameters, **kw))

        return self._post("add-package", json=payload)

    def show(
        self,
        uid: str = None,
        name: str = None,
        **kw,
    ) -> Box:
        """
        Retrieve existing object using object name or uid.

        Args:
            uid (str, optional): Object unique identifier.
            name (str, optional): Object name.

        Keyword Args:
            **details-level (str, optional):
                The level of detail for some of the fields in the response can vary from showing only the UID value\
                of the object to a fully detailed representation of the object.

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> management.policy.package.show(
            ... uid="38b4ed6e-711c-49fa-b9f4-638290d621be")
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

        payload.update(sanitize_secondary_parameters(secondary_parameters, **kw))

        return self._post("show-package", json=payload)

    def set(
        self,
        uid: str = None,
        name: str = None,
        new_name: str = None,
        access: bool = None,
        access_layers: dict = None,
        desktop_security: bool = None,
        https_layer: str = None,
        installation_targets: Union[dict, str, List[str]] = None,
        qos: bool = None,
        qos_policy_type: str = None,
        tags: Union[str, List[str]] = None,
        threat_prevention: bool = None,
        vpn_traditional_mode: bool = None,
        **kw,
    ) -> Box:
        """Edit existing object using object name or uid.

        Args:
            uid (str, optional): Object unique identifier. Defaults to None
            name (str, optional): Object name. Defaults to None
            new_name (str, optional): New name of the object. Defaults to None
            access (bool, optional): True - enables, False - disables access & NAT policies, empty - nothing is changed. \
            Defaults to None
            access_layers (dict, optional): Access policy layers. Defaults to None
            desktop_security (bool, optional): True - enables, False - disables Desktop security policy, empty - nothing \
            is changed. Defaults to None
            https_layer (str, optional): HTTPS inspection policy layer. Defaults to None
            installation_targets (Union[str, List[str]], optional): Which Gateways identified by the name or UID to install \
            the policy on. Defaults to None
            qos (bool, optional): True - enables, False - disables QoS policy, empty - nothing is changed. Defaults to None
            qos_policy_type (str, optional): QoS policy type. Defaults to None
            tags (Union[str, List[str]], optional): Collection of tag identifiers. Defaults to None
            threat_prevention (bool, optional): True - enables, False - disables Threat policy, empty - nothing is changed. \
            Defaults to None
            vpn_traditional_mode (bool, optional): True - enables, False - disables VPN traditional mode, empty - nothing is \
            changed. Defaults to None
            **kw (dict, optional): Arbitrary keyword arguments for secondary parameters.

        Keyword Args:
            **color (Color, optional):
                Color of the object. Should be one of existing colors.
            **comments (str, optional):
                Comments string.
            **details-level (str, optional):
                The level of detail for some of the fields in the response can vary from showing only the UID value\
                of the object to a fully detailed representation of the object.
            **ignore-warnings (bool, optional):
                Apply changes ignoring warnings. Defaults to False
            **ignore-errors (bool, optional):
                Apply changes ignoring errors. You won't be able to publish such a changes.
                If ignore-warnings flag was omitted - warnings will also be ignored. Defaults to False

        Raises:
            MandatoryFieldMissing: The value is not given as a keyword parameter and it's mandatory

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> management.policy.package.set(
            ... uid="38b4ed6e-711c-49fa-b9f4-638290d621be",
            ... new_name="New Standard Package 1",
            ... comments="My Comments",
            ... color=Color.GREEN,
            ... threat_prevention=False,
            ... access=True,
            ... access_layers={"name": "New Standard Package 1 Network"},
            ... desktop_security=False,
            ... installation_targets="all",
            ... qos=False,
            ... qos_policy_type="recommanded",
            ... tags=["t1"],
            ... vpn_traditional_mode=False)
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
        if access is not None:
            payload["access"] = access
        if access_layers is not None:
            payload["access-layers"] = access_layers
        if desktop_security is not None:
            payload["desktop-security"] = desktop_security
        if https_layer is not None:
            payload["https-layer"] = https_layer
        if installation_targets is not None:
            payload["installation-targets"] = installation_targets
        if qos is not None:
            payload["qos"] = qos
        if qos_policy_type is not None:
            payload["qos-policy-type"] = qos_policy_type
        if tags is not None:
            payload["tags"] = tags
        if threat_prevention is not None:
            payload["threat-prevention"] = threat_prevention
        if vpn_traditional_mode is not None:
            payload["vpn-traditional-mode"] = vpn_traditional_mode

        # Secondary parameters
        secondary_parameters = {
            "color": Color,
            "comments": str,
            "details-level": str,
            "ignore-warnings": bool,
            "ignore-errors": bool,
        }
        payload.update(sanitize_secondary_parameters(secondary_parameters, **kw))

        return self._post("set-package", json=payload)

    def delete(
        self,
        uid: str = None,
        name: str = None,
        **kw,
    ) -> Box:
        """
        Delete existing object using object name or uid.

        Args:
            uid (str, optional): Object unique identifier.
            name (str, optional): Object name.

        Keyword Args:
            **details-level (str, optional):
                The level of detail for some of the fields in the response can vary from showing only the UID value\
                of the object to a fully detailed representation of the object.

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> management.policy.package.delete(
            ... uid="38b4ed6e-711c-49fa-b9f4-638290d621be")
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
        }
        payload.update(sanitize_secondary_parameters(secondary_parameters, **kw))

        return self._post("delete-package", json=payload)

    def show_packages(
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
            filter_results (str): Search expression to filter objects by.\
            The provided text should be exactly the same as it would be given in SmartConsole Object Explorer.\
            The logical operators in the expression ('AND', 'OR') should be provided in capital letters.\
            he search involves both a IP search and a textual search in name, comment, tags etc.
            limit (int): The maximal number of returned results. Defaults to 50 (between 1 and 500)
            offset (int): Number of the results to initially skip. Defaults to 0

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
            >>> management.policy.package.show_packages(
            ... filter_results="", order={"ASC": "name"})
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

        # Secondary parameters
        secondary_parameters = {
            "details-level": str,
            "domains-to-process": List[str],
        }

        payload.update(sanitize_secondary_parameters(secondary_parameters, **kw))

        return self._post("show-packages", json=payload)
