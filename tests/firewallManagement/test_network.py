# from box import Box
import responses
import pytest

# from pycheckpoint.firewallManagement.exception import MandatoryFieldMissing


@pytest.fixture(name="resp_host")
def fixture_session():
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


@responses.activate
def test_add_host(firewallManagement, resp_host):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-host",
        json=resp_host,
        status=200,
    )

    resp = firewallManagement.network.add_host(
        name="New Host 4", ip_address="192.0.2.1"
    )

    assert resp.name == "New Host 4"
    assert resp.ipv4_address == "192.0.2.1"
