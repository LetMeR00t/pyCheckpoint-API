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


@pytest.fixture(name="resp_host")
def fixture_resp_host():
    return {
        "uid": "9423d36f-2d66-4754-b9e2-e7f4493756d4",
        "folder": {
            "uid": "feb54da1-c5e2-4e83-a3ed-d0601ba5ccb9",
            "name": "/Global Objects",
        },
        "domain": {
            "domain-type": "local domain",
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
        },
        "meta-info": {
            "lock": "unlocked",
            "validation-state": "ok",
            "read-only": False,
            "last-modify-time": {
                "posix": 1429440561055,
                "iso-8601": "2015-04-19T13:49+0300",
            },
            "last-modifier": "aa",
            "creation-time": {
                "posix": 1429440561055,
                "iso-8601": "2015-04-19T13:49+0300",
            },
            "creator": "aa",
        },
        "tags": [],
        "name": "New Host 4",
        "comments": "",
        "color": "black",
        "icon": "Objects/host",
        "groups": [],
        "nat-settings": {"auto-rule": False},
        "ipv4-address": "192.0.2.1",
        "ipv6-address": "",
    }


@pytest.fixture(name="resp_network")
def fixture_resp_network():
    return {
        "uid": "d5e8d56f-2d77-4824-a5d2-c4a7885dd4a7",
        "folder": {
            "uid": "feb54da1-c5e2-4e83-a3ed-d0601ba5ccb9",
            "name": "/Global Objects",
        },
        "domain": {
            "domain-type": "local domain",
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
        },
        "meta-info": {
            "lock": "unlocked",
            "validation-state": "ok",
            "read-only": False,
            "last-modify-time": {
                "posix": 1429440561055,
                "iso-8601": "2015-04-19T13:49+0300",
            },
            "last-modifier": "aa",
            "creation-time": {
                "posix": 1429440561055,
                "iso-8601": "2015-04-19T13:49+0300",
            },
            "creator": "aa",
        },
        "tags": [],
        "name": "New Network 4",
        "comments": "",
        "color": "black",
        "icon": "Objects/network",
        "groups": [],
        "nat-settings": {"auto-rule": False},
        "subnet": "192.0.2.0",
        "subnet-mask": "255.255.255.0",
    }


@pytest.fixture(name="resp_wildcard")
def fixture_resp_wildcard():
    return {
        "uid": "d8a5e4dd-2a93-4847-aaa8-d5d33a695da5",
        "folder": {
            "uid": "feb54da1-c5e2-4e83-a3ed-d0601ba5ccb9",
            "name": "/Global Objects",
        },
        "domain": {
            "domain-type": "local domain",
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
        },
        "meta-info": {
            "lock": "unlocked",
            "validation-state": "ok",
            "read-only": False,
            "last-modify-time": {
                "posix": 1429440561055,
                "iso-8601": "2015-04-19T13:49+0300",
            },
            "last-modifier": "aa",
            "creation-time": {
                "posix": 1429440561055,
                "iso-8601": "2015-04-19T13:49+0300",
            },
            "creator": "aa",
        },
        "tags": [],
        "name": "New Wildcard 4",
        "comments": "",
        "color": "black",
        "icon": "Objects/wildcard",
        "groups": [],
        "ipv4-address": "192.168.2.1",
        "ipv4-mask-wildcard": "0.0.0.128",
        "ipv6-address": "",
        "ipv6-mask-wildcard": "",
    }


@pytest.fixture(name="resp_group")
def fixture_resp_group():
    return {
        "uid": "ed997ff8-6709-4d71-a713-99bf01711cd5",
        "folder": {
            "uid": "5568324a-68ed-4c6c-9aa6-553978c7e746",
            "name": "/Global Objects",
        },
        "domain": {
            "domain-type": "local domain",
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
        },
        "meta-info": {
            "lock": "unlocked",
            "validation-state": "ok",
            "read-only": False,
            "last-modify-time": {
                "posix": 1435470206821,
                "iso-8601": "2015-06-28T08:43+0300",
            },
            "last-modifier": "aa",
            "creation-time": {
                "posix": 1435470206821,
                "iso-8601": "2015-06-28T08:43+0300",
            },
            "creator": "aa",
        },
        "tags": [],
        "name": "New Group 3",
        "comments": "",
        "color": "black",
        "icon": "General/group",
        "groups": [
            {
                "folder": {
                    "uid": "5568324a-68ed-4c6c-9aa6-553978c7e746",
                    "name": "/Global Objects",
                },
                "domain": {
                    "domain-type": "local domain",
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                },
                "type": "group",
                "name": "New Group 1",
                "uid": "d20710f1-831c-49dd-a009-aa9e569f643a",
            },
            {
                "folder": {
                    "uid": "5568324a-68ed-4c6c-9aa6-553978c7e746",
                    "name": "/Global Objects",
                },
                "domain": {
                    "domain-type": "local domain",
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                },
                "type": "group",
                "name": "New Group 2",
                "uid": "6e3e3f33-fc23-433d-ac90-d72196f9ffcf",
            },
        ],
        "members": [
            {
                "folder": {
                    "uid": "5568324a-68ed-4c6c-9aa6-553978c7e746",
                    "name": "/Global Objects",
                },
                "domain": {
                    "domain-type": "local domain",
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                },
                "type": "host",
                "name": "New Host 1",
                "uid": "280ff2f7-2ce2-42ac-a29f-cad26a4d6de5",
            }
        ],
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
