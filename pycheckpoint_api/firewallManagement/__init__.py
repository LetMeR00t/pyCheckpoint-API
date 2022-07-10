from box import Box
from restfly.session import APISession

from pycheckpoint_api import __version__

from .session import SessionAPI
from .network_objects import NetworkObjects
from .service_applications import ServiceApplications

from pycheckpoint_api.utils import sanitize_value


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
            field="username", t=str, is_mandatory=False, **kw
        )
        self._password = sanitize_value(
            field="password", t=str, is_mandatory=False, **kw
        )
        self._api_key = sanitize_value(field="api-key", t=str, is_mandatory=False, **kw)
        self._hostname = sanitize_value(
            field="hostname", t=str, is_mandatory=True, **kw
        )
        self._port = sanitize_value(field="port", t=int, is_mandatory=True, **kw)
        self._version = sanitize_value(field="version", t=str, is_mandatory=True, **kw)
        self._url = f"https://{self._hostname}:{self._port}/web_api"
        if self._version not in ["1.6", "1.6.1", "1.7", "1.7.1", "1.8", "1.9"]:
            self._url += f"/v{self._version}"
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
        del self._session.headers["X-chkp-sid"]
        return self.session.logout()

    @property
    def session(self):
        """The interface object for the Session Management."""
        return SessionAPI(self)

    @property
    def network_objects(self):
        """The interface object for the Network Objects Management."""
        return NetworkObjects(self)

    @property
    def service_applications(self):
        """The interface object for the Service & Applications Management."""
        return ServiceApplications(self)
