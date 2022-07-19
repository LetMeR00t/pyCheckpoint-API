import pytest


@pytest.fixture(name="resp_package")
def fixture_resp_package():
    # Not all parameters from the response are tested here
    return {
        "uid": "38b4ed6e-711c-49fa-b9f4-638290d621be",
        "folder": {
            "uid": "3a1d42e8-b138-4f91-bf9e-4c79247d2ded",
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
                "posix": 1430896142009,
                "iso-8601": "2015-05-06T10:09+0300",
            },
            "last-modifier": "aa",
            "creation-time": {
                "posix": 1430896142009,
                "iso-8601": "2015-05-06T10:09+0300",
            },
            "creator": "aa",
        },
        "tags": ["t1"],
        "name": "New Standard Package 1",
        "comments": "My Comments",
        "color": "green",
        "icon": "Blades/Access",
        "access": True,
        "access-layers": [
            {
                "folder": {
                    "uid": "3a1d42e8-b138-4f91-bf9e-4c79247d2ded",
                    "name": "/Global Objects",
                },
                "domain": {
                    "domain-type": "local domain",
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                },
                "type": "layer",
                "name": "New Standard Package 1 Network",
                "uid": "0029eebd-27a3-4a9f-a9e4-20e083226555",
            }
        ],
        "vpn-traditional-mode": False,
        "nat-policy": True,
        "qos": False,
        "qos-policy-type": "recommended",
        "desktop-security": False,
        "threat-prevention": False,
        "installation-targets": "all",
    }
