from typing import List, Union

from box import Box
from restfly.endpoint import APIEndpoint

from .policy_package import PolicyPackage


class Policy(APIEndpoint):
    @property
    def package(self) -> PolicyPackage:
        """The interface object for the Policy Package Management.

        Returns:
            Policy: a Policy Package instance

        Examples:
            >>> firewall.policy.package

        """
        return PolicyPackage(self)

    def install_policy(
        self,
        policy_package: str,
        targets: Union[str, List[str]],
        access: bool = None,
        desktop_security: bool = None,
        qos: bool = None,
        threat_prevention: bool = None,
        install_on_all_cluster_members_or_fail: bool = True,
        prepare_only: bool = False,
        revision: str = None,
    ) -> Box:
        """Executes the install-policy on a given list of targets.

        Args:
            policy_package (str): The name of the Policy Package to be installed.
            targets (Union[str, List[str]]): 	On what targets to execute this command. Targets may be identified by their \
            name, or object unique identifier.
            access (bool, optional): Set to be true in order to install the Access Control policy. By default, the value is \
            true if Access Control policy is enabled on the input policy package, otherwise false.. Defaults to None
            desktop_security (bool, optional): Set to be true in order to install the Desktop Security policy. By default, \
            the value is true if desktop security policy is enabled on the input policy package, otherwise false. \
            Defaults to None
            qos (bool, optional): Set to be true in order to install the QoS policy. By default, the value is true if \
            Quality-of-Service policy is enabled on the input policy package, otherwise false. Defaults to None
            threat_prevention (bool, optional): Set to be true in order to install the Threat Prevention policy. \
            By default, the value is true if Threat Prevention policy is enabled on the input policy package, \
            otherwise false.Defaults to None
            install_on_all_cluster_members_or_fail (bool, optional): Relevant for the gateway clusters. If true, the policy \
            is installed on all the cluster members. If the installation on a cluster member fails, don't install on \
            that cluster. Defaults to True
            prepare_only (bool, optional): If true, prepares the policy for the installation, but doesn't install it on an \
            installation target. Defaults to False
            revision (str, optional): The UID of the revision of the policy to install. Defaults to None

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> firewallManagement.policy.install_policy(
            ... policy_package="standard",
            ... access=True,
            ... threat_prevention=True,
            ... targets=["corporate-gateway"])

        """
        # Main request parameters
        payload = {"policy-package": policy_package, "targets": targets}

        if access is not None:
            payload["access"] = access
        if desktop_security is not None:
            payload["desktop-security"] = desktop_security
        if qos is not None:
            payload["qos"] = qos
        if threat_prevention is not None:
            payload["threat-prevention"] = threat_prevention
        if install_on_all_cluster_members_or_fail is not None:
            payload[
                "install-on-all-cluster-members-or-fail"
            ] = install_on_all_cluster_members_or_fail
        if prepare_only is not None:
            payload["prepare-only"] = prepare_only
        if revision is not None:
            payload["revision"] = revision

        return self._post("install-policy", json=payload)

    def verify_policy(self, policy_package: str) -> Box:
        """Verifies the policy of the selected package.
        Note: Verify Policy command can verify only access policy.

        Args:
            policy_package (str): Policy package identified by the name or UID.

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> firewallManagement.policy.verify_policy(
            ... policy_package="standard")

        """
        # Main request parameters
        payload = {"policy-package": policy_package}

        return self._post("verify-policy", json=payload)
