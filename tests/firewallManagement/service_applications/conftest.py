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


@pytest.fixture(name="resp_service_udp")
def fixture_resp_service_udp():
    return {
        "uid": "64a4c8d1-7fed-4320-9826-0570bbb4a5bd",
        "name": "New_UDP_Service_1",
        "type": "service-udp",
        "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain",
        },
        "meta-info": {
            "lock": "unlocked",
            "validation-state": "ok",
            "last-modify-time": {
                "posix": 1479720338890,
                "iso-8601": "2016-11-21T11:25+0200",
            },
            "last-modifier": "aa",
            "creation-time": {
                "posix": 1479720338890,
                "iso-8601": "2016-11-21T11:25+0200",
            },
            "creator": "aa",
        },
        "tags": [],
        "read-only": True,
        "comments": "",
        "color": "black",
        "icon": "Services/UDPService",
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
        "accept-replies": False,
    }


@pytest.fixture(name="resp_service_icmp")
def fixture_resp_service_icmp():
    return {
        "uid": "22c8faba-3a24-4e99-ae6f-e798014facc2",
        "name": "Icmp1",
        "type": "service-icmp",
        "domain": {
            "domain-type": "domain",
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
        },
        "icmp-type": 5,
        "icmp-code": 7,
        "keep-connections-open-after-policy-installation": False,
        "meta-info": {
            "lock": "unlocked",
            "validation-state": "ok",
            "last-modify-time": {
                "posix": 1475051751286,
                "iso-8601": "2016-09-28T11:35+0300",
            },
            "last-modifier": "aa",
            "creation-time": {
                "posix": 1475051751286,
                "iso-8601": "2016-09-28T11:35+0300",
            },
            "creator": "aa",
        },
        "tags": [],
        "read-only": True,
        "comments": "",
        "color": "black",
        "icon": "Services/ICMPService",
        "groups": [],
    }


@pytest.fixture(name="resp_service_icmp6")
def fixture_resp_service_icmp6():
    return {
        "uid": "d9dcb753-1aa7-4e65-b5ff-b4878f8b3890",
        "name": "Icmp2",
        "type": "service-icmp6",
        "domain": {
            "domain-type": "domain",
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
        },
        "icmp-type": 5,
        "icmp-code": 7,
        "keep-connections-open-after-policy-installation": False,
        "meta-info": {
            "lock": "unlocked",
            "validation-state": "ok",
            "last-modify-time": {
                "posix": 1475051823316,
                "iso-8601": "2016-09-28T11:37+0300",
            },
            "last-modifier": "aa",
            "creation-time": {
                "posix": 1475051823316,
                "iso-8601": "2016-09-28T11:37+0300",
            },
            "creator": "aa",
        },
        "tags": [],
        "read-only": True,
        "comments": "",
        "color": "black",
        "icon": "Services/ICMPV6Service",
        "groups": [],
    }


@pytest.fixture(name="resp_service_sctp")
def fixture_resp_service_sctp():
    return {
        "uid": "d0385c6d-72dd-4981-b951-4783b7100343",
        "name": "New_SCTP_Service_1",
        "type": "service-sctp",
        "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain",
        },
        "meta-info": {
            "lock": "unlocked",
            "validation-state": "ok",
            "last-modify-time": {
                "posix": 1479720948687,
                "iso-8601": "2016-11-21T11:35+0200",
            },
            "last-modifier": "aa",
            "creation-time": {
                "posix": 1479720948687,
                "iso-8601": "2016-11-21T11:35+0200",
            },
            "creator": "aa",
        },
        "tags": [],
        "read-only": True,
        "comments": "",
        "color": "black",
        "icon": "Services/SCTPService",
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
    }


@pytest.fixture(name="resp_service_other")
def fixture_resp_service_other():
    return {
        "uid": "42f2b86e-09ee-415c-a6ae-75556c6c70e0",
        "name": "New_Service_1",
        "type": "service-other",
        "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain",
        },
        "meta-info": {
            "lock": "unlocked",
            "validation-state": "ok",
            "last-modify-time": {
                "posix": 1479721379028,
                "iso-8601": "2016-11-21T11:42+0200",
            },
            "last-modifier": "aa",
            "creation-time": {
                "posix": 1479721379028,
                "iso-8601": "2016-11-21T11:42+0200",
            },
            "creator": "aa",
        },
        "tags": [],
        "read-only": True,
        "comments": "",
        "color": "black",
        "icon": "Services/OtherService",
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
        "ip-protocol": 51,
        "accept-replies": False,
    }
