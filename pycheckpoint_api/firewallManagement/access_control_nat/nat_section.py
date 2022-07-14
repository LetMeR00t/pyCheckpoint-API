from typing import Union

from box import Box
from restfly.endpoint import APIEndpoint

from pycheckpoint_api.utils import sanitize_secondary_parameters

from ..exception import MandatoryFieldMissing


class NASSection(APIEndpoint):
    def add(
        self,
        package: str,
        position: Union[int, str, dict],
        name: str = None,
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
            name (str): Section name.
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
            >>> firewallManagement.access_control_nat.nat_section.add(
        package="standard",
        position=1,
        name="New NAT Section 1",)
        """

        # Main request parameters
        payload = {"package": package, "position": position}

        if name is not None:
            payload["name"] = name

        # Secondary parameters
        secondary_parameters = {
            "details-level": str,
            "ignore-warnings": bool,
            "ignore-errors": bool,
        }
        payload.update(sanitize_secondary_parameters(secondary_parameters, **kw))

        return self._post("add-nat-section", json=payload)

    def show(
        self,
        package: str,
        uid: str = None,
        name: str = None,
        **kw,
    ) -> Box:
        """
        Retrieve existing object using object name or uid.

        Args:
            package (str): Name of the package.
            rule_number (int): Rule number. Mandatory if "uid" or "name" are not set.
            uid (str): Object unique identifier. Mandatory if "rule_number" or "name" are not set.
            name (str): Object name. Mandatory if "rule_number" or "uid" are not set.
        Keyword Args:
            **details-level (str, optional):
                The level of detail for some of the fields in the response can vary from showing only the UID value
                of the object to a fully detailed representation of the object.
        Returns:
            :obj:`Box`: The response from the server
        Examples:
            >>> firewallManagement.access_control_nat.nat_section.show(
        uid="bb89a652-369a-2884-dd59-f69ea241567cd", package="standard")
        """
        # Main request parameters
        payload = {"package": package}

        if uid is not None:
            payload["uid"] = uid
        elif name is not None:
            payload["name"] = name
        else:
            raise MandatoryFieldMissing("uid or name")

        # Secondary parameters
        secondary_parameters = {"details-level": str}

        payload.update(sanitize_secondary_parameters(secondary_parameters, **kw))

        return self._post("show-nat-section", json=payload)

    def set(
        self,
        package: str,
        uid: str = None,
        name: str = None,
        new_name: str = None,
        **kw,
    ) -> Box:
        """
        Edit existing object using object name or uid.

        Args:
            uid (str): Object unique identifier.
            new_name (str): New name of the object.
            package (str): Name of the package.
            name (str): Rule name.
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
            >>> firewallManagement.access_control_nat.nat_section.set(
        package="standard",
        uid="bb89a652-369a-2884-dd59-f69ea241567cd",
        new_name="New NAT Section 1",)
        """

        # Main request parameters
        payload = {"package": package}

        if uid is not None:
            payload["uid"] = uid
        elif name is not None:
            payload["name"] = name
        else:
            raise MandatoryFieldMissing("uid or name")

        if new_name is not None:
            payload["new-name"] = new_name

        # Secondary parameters
        secondary_parameters = {
            "details-level": str,
            "ignore-warnings": bool,
            "ignore-errors": bool,
        }
        payload.update(sanitize_secondary_parameters(secondary_parameters, **kw))

        return self._post("set-nat-section", json=payload)

    def delete(
        self,
        package: str,
        uid: str = None,
        name: str = None,
        **kw,
    ) -> Box:
        """
        Delete existing object using object name or uid.

        Args:
            uid (str): Object unique identifier.
            name (str): Object name.
            package (str): Name of the package.
        Keyword Args:
            **details-level (str, optional):
                The level of detail for some of the fields in the response can vary from showing only the UID value
                of the object to a fully detailed representation of the object.
        Returns:
            :obj:`Box`: The response from the server
        Examples:
            >>> firewallManagement.access_control_nat.nat_section.delete(
        package="standard", uid="bb89a652-369a-2884-dd59-f69ea241567cd")
        """
        # Main request parameters
        payload = {"package": package}

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

        return self._post("delete-nat-section", json=payload)
