from box import Box
from restfly.session import APISession

from pycheckpoint_api import __version__
from pycheckpoint_api.utils import sanitize_value

from .access_control_nat import AccessControlNAT
from .network_objects import NetworkObjects
from .service_applications import ServiceApplications
from .session import Session


class FirewallManagement(APISession):
    """A Controller to access Endpoints in the Checkpoint Firewall Management API.
    The ManagementAPI object stores the session token and simplifies access to CRUD options within the Checkpoint firewalls.
    """

    _vendor = "Checkpoint"
    _product = "Checkpoint Firewall Management"
    _backoff = 3
    _build = __version__
    _box = True
    _box_attrs = {"camel_killer_box": True}
    _env_base = "CHECKPOINT_FIREWALL"

    def __init__(self, **kw):
        """Class constructor

        Args:
            **kw (dict): Arbitrary keyword arguments for parameters.

        Keyword Args:
            **user (str, optional)
                User name to use to authenticate (instead of ``api_key``)
            **password (str, optional)
                Password to use to authenticate (instead of ``api_key``)
            **api_key (str, optional)
                API key to use to authenticate (instead of ``user``/``password``)
            **hostname (str, optional)
                Hostname used to reach the Firewall Checkpoint
            **port (str, optional)
                Port used to reach the Firewall Checkpoint.
            **version (str, optional)
                Current API version used by the Firewall Checkpoint

        Examples:
            >>> firewall = FirewallManagement(hostname="localhost",port=443,
            ... api_key="<API_KEY>",version="1.8",domain="Local Domain"",ssl_verify=False,)

        """
        self._user = sanitize_value(field="user", t=str, is_mandatory=False, **kw)
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
        super(FirewallManagement, self).__init__(**kw)

    def _build_session(self, **kwargs) -> Box:
        """Creates a Firewall Management API session."""
        super(FirewallManagement, self)._build_session(**kwargs)
        resp = self.session.login(**kwargs)
        self._session.headers.update({"X-chkp-sid": resp["sid"]})
        return resp

    def _deauthenticate(self):
        """Ends the authentication session."""
        del self._session.headers["X-chkp-sid"]
        return self.session.logout()

    @property
    def session(self) -> Session:
        """The interface object for the Session Management.

        Returns:
            Session: a Session object

        Examples:
            >>> firewall.session

        """
        return Session(self)

    @property
    def network_objects(self) -> NetworkObjects:
        """The interface object for the Network Objects Management.

        Returns:
            NetworkObjects: a NetworkObjects object

        Examples:
            >>> firewall.network_objects

        """
        return NetworkObjects(self)

    @property
    def service_applications(self) -> ServiceApplications:
        """The interface object for the Service & Applications Management.

        Returns:
            ServiceApplications: a ServiceApplications object

        Examples:
            >>> firewall.service_applications

        """
        return ServiceApplications(self)

    @property
    def access_control_nat(self) -> AccessControlNAT:
        """The interface object for the Access Control & NAT Management.

        Returns:
            AccessControlNAT: an AccessControlNAT object

        Examples:
            >>> firewall.access_control_nat

        """
        return AccessControlNAT(self)
