import pytest
import responses

from pycheckpoint_api.firewallManagement import FirewallManagementAPI


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


@pytest.fixture(name="resp_message_ok")
def fixture_resp_message_ok():
    return {"message": "OK"}


@pytest.fixture(name="resp_message_ok_with_number_of_discarded_changes")
def fixture_resp_message_ok_with_number_of_discarded_changes():
    return {"message": "OK", "number-of-discarded-changes": 0}


@pytest.fixture(name="resp_automatic_purge")
def fixture_resp_automatic_purge():
    return {
        "enabled": True,
        "keep-sessions-by-count": True,
        "number-of-sessions-to-keep": "10",
        "keep-sessions-by-days": False,
        "number-of-days-to-keep": "0",
        "scheduling": {
            "check-interval": 21,
            "time-units": "days",
            "start-date": "2020-04-24T12:00:00",
            "last-check": "",
            "next-check": "2020-04-24T12:00:00",
        },
    }


@pytest.fixture(name="resp_task")
def fixture_resp_task():
    return {"task-id": "01234567-89ab-cdef-a930-8c37a59972b3"}


@pytest.fixture(name="resp_session")
def fixture_resp_session():
    # Not all parameters from the response are tested here
    return {
        "name": "CustomName",
        "uid": "7a13a360-9b24-40d7-acd3-5b50247be33e",
    }


@pytest.fixture(name="resp_from_to_objects")
def fixture_resp_from_to_objects():
    # Not all parameters from the response are tested here
    return {
        "from": 1,
        "to": 3,
        "total": 3,
        "objects": [
            "01f83a11-179a-405a-971a-50c58368f415",
            "27aabb7e-263a-4161-b822-0e0078c72e06",
            "2b486864-1356-4b66-ae6b-6eda09821955",
        ],
    }


@pytest.fixture(name="resp_login_message")
def fixture_resp_login_message():
    return {
        "type": "A",
        "header": "D",
        "message": "C",
        "show-message": True,
        "warning": True,
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
        user="test@example.com",
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
