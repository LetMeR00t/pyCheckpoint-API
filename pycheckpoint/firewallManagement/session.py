from box import Box
from restfly.endpoint import APIEndpoint


class SessionAPI(APIEndpoint):
    def create(self, username: str, password: str, **kw) -> Box:
        """
        Creates a Firewall Management authentication session.
        Args:
            username (str): Username of admin user for the authentication session.
            password (str): Password of the admin user for the authentication session.
        Keyword Args:
            **continue-last-session (bool, optional):
                When 'continue-last-session' is set to 'True', the new session would continue where the last session
                 was stopped. This option is available when the administrator has only one session that can be continued.
                If there is more than one session, see 'switch-session' API. Default is 'False'
            **domain (str, optional):
                Use domain to login to specific domain. Domain can be identified by name or UID.
            **enter-last-published-session (bool, optional):
                Login to the last published session. Such login is done with the Read Only permissions.
            **read-only (bool, optional):
                Login with Read Only permissions. This parameter is not considered in case continue-last-session is true.
            **session-comments (str, optional):
                Session comments. Can be viewed only using the show-session API.
            **session-description (str, optional):
                A description of the session's purpose.
            **session-name (str, optional):
                Session unique name.
            **session-timeout (int, optional):
                Session expiration timeout in seconds. Default 600 seconds.
        Returns:
            :obj:`Box`: The authenticated session information.
        Examples:
            >>> firewallManagementApi.session.create(username='admin@example.com',
            ...    password='MyInsecurePassword')
        """

        payload = {"username": username, "password": password}
        for k in [
            "continue-last-session",
            "domain",
            "enter-last-published-session",
            "read-only",
            "session-comments",
            "session-description",
            "session-name",
            "session-timeout",
        ]:
            v = kw.get(k, None)
            if v is not None:
                payload[k] = v

        return self._post("login", json=payload)

    def delete(self) -> int:
        """
        Ends an authentication session.
        Returns:
            :obj:`int`: The status code of the operation.
        Examples:
            >>> firewallManagementApi.session.delete()
        """
        return self._post("logout", box=False).status_code
