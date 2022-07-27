from typing import List, Union

from box import Box
from restfly.endpoint import APIEndpoint

from pycheckpoint_api.models import Color
from pycheckpoint_api.utils import sanitize_secondary_parameters, sanitize_value

from .exception import MandatoryFieldMissing


class Session(APIEndpoint):
    def login(
        self, user: str = None, password: str = None, api_key: str = None, **kw
    ) -> Box:
        """Creates a Firewall Management authentication session. You should authenticate using either a \
        username/password or by using an API key.

        Args:
            user (str, optional): Username of admin user for the authentication session. If set, you must specify\
            ``password`` too. Defaults to None
            password (str, optional): Password of the admin user for the authentication session. If set, you must\
            specify ``user`` too. Defaults to None
            api_key (str, optional): An API key used to authenticate instead of a user/password.\ You must enter\
            either a ``user``/``password`` or an ``api_key``. Defaults to None
            **kw (dict, optional): Arbitrary keyword arguments for secondary parameters.

        Keyword Args:
            **continue-last-session (bool, optional):
                When 'continue-last-session' is set to 'True', the new session would continue where the last session\
                 was stopped. This option is available when the administrator has only one session that can be continued.\
                If there is more than one session, see 'switch-session' API. Defaults to 'False'
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
        Raises:
            MandatoryFieldMissing: The value is not given as a keyword parameter and it's mandatory

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> Management.session.login(
            ... hostname="127.0.0.1",
            ... port=443,
            ... user="test@example.com",
            ... password="hunter2",
            ... domain="MyDomain",
            ... version="1.5",
            ... ssl_verify=False)
        """

        # Main request parameters
        payload = {}
        if user is not None:
            if password is not None:
                payload = {"user": user, "password": password}
            else:
                raise MandatoryFieldMissing("password")
        elif api_key is not None:
            payload = {"api-key": api_key}
        else:
            raise MandatoryFieldMissing("user/password or api_key")

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
        payload.update(sanitize_secondary_parameters(secondary_parameters, **kw))

        return self._post("login", json=payload)

    def logout(self) -> Box:
        """Ends an authentication session.

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> Management.session.logout()

        """
        return self._post("logout", json={})

    def publish(self, uid: str = None) -> Box:
        """All the changes done by this user will be seen by all users only after publish is called.

        Args:
            uid (str, optional): Session unique identifier. Specify it to publish a different session\
                than the one you currently use.. Defaults to None

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> Management.session.publish(uid="7a13a360-9b24-40d7-acd3-5b50247be33e")

        """

        payload = {}
        if uid is not None:
            payload["uid"] = uid

        return self._post("publish", json=payload)

    def discard(self, uid: str = None) -> Box:
        """All changes done by user are discarded and removed from database.

        Args:
            uid (str, optional): Session unique identifier. Specify it to publish a different session than\
                the one you currently use. Defaults to None.

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> Management.session.discard(uid="7a13a360-9b24-40d7-acd3-5b50247be33e")

        """

        payload = {}
        if uid is not None:
            payload["uid"] = uid

        return self._post("discard", json=payload)

    def disconnect(self, uid: str, discard: bool = False) -> Box:
        """Disconnect a private session.

        Args:
            uid (str): Session unique identifier.
            discard (bool, optional): Discard all changes committed during the session.\
                Defaults to False.

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> Management.session.disconnect()
        """
        payload = {"uid": uid}

        if discard is not None:
            payload["discard"] = discard

        return self._post("disconnect", json=payload)

    def keepalive(self) -> Box:
        """Keep the session valid/alive.

        Returns:
            :obj:`Response`: The response from the server

        Examples:
            >>> Management.session.keepalive()
        """
        return self._post("keepalive")

    def revert_to_revision(self, to_session: str = None) -> Box:
        """Revert the Management Database to the selected revision.

        Args:
            to_session (str, optional): Session unique identifier. Specify the session id you would like to revert\
            your database to.. Defaults to None

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> Management.session.revert_to_revision(to_session="7a13a360-9b24-40d7-acd3-5b50247be33e")

        """

        payload = {}
        if to_session is not None:
            payload["to-session"] = to_session

        return self._post("revert-to-revision", json=payload)

    def verify_revert(self, to_session: str) -> Box:
        """Verify the Management Database can revert to the selected revision.

        Args:
            to_session (str): Session unique identifier. Specify the session id you would like to revert your database to.

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> Management.session.verify_revert(to_session="7a13a360-9b24-40d7-acd3-5b50247be33e")
        """

        payload = {}
        if to_session is not None:
            payload["to-session"] = to_session

        return self._post("verify-revert", json=payload)

    def login_to_domain(self, domain: str) -> Box:
        """Login from MDS to other domain.\
        This command is available only after logging in to the System Data domain.

        Args:
            domain (str): Domain identified by the name or UID.

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> Management.session.login_to_domain(domain="OneDomain")
        """

        payload = {}
        if domain is not None:
            payload["domain"] = domain

        return self._post("login-to-domain", json=payload)

    def show_session(self, uid: str = None) -> Box:
        """Show session.

        Args:
            uid (str, optional): Session unique identifier. Defaults to None.

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> Management.session.show_session(uid="7a13a360-9b24-40d7-acd3-5b50247be33e")
        """

        payload = {}
        if uid is not None:
            payload["uid"] = uid

        return self._post("show-session", json=payload)

    def set_session(
        self,
        description: str = None,
        new_name: str = None,
        tags: Union[dict, str, List[str]] = None,
        **kw
    ) -> Box:
        """Edit user's current session.

        Args:
            description (str, optional): Session description. Defaults to None.
            new_name (str, optional): New name of the object. Defaults to None.
            tags (List[str], optional): Collection of tag identifiers. Defaults to None.

        Keyword Args:
            **color (string, optional):
                Color of the object. Should be one of existing colors.
            **comments (string, optional):
                Comments string.
            **details-level (string, optional):
                The level of detail for some of the fields in the response can vary from showing only
                the UID value of the object to a fully detailed representation of the object.
            **ignore-warnings (bool, optional):
                Apply changes ignoring warnings. Defaults to "False"
            **ignore-errors (bool, optional):
                Apply changes ignoring errors. You won't be able to publish such a changes.
                If ignore-warnings flag was omitted - warnings will also be ignored. Defaults to "False"

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> Management.session.set_session(description="My custom description")
        """

        payload = {}
        # Main request parameters
        if description is not None:
            payload["description"] = sanitize_value(kw.get("description", None), t=str)
        if new_name is not None:
            payload["new-name"] = sanitize_value(kw.get("new_name", None), t=str)
        if tags is not None:
            payload["tags"] = sanitize_value(kw.get("tags", None), t=List[str])

        # Secondary parameters
        secondary_parameters = {
            "color": Color,
            "comments": str,
            "details-level": str,
            "ignore-warnings": bool,
            "ignore-errors": bool,
        }
        payload.update(sanitize_secondary_parameters(secondary_parameters, **kw))

        return self._post("set-session", json=payload)

    def purge_published_sessions(
        self, number_of_sessions_to_preserve: int = None, preserve_to_date: str = None
    ) -> Box:
        """Permanently deletes all data which belongs to the published sessions not selected for preservation.\
        This operation is irreversible.

        Args:
            number_of_sessions_to_preserve (int, optional): The number of newest sessions to preserve, by the \
                sessions's publish date. Required if ``preserve_to_date`` is not set. Defaults to None
            preserve_to_date (str, optional): The date until which sessions are preserved, by the sessions's\
                publish date. ISO 8601. If timezone isn't specified in the input, the Management server's\
                timezone is used. Required if ``number_of_sessions_to_preserve`` is not set. Defaults to None

        Raises:
            MandatoryFieldMissing: The value is not given as a keyword parameter and it's mandatory

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> Management.session.purge_published_sessions(number_of_sessions_to_preserve=1)

        """

        payload = {}
        if number_of_sessions_to_preserve is not None:
            payload["number-of-sessions-to-preserve"] = number_of_sessions_to_preserve
        elif preserve_to_date is not None:
            payload["preserve-to-date"] = preserve_to_date
        else:
            raise MandatoryFieldMissing(
                "number_of_sessions_to_preserve or preserve_to_date"
            )

        return self._post("purge-published-sessions", json=payload)

    def switch_session(self, uid: str) -> Box:
        """Switch to a disconnected Management API session of the same administrator.\
        To switch to an open session or to a session of a different administrator\
        use the take-over session API.

        Args:
            uid (str): Session unique identifier. It should belong to the current administrator.\
 Switching to the sessions opened in SmartConsole is not supported.

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> Management.session.switch_session(uid="7a13a360-9b24-40d7-acd3-5b50247be33e")

        """

        payload = {"uid": uid}

        return self._post("switch-session", json=payload)

    def take_over_session(
        self, uid: str, disconnect_active_session: bool = False
    ) -> Box:
        """Take ownership of another session and start working on it.

        Args:
            uid (str): Session unique identifier.
            disconnect-active-session (bool): Allows taking over of an active session,\
                currently executed by another administrator. Defaults to False

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> Management.session.take_over_session(uid="7a13a360-9b24-40d7-acd3-5b50247be33e")

        """

        payload = {"uid": uid}

        if disconnect_active_session is not False:
            payload["disconnect-active-session"] = True

        return self._post("take-over-session", json=payload)

    def show_sessions(
        self,
        filter_results: str = None,
        limit: int = 50,
        offset: int = 0,
        order: List[dict] = None,
        view_published_sessions: bool = False,
        **kw
    ) -> Box:
        """Retrieve all objects.

        Args:
            filter_results (str, optional): Search expression to filter objects by.\
                The provided text should be exactly the same as it would be given in\
                SmartConsole Object Explorer. The logical operators in the expression\
                ('AND', 'OR') should be provided in capital letters.\ The search involves\
                both a IP search and a textual search in name, comment, tags etc. Defaults to None
            limit (int, optional): The maximal number of returned results. Defaults to 50 (between 1 and 500).
            offset (int, optional): Number of the results to initially skip. Defaults to 0
            order (List[dict], optional): Sorts results by the given field.\
                By default the results are sorted in the descending order by the session publish time.\
                Defaults to None
            view_published_sessions (bool, optional): Show a list of published sessions. Defaults to False
            **kw (dict, optional): Arbitrary keyword arguments for secondary parameters.

        Keyword Args:
            **details-level (str, optional):
                The level of detail for some of the fields in the response can vary from showing only the UID value\
                of the object to a fully detailed representation of the object.

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> Management.session.switch_session(uid="7a13a360-9b24-40d7-acd3-5b50247be33e")

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
        if view_published_sessions is not False:
            payload["view-published-sessions"] = True

        # Secondary parameters
        secondary_parameters = {"details-level": str}
        payload.update(sanitize_secondary_parameters(secondary_parameters, **kw))

        return self._post("show-sessions", json=payload)

    def continue_session_in_smartconsole(self, uid: str = None) -> Box:
        """ Logout from existing session. The session will be continued next time your open SmartConsole.\
        In case 'uid' is not provided, use current session. In order for the session to pass\
        successfully to SmartConsole, make sure you don't have any other active GUI sessions.

        Args:
            uid (str, optional): Session unique identifier. Defaults to None

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> Management.session.continue_session_in_smartconsole(uid="7a13a360-9b24-40d7-acd3-5b50247be33e")

        """

        payload = {"uid": uid}

        return self._post("continue-session-in-smartconsole", json=payload)

    def show_last_published_session(self) -> Box:
        """Shows the last published session.

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> Management.session.show_last_published_session()

        """

        return self._post("show-last-published-session", json={})

    def show_login_message(self, **kw) -> Box:
        """Retrieve existing object using object name or uid.

        Args:
            **kw (dict, optional): Arbitrary keyword arguments for secondary parameters.

        Keyword Args:
            **details-level (string, optional):
                The level of detail for some of the fields in the response can vary from showing only
                the UID value of the object to a fully detailed representation of the object.

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> Management.session.show_login_message()

        """

        payload = {}

        # Secondary parameters
        secondary_parameters = {"details-level": str}
        payload.update(sanitize_secondary_parameters(secondary_parameters, **kw))

        return self._post("show-login-message", json=payload)

    def set_login_message(
        self,
        header: str = None,
        message: str = None,
        show_message: bool = None,
        warning: bool = None,
        **kw
    ) -> Box:
        """Edit existing object using object name or uid.

        Args:
            header (str, optional): Login message header. Defaults to None
            message (str, optional): Login message body. Defaults to None
            show_message (bool, optional): Whether to show login message. Defaults to None
            warning (bool, optional): Add warning sign. Defaults to None
            **kw (dict, optional): Arbitrary keyword arguments for secondary parameters.

        Keyword Args:
            **details-level (str, optional):
                The level of detail for some of the fields in the response can vary from showing only the UID value\
                of the object to a fully detailed representation of the object.

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> Management.session.set_login_message(message="Hello World!")

        """

        payload = {}
        if header is not None:
            payload["header"] = header
        if message is not None:
            payload["message"] = message
        if show_message is not None:
            payload["offset"] = show_message
        if warning is not None:
            payload["order"] = warning

        # Secondary parameters
        secondary_parameters = {"details-level": str}
        payload.update(sanitize_secondary_parameters(secondary_parameters, **kw))

        return self._post("set-login-message", json=payload)

    def set_automatic_purge(
        self,
        enabled: bool,
        keep_sessions_by_count: bool = True,
        number_of_sessions_to_keep: int = 999,
        keep_sessions_by_days: bool = True,
        number_of_days_to_keep: int = 365,
        scheduling: dict = None,
    ) -> Box:
        """Set Automatic Purge. ⚠️ Note:
        This command will permanently delete all of the data which\
        belongs to the published sessions not selected for preservation.⚠️

        Args:
            enabled (bool): Turn on/off the automatic-purge feature
            keep_sessions_by_count (bool, optional): Whether or not to keep the latest N sessions.\
            Note: when the automatic purge feature is enabled, this field and/or the \
            "keep-sessions-by-date" field must be set to 'true'. Defaults to True
            number_of_sessions_to_keep (int, optional): When "keep-sessions-by-count = true"\
            this sets the number of newest sessions to preserve, by the sessions's publish date. \
            Defaults to 999
            keep_sessions_by_days (bool, optional): Whether or not to keep the sessions for D days.\
            Note: when the automatic purge feature is enabled, this field and/or the \
            "keep-sessions-by-count" field must be set to 'true'. Defaults to True
            number_of_days_to_keep (int, optional): When "keep-sessions-by-days = true" this sets\
            the number of days to keep the sessions. Defaults to 365
            scheduling (dict, optional): When to purge sessions that do not meet the "keep" criteria.\
            Note: when the automatic purge feature is enabled, this field must be set. Defaults to None

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> Management.session.set_automatic_purge(enabled=True)

        """

        payload = {"enabled": enabled}
        if keep_sessions_by_count is not None:
            payload["keep-sessions-by-count"] = keep_sessions_by_count
        if number_of_sessions_to_keep is not None:
            payload["number-of-sessions-to-keep"] = number_of_sessions_to_keep
        if keep_sessions_by_days is not None:
            payload["keep-sessions-by-days"] = keep_sessions_by_days
        if number_of_days_to_keep is not None:
            payload["number-of-days-to-keep"] = number_of_days_to_keep
        if scheduling is not None:
            payload["scheduling"] = scheduling

        return self._post("set-automatic-purge", json=payload)

    def show_automatic_purge(self) -> Box:
        """Show Automatic Purge.

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> Management.session.show_automatic_purge()

        """

        return self._post("show-automatic-purge", json={})
