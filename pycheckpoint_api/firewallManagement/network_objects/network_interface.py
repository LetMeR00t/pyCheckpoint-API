from box import Box
from restfly.endpoint import APIEndpoint

from ..exception import MandatoryFieldMissing


class NetworkInterface(APIEndpoint):
    def abort_get_interfaces(self, task_id: str, force_cleanup: bool = False) -> Box:
        """
        Attempt to abort an on-going "get-interfaces" operation.
        This API might fail if the "get-interfaces" operation is in its final stage.

        Args:
            task_id (str): get-interfaces task UID.
            force_cleanup (bool, optional): Forcefully abort the "get-interfaces" task.
        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> firewall.network_objects.network_interface.abort_get_interfaces(
                task_id="01234567-89ab-cdef-a930-8c37a59972b3")
        """
        # Main request parameters
        payload = {"task-id": task_id}

        if force_cleanup is not None:
            payload["force-cleanup"] = force_cleanup

        return self._post("abort-get-interfaces", json=payload)

    def get_interfaces(
        self,
        target_uid: str = None,
        target_name: str = None,
        group_interfaces_by_subnet: bool = False,
        use_defined_by_routes: bool = True,
        with_topology: bool = False,
    ) -> Box:
        """
        Get physical interfaces with or without their topology from a Gaia Security Gateway or Cluster.
        Note: The fetched topology is based on static routes. Prerequisites: 1) SIC must be established in the
        Security Gateway or Cluster Member object. 2) Security Gateway or Cluster Members must be up and running.

        Args:
            target_uid (str, optional): Target unique identifier.
            target_name (str, optional): Target name.
            group_interfaces_by_subnet (bool, optional): Specify whether to group the cluster interfaces by a subnet.\
            Otherwise, group the cluster interfaces by their names.
            use_defined_by_routes (bool, optional): Specify whether to configure the topology "Defined by Routes" where applicable.\
            Otherwise, configure the topology to "This Network" as default for internal interfaces.
            with_topology (bool, optional): Specify whether to fetch the interfaces with their topology.\
            Otherwise, the Management Server fetches the interfaces without their topology.
        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> firewall.network_objects.network_interface.get_interfaces(
            ... target_name="gw123")
        """
        # Main request parameters
        payload = {}
        if target_uid is not None:
            payload["target-uid"] = target_uid
        elif target_name is not None:
            payload["target-name"] = target_name
        else:
            raise MandatoryFieldMissing("target_uid or target_name")

        if group_interfaces_by_subnet is not None:
            payload["group-interfaces-by-subnet"] = group_interfaces_by_subnet
        if use_defined_by_routes is not None:
            payload["use-defined-by-routes"] = use_defined_by_routes
        if with_topology is not None:
            payload["with-topology"] = with_topology

        return self._post("get-interfaces", json=payload)
