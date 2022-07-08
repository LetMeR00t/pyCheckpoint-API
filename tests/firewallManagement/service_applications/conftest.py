import pytest


@pytest.fixture(name="resp_service_tcp")
def fixture_resp_service_tcp():
    return {
        "uid": "bee785c5-998b-4a45-80e8-3fa91181aba9",
        "name": "New_TCP_Service_1",
        "type": "service-tcp",
        "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain",
        },
        "meta-info": {
            "lock": "unlocked",
            "validation-state": "ok",
            "last-modify-time": {
                "posix": 1479719218212,
                "iso-8601": "2016-11-21T11:06+0200",
            },
            "last-modifier": "aa",
            "creation-time": {
                "posix": 1479719218212,
                "iso-8601": "2016-11-21T11:06+0200",
            },
            "creator": "aa",
        },
        "tags": [],
        "read-only": True,
        "comments": "",
        "color": "black",
        "icon": "Services/TCPService",
        "groups": [],
        "keep-connections-open-after-policy-installation": False,
        "session-timeout": 0,
        "use-default-session-timeout": True,
        "match-for-any": True,
        "sync-connections-on-cluster": True,
        "aggressive-aging": {
            "enable": True,
            "timeout": 360,
            "use-default-timeout": False,
            "default-timeout": 0,
        },
        "port": "5669",
        "match-by-protocol-signature": False,
    }
