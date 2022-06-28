from box import Box
from restfly.session import APISession

from pycheckpoint import __version__

from .session import SessionAPI

from pycheckpoint.utils import sanitize_value


class FirewallManagementAPI(APISession):
    """
    A Controller to access Endpoints in the Checkpoint Firewall Management API.
    The ManagementAPI object stores the session token and simplifies access to CRUD options within the Checkpoint firewalls.
    Attributes:
        username (str): (Mandatory) The Firewall Management administrator username.
        password (str): (Mandatory) The Firewall Management administrator password.
        hostname (str): (Mandatory) The Firewall Management hostname to use
        port (int): (Mandatory) The Firewall Management port to use.
        version (int): (Mandatory) The Firewall Management version to use.
    """

    _vendor = "Checkpoint"
    _product = "Checkpoint Firewall Management"
    _backoff = 3
    _build = __version__
    _box = True
    _box_attrs = {"camel_killer_box": True}
    _env_base = "CHECKPOINT_FIREWALL"

    def __init__(self, **kw):
        self._username = sanitize_value(
            field="username", type=str, is_mandatory=False, **kw
        )
        self._password = sanitize_value(
            field="password", type=str, is_mandatory=False, **kw
        )
        self._api_key = sanitize_value(
            field="api-key", type=str, is_mandatory=False, **kw
        )
        self._hostname = sanitize_value(
            field="hostname", type=str, is_mandatory=True, **kw
        )
        self._port = sanitize_value(field="port", type=int, is_mandatory=True, **kw)
        self._version = sanitize_value(
            field="version", type=str, is_mandatory=True, **kw
        )
        self._url = f"https://{self._hostname}:{self._port}/web_api/v{self._version}"
        self.conv_box = True
        super(FirewallManagementAPI, self).__init__(**kw)

    def _build_session(self, **kwargs) -> Box:
        """Creates a Firewall Management API session."""
        super(FirewallManagementAPI, self)._build_session(**kwargs)
        resp = self.session.login(**kwargs)
        self._session.headers.update({"X-chkp-sid": resp["sid"]})
        return resp

    def _deauthenticate(self):
        """Ends the authentication session."""
        self._session.headers.update({"X-chkp-sid": None})
        return self.session.logout()

    @property
    def session(self):
        """The interface object for the :ref:`ZIA Authenticated Session interface <zia-session>`."""
        return SessionAPI(self)
