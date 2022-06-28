from box import Box
from requests import Response
from restfly.endpoint import APIEndpoint

from .exception import MandatoryFieldMissing
from pycheckpoint.utils import sanitize_value
from pycheckpoint.models import Color


class SessionAPI(APIEndpoint):
    def login(
        self, username: str = None, password: str = None, api_key: str = None, **kw
    ) -> Box:
        """
        Creates a Firewall Management authentication session. You should authenticate using either a
        username/password or by using an API key.
        Args:
            username (str): Username of admin user for the authentication session. You must specify "password" too.
            password (str): Password of the admin user for the authentication session. You must specify "username" too.
            api_key (str): API key of the admin user for the authentication session (use this only or user/password)
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

        # Main request parameters
        payload = {}
        if username is not None:
            if password is not None:
                payload = {"username": username, "password": password}
            else:
                raise MandatoryFieldMissing("password")
        elif username is None and api_key is not None:
            payload = {"api-key": api_key}
        elif username is None:
            raise MandatoryFieldMissing("username")
        else:
            raise MandatoryFieldMissing("api_key")

        # Secondary parameters
        secondary_parameters = {
            "continue-last-session": bool,
            "domain": str,
            "enter-last-published-session": bool,
            "read-only": bool,
            "session-comments": str,
            "session-description": str,
            "session-name": str,
            "session-timeout": int,
        }
        for field, type in secondary_parameters.items():
            payload[field] = sanitize_value(
                field=field, type=type, is_mandatory=False, **kw
            )

        return self._post("login", json=payload)

    def logout(self) -> Response:
        """
        Ends an authentication session.
        Returns:
            :obj:`Response`: The response from the server
        Examples:
            >>> firewallManagementApi.session.delete()
        """
        return self._post("logout", box=False)

    def publish(self, uid: str = None) -> Box:
        """
        All the changes done by this user will be seen by all users only after publish is called.
        Args:
            uid (str): Session unique identifier. Specify it to publish a different session than the one you currently use.
        Returns:
            :obj:`Box`: The response from the server
        Examples:
            >>> firewallManagementApi.session.publish(uid="7a13a360-9b24-40d7-acd3-5b50247be33e")
        """

        payload = {}
        if uid is not None:
            payload["uid"] = uid

        return self._post("publish", json=payload)

    def discard(self, uid: str = None) -> Box:
        """
        All changes done by user are discarded and removed from database.
        Args:
            uid (str): Session unique identifier. Specify it to publish a different session than the one you currently use.
        Returns:
            :obj:`Box`: The response from the server
        Examples:
            >>> firewallManagementApi.session.discard(uid="7a13a360-9b24-40d7-acd3-5b50247be33e")
        """

        payload = {}
        if uid is not None:
            payload["uid"] = uid

        return self._post("discard", json=payload)

    def disconnect(self) -> Response:
        """
        Disconnect a private session.
        Returns:
            :obj:`Response`: The response from the server
        Examples:
            >>> firewallManagementApi.session.disconnect()
        """
        return self._post("disconnect", box=False)

    def keepalive(self) -> Box:
        """
        Keep the session valid/alive.
        Returns:
            :obj:`Response`: The response from the server
        Examples:
            >>> firewallManagementApi.session.keepalive()
        """
        return self._post("keepalive", box=False)

    def revert_to_revision(self, to_session: str = None) -> Box:
        """
        Revert the Management Database to the selected revision.
        Args:
            to_session (str): Session unique identifier. Specify the session id you would like to revert your database to.
        Returns:
            :obj:`Box`: The response from the server
        Examples:
            >>> firewallManagementApi.session.revert_to_revision(to_session="7a13a360-9b24-40d7-acd3-5b50247be33e")
        """

        payload = {}
        if to_session is not None:
            payload["to-session"] = to_session

        return self._post("revert-to-revision", json=payload)

    def verify_revert(self, to_session: str) -> Box:
        """
        Verify the Management Database can revert to the selected revision.
        Args:
            to_session (str): Session unique identifier. Specify the session id you would like to revert your database to.
        Returns:
            :obj:`Box`: The response from the server
        Examples:
            >>> firewallManagementApi.session.verify_revert(to_session="7a13a360-9b24-40d7-acd3-5b50247be33e")
        """

        payload = {}
        if to_session is not None:
            payload["to-session"] = to_session

        return self._post("verify-revert", json=payload)

    def login_to_domain(self, domain: str) -> Box:
        """
        Login from MDS to other domain.
        This command is available only after logging in to the System Data domain.
        Args:
            domain (str): Domain identified by the name or UID.
        Returns:
            :obj:`Box`: The response from the server
        Examples:
            >>> firewallManagementApi.session.login_to_domain(domain="OneDomain")
        """

        payload = {}
        if domain is not None:
            payload["domain"] = domain

        return self._post("login-to-domain", json=payload)

    def show_session(self, uid: str = None) -> Box:
        """
        Show session.
        Args:
            uid (str): Session unique identifier.
        Returns:
            :obj:`Box`: The response from the server
        Examples:
            >>> firewallManagementApi.session.show_session(uid="7a13a360-9b24-40d7-acd3-5b50247be33e")
        """

        payload = {}
        if uid is not None:
            payload["uid"] = uid

        return self._post("show-session", json=payload)

    def set_session(
        self,
        description: str = None,
        new_name: str = None,
        tags: list[str] = None,
        **kw
    ) -> Box:
        """
        Edit user's current session.
        Args:
            description (str): Session description.
            new_name (str): New name of the object.
            tags (list[str]): Collection of tag identifiers.
        Keyword Args:
            **color (string, optional):
                Color of the object. Should be one of existing colors.
            **comments (string, optional):
                Comments string.
            **details-level (string, optional):
                The level of detail for some of the fields in the response can vary from showing only
                the UID value of the object to a fully detailed representation of the object.
            **ignore-warnings (bool, optional):
                Apply changes ignoring warnings. Default is "False"
            **ignore-errors (bool, optional):
                Apply changes ignoring errors. You won't be able to publish such a changes.
                If ignore-warnings flag was omitted - warnings will also be ignored. Default is "False"
        Returns:
            :obj:`Box`: The response from the server
        Examples:
            >>> firewallManagementApi.session.set_session(description="My custom description")
        """

        payload = {}
        # Main request parameters
        if description is not None:
            payload["description"] = sanitize_value(
                kw.get("description", None), type=str
            )
        if new_name is not None:
            payload["new-name"] = sanitize_value(kw.get("new_name", None), type=str)
        if tags is not None:
            payload["tags"] = sanitize_value(kw.get("tags", None), type=list[str])

        # Secondary parameters
        secondary_parameters = {
            "color": Color,
            "comments": str,
            "details-level": str,
            "ignore-warnings": bool,
            "ignore-errors": bool,
        }
        for field, type in secondary_parameters.items():
            payload[field] = sanitize_value(
                field=field, type=type, is_mandatory=False, **kw
            )

        return self._post("set-session", json=payload)
