from typing import Union, List

from box import Box

from ..abstract.network_object import NetworkObjectAPI
from ..exception import MandatoryFieldMissing
from pycheckpoint_api.utils import sanitize_secondary_parameters
from pycheckpoint_api.models import Color


class LSMGatewayAPI(NetworkObjectAPI):
    def add(
        self,
        name: str,
        security_profile: str,
        provisioning_settings: dict = None,
        provisioning_state: str = None,
        sic: dict = None,
        tags: Union[str, List[str]] = None,
        **kw
    ) -> Box:
        """
        Add LSM Gateway.

        Args:
            name (str): Object name. Must be unique in the domain.
            security_profile (str):	LSM profile.
            provisioning_settings (dict): Provisioning settings.
            provisioning_state (str): Provisioning state. By default the state is 'manual'- enable provisioning
            but not attach to profile. If 'using-profile' state is provided a provisioning profile must be
            provided in provisioning-settings.
            sic (dict): Secure Internal Communication.
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
            >>> firewallManagementApi.network_objects.lsm_gateway.add(name="My object")
        """

        # Main request parameters
        payload = {"name": name, "security-profile": security_profile}
        if provisioning_settings is not None:
            payload["provisioning-settings"] = provisioning_settings
        if provisioning_state is not None:
            payload["provisioning-state"] = provisioning_state
        if sic is not None:
            payload["sic"] = sic
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

        return self._post("add-lsm-gateway", json=payload)

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
            >>> firewallManagementApi.network_objects.lsm_gateway.show(uid="ed997ff8-6709-4d71-a713-99bf01711cd5")
        """
        return self.show_object(endpoint="show-lsm-gateway", uid=uid, name=name, **kw)

    def set(
        self,
        uid: str = None,
        name: str = None,
        security_profile: str = None,
        provisioning_settings: dict = None,
        provisioning_state: str = None,
        sic: dict = None,
        new_name: str = None,
        tags: Union[str, List[str]] = None,
        **kw
    ) -> Box:
        """
        Edit existing object using object name or uid.

        Args:
            uid (str): Object unique identifier.
            name (str): Object name.
            security_profile (str):	LSM profile.
            provisioning_settings (dict): Provisioning settings.
            provisioning_state (str): Provisioning state. By default the state is 'manual'- enable provisioning
            but not attach to profile. If 'using-profile' state is provided a provisioning profile must be
            provided in provisioning-settings.
            sic (dict): Secure Internal Communication.
            new_name (str): New name of the object.
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
            >>> firewallManagement.network_objects.lsm_gateway.set(uid="ed997ff8-6709-4d71-a713-99bf01711cd5",
            new_name="New Tag")
        """

        # Main request parameters
        payload = {}
        if uid is not None:
            payload["uid"] = uid
        elif name is not None:
            payload["name"] = name
        else:
            raise MandatoryFieldMissing("uid or name")

        if security_profile is not None:
            payload["security-profile"] = security_profile
        if provisioning_settings is not None:
            payload["provisioning-settings"] = provisioning_settings
        if provisioning_state is not None:
            payload["provisioning-state"] = provisioning_state
        if sic is not None:
            payload["sic"] = sic
        if new_name is not None:
            payload["new-name"] = new_name
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

        return self._post("set-lsm-gateway", json=payload)

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
            >>> firewallManagementApi.network_objects.lsm_gateway.delete(uid="ed997ff8-6709-4d71-a713-99bf01711cd5")
        """
        return self.delete_object(
            endpoint="delete-lsm-gateway", uid=uid, name=name, **kw
        )

    def show_lsm_gateways(
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
            >>> firewallManagementApi.network_objects.lsm_gateway.shows_lsm_gateways()
        """
        return self.show_objects(
            endpoint="show-lsm-gateways",
            filter_results=filter_results,
            limit=limit,
            offset=offset,
            order=order,
            extra_secondary_parameters={"domains-to-process": List[str]},
            **kw
        )
