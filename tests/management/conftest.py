import pytest
import responses

from pycheckpoint_api.management import Management


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
    # Not all parameters from the response are tested here, the example is highly simplified here
    return {
        "from": 1,
        "to": 7,
        "total": 7,
        "objects": [
            "01f83a11-179a-405a-971a-50c58368f415",
            "27aabb7e-263a-4161-b822-0e0078c72e06",
            "2b486864-1356-4b66-ae6b-6eda09821955",
            "dd857ad5-a354-3991-cddc-58dc5ae69f65",
            "c9d1de16-407a-42bc-a28d-3b9d7f933766",
            "160de00a-c8b8-4cb4-ae4b-8623d0e6f8b6",
            "1741bb6c-3b19-456c-a635-b96c8456a0e8",
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


@pytest.fixture(name="management")
@responses.activate
def management(session):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/login",
        content_type="application/json",
        json=session,
        status=200,
    )

    fw = Management(
        user="test@example.com",
        password="false_strong_password",
        hostname="127.0.0.1",
        port=443,
        version="1.5",
    )

    assert (
        fw._session.headers["X-chkp-sid"]
        == "97BVpRfN4j81ogN-V2XqGYmw3DDwIhoSn0og8PiKDiM"
    )

    return fw
