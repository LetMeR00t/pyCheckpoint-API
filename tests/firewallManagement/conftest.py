import pytest
import responses

from pycheckpoint.firewallManagement import FirewallManagementAPI


@pytest.fixture(name="session")
def fixture_session():
    return {
        "sid": "97BVpRfN4j81ogN-V2XqGYmw3DDwIhoSn0og8PiKDiM",
        "url": "https://127.0.0.1:443/web_api",
        "uid": "7a13a360-9b24-40d7-acd3-5b50247be33e",
        "session-timeout": 600,
        "last-login-was-at": {
            "posix": 1430032266851,
            "iso-8601": "2015-04-26T10:11+0300",
        },
    }


@pytest.fixture(name="firewallManagement")
@responses.activate
def firewallManagement(session):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/login",
        content_type="application/json",
        json=session,
        status=200,
    )

    firewallManagementAPI = FirewallManagementAPI(
        username="test@example.com",
        password="false_strong_password",
        hostname="127.0.0.1",
        port=443,
        version="1.5",
    )

    assert (
        firewallManagementAPI._session.headers["X-chkp-sid"]
        == "97BVpRfN4j81ogN-V2XqGYmw3DDwIhoSn0og8PiKDiM"
    )

    return firewallManagementAPI
