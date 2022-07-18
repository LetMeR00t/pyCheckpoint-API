from typing import List, Union

from box import Box
from restfly.endpoint import APIEndpoint

from pycheckpoint_api.utils import sanitize_secondary_parameters

from ..exception import MandatoryFieldMissing


class NATRule(APIEndpoint):
    def add(
        self,
        package: str,
        position: Union[int, str, dict],
        name: str = None,
        enabled: bool = False,
        install_on: Union[str, List[str]] = None,
        method: str = None,
        original_destination: str = None,
        original_service: str = None,
        original_source: str = None,
        translated_destination: str = None,
        translated_service: str = None,
        translated_source: str = None,
        **kw,
    ) -> Box:
        """
        Create new object.

        Args:
            package (str): Name of the package.
            position (Union[int, str, dict]): Position in the rulebase. If an integer is provided, it will add the rule
            at the specific position. If a string is provided, it will add the rule at the position mentioned in the
            valid values ("top" or "bottom"). Otherwise, you can provide a dictionnary to explain more complex position
            (see the API documentation).
            name (str): Rule name.
            enabled (bool): Enable/Disable the rule.
            install_on (Union[str, List[str]]): Which Gateways identified by the name or UID to install the policy on.
            method (str): Nat method. Valid values are "static", "hide", "nat64", "nat46" and "cgnat"
            original_destination (str): Original destination.
            original_service (str): Original service.
            original_source (str): 	Original source.
            translated_destination (str): Translated destination.
            translated_service (str): Translated service.
            translated_source (str): Translated service.
        Keyword Args:
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
            >>> firewallManagement.access_control_nat.nat_rule.add(
        package="standard",
        position="top",
        name="New NAT Rule 1",
        enabled=True,
        install_on="6c488338-8eec-4103-ad21-cd461ac2c476",
        method="static",
        original_destination="Any",
        original_service="New_TCP_Service_1",
        original_source="Any",
        translated_destination="Any",
        translated_service="New_TCP_Service_1",
        translated_source="Any",)
        """

        # Main request parameters
        payload = {"package": package, "position": position}

        if name is not None:
            payload["name"] = name
        if enabled is not None:
            payload["enabled"] = enabled
        if install_on is not None:
            payload["install-on"] = install_on
        if method is not None:
            payload["method"] = method
        if original_destination is not None:
            payload["original-destination"] = original_destination
        if original_service is not None:
            payload["original-service"] = original_service
        if original_source is not None:
            payload["original-source"] = original_source
        if translated_destination is not None:
            payload["translated-destination"] = translated_destination
        if translated_service is not None:
            payload["translated-service"] = translated_service
        if translated_source is not None:
            payload["translated-source"] = translated_source

        # Secondary parameters
        secondary_parameters = {
            "comments": str,
            "details-level": str,
            "ignore-warnings": bool,
            "ignore-errors": bool,
        }
        payload.update(sanitize_secondary_parameters(secondary_parameters, **kw))

        return self._post("add-nat-rule", json=payload)

    def show(
        self,
        package: str,
        uid: str = None,
        name: str = None,
        rule_number: int = None,
        **kw,
    ) -> Box:
        """
        Retrieve existing object using object name or uid.

        Args:
            layer (str): Layer that the rule belongs to identified by the name or UID.
            rule_number (int): Rule number. Mandatory if "uid" or "name" are not set.
            uid (str): Object unique identifier. Mandatory if "rule_number" or "name" are not set.
            name (str): Object name. Mandatory if "rule_number" or "uid" are not set.
        Keyword Args:
            **details-level (str, optional):
                The level of detail for some of the fields in the response can vary from showing only the UID value\
                of the object to a fully detailed representation of the object.
                
        Returns:
            :obj:`Box`: The response from the server
            
        Examples:
            >>> firewallManagement.access_control_nat.nat_rule.show(
        uid="a5a88521-c996-a256-9625-b5a5d56c39ad",
        package="standard",)
        """
        # Main request parameters
        payload = {"package": package}

        if uid is not None:
            payload["uid"] = uid
        elif name is not None:
            payload["name"] = name
        elif rule_number is not None:
            payload["rule-number"] = rule_number
        else:
            raise MandatoryFieldMissing("uid or name or rule_number")

        # Secondary parameters
        secondary_parameters = {"details-level": str}

        payload.update(sanitize_secondary_parameters(secondary_parameters, **kw))

        return self._post("show-nat-rule", json=payload)

    def set(
        self,
        package: str,
        uid: str = None,
        name: str = None,
        rule_number: int = None,
        new_name: str = None,
        new_position: Union[int, str, dict] = None,
        enabled: bool = False,
        install_on: Union[str, List[str]] = None,
        method: str = None,
        original_destination: str = None,
        original_service: str = None,
        original_source: str = None,
        translated_destination: str = None,
        translated_service: str = None,
        translated_source: str = None,
        **kw,
    ) -> Box:
        """
        Edit existing object using object name or uid.

        Args:
            uid (str): Object unique identifier.
            new_name (str): New name of the object.
            rule_number (int): 	Rule number.
            name (str): Rule name.
            package (str): Name of the package.
            new_position (Union[int, str, dict]): New position in the rulebase. If an integer is provided, it will add the rule
            at the specific position. If a string is provided, it will add the rule at the position mentioned in the
            valid values ("top" or "bottom"). Otherwise, you can provide a dictionnary to explain more complex position
            (see the API documentation).
            enabled (bool): Enable/Disable the rule.
            install_on (Union[str, List[str]]): Which Gateways identified by the name or UID to install the policy on.
            method (str): Nat method. Valid values are "static", "hide", "nat64", "nat46" and "cgnat"
            original_destination (str): Original destination.
            original_service (str): Original service.
            original_source (str): 	Original source.
            translated_destination (str): Translated destination.
            translated_service (str): Translated service.
            translated_source (str): Translated service.
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
            >>> firewallManagement.access_control_nat.nat_rule.set(
        uid="a5a88521-c996-a256-9625-b5a5d56c39ad",
        new_name="New NAT Rule 1",
        new_position=3,
        package="standard",
        position="top",
        enabled=True,
        install_on="6c488338-8eec-4103-ad21-cd461ac2c476",
        method="static",
        original_destination="Any",
        original_service="New_TCP_Service_1",
        original_source="Any",
        translated_destination="Any",
        translated_service="New_TCP_Service_1",
        translated_source="Any",)
        """

        # Main request parameters
        payload = {"package": package}

        if uid is not None:
            payload["uid"] = uid
        elif name is not None:
            payload["name"] = name
        elif rule_number is not None:
            payload["rule-number"] = rule_number
        else:
            raise MandatoryFieldMissing("uid or name or rule_number")

        if enabled is not None:
            payload["enabled"] = enabled
        if install_on is not None:
            payload["install-on"] = install_on
        if method is not None:
            payload["method"] = method
        if original_destination is not None:
            payload["original-destination"] = original_destination
        if original_service is not None:
            payload["original-service"] = original_service
        if original_source is not None:
            payload["original-source"] = original_source
        if translated_destination is not None:
            payload["translated-destination"] = translated_destination
        if translated_service is not None:
            payload["translated-service"] = translated_service
        if translated_source is not None:
            payload["translated-source"] = translated_source
        if new_name is not None:
            payload["new-name"] = new_name
        if new_position is not None:
            payload["new-position"] = new_position

        # Secondary parameters
        secondary_parameters = {
            "comments": str,
            "details-level": str,
            "ignore-warnings": bool,
            "ignore-errors": bool,
        }
        payload.update(sanitize_secondary_parameters(secondary_parameters, **kw))

        return self._post("set-nat-rule", json=payload)

    def delete(
        self,
        package: str,
        uid: str = None,
        name: str = None,
        rule_number: int = None,
        **kw,
    ) -> Box:
        """
        Delete existing object using object name or uid.

        Args:
            uid (str): Object unique identifier.
            name (str): Object name.
            rule_number (int): 	Rule number.
            package (str): Name of the package
        Keyword Args:
            **details-level (str, optional):
                The level of detail for some of the fields in the response can vary from showing only the UID value\
                of the object to a fully detailed representation of the object.
                
        Returns:
            :obj:`Box`: The response from the server
            
        Examples:
            >>> firewallManagement.access_control_nat.nat_rule.delete(
        package="standard", uid="a5a88521-c996-a256-9625-b5a5d56c39ad")
        """
        # Main request parameters
        payload = {"package": package}

        if uid is not None:
            payload["uid"] = uid
        elif name is not None:
            payload["name"] = name
        elif rule_number is not None:
            payload["rule-number"] = rule_number
        else:
            raise MandatoryFieldMissing("uid or name or rule_number")

        # Secondary parameters
        secondary_parameters = {
            "details-level": str,
        }
        payload.update(sanitize_secondary_parameters(secondary_parameters, **kw))

        return self._post("delete-nat-rule", json=payload)

    def show_nat_rulebase(
        self,
        package: str,
        filter_results: str = None,
        filter_settings: dict = None,
        limit: int = 50,
        offset: int = 0,
        order: List[dict] = None,
        use_object_dictionnary: bool = None,
        **kw,
    ) -> Box:
        """
        Shows the entire NAT Rules layer. This layer is divided into sections. A NAT Rule may be within a section,
        or independent of a section (in which case it is said to be under the "global" section).
        There are two types of sections: auto generated
        read only sections and general sections which are created manually. The reply features a list of objects.
        Each object may be a section of the layer, within which its rules may be found, or a rule itself, for the case
        of rules which are under the global section. An optional "filter" field may be added in order to filter
        out only those rules that match a searchcriteria.

        Args:
            package (str): Name of the package
            name (str): Object name. Must be unique in the domain.
            uid (str): 	Object unique identifier.
            filter_results (str): Search expression to filter objects by.\
            The provided text should be exactly the same as it would be given in SmartConsole Object Explorer.\
            The logical operators in the expression ('AND', 'OR') should be provided in capital letters.\
            he search involves both a IP search and a textual search in name, comment, tags etc.
            filter_settings (str): Sets filter preferences.
            limit (int): The maximal number of returned results. Defaults to 50 (between 1 and 500)
            offset (int): Number of the results to initially skip. Defaults to 0
            order (List[dict]): Sorts results by the given field. By default the results are sorted in the \
            descending order by the session publish time.
            package (str): Name of the package.
            use_object_dictionnary (bool): N/A
        Keyword Args:
            **details-level (str, optional):
                The level of detail for some of the fields in the response can vary from showing only the UID value\
                of the object to a fully detailed representation of the object.
            **domains-to-process (List[str], optional):
                Indicates which domains to process the commands on. It cannot be used with the details-level full,
                must be run from the System Domain only and with ignore-warnings true.
                Valid values are: CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER.
            **dereference-group-members (bool, optional):
                Indicates whether to dereference "members" field by details level for every object in reply.
        Returns:
            :obj:`Box`: The response from the server
            
        Examples:
            >>> firewallManagement.access_control_nat.nat_rule.show_nat_rulebase(
        package="standard",
        offset=0,
        limit=20,
        order={"ASC": "name"},
        details_level="standard",
        use_object_dictionnary=True,
        filter_results="",
        filter_settings={},)
        """
        # Main request parameters
        payload = {"package": package}

        if filter_results is not None:
            payload["filter"] = filter_results
        if filter_settings is not None:
            payload["filter-settings"] = filter_settings
        if limit is not None:
            payload["limit"] = limit
        if offset is not None:
            payload["offset"] = offset
        if order is not None:
            payload["order"] = order
        if use_object_dictionnary is not None:
            payload["use-object-dictionnary"] = use_object_dictionnary

        # Secondary parameters
        secondary_parameters = {
            "dereference-group-members": bool,
            "details-level": str,
            "domains-to-process": List[str],
        }

        payload.update(sanitize_secondary_parameters(secondary_parameters, **kw))

        return self._post("show-nat-rulebase", json=payload)
