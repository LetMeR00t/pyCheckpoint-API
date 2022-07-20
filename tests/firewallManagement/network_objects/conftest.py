import pytest


@pytest.fixture(name="resp_host_ipv4")
def fixture_resp_host_ipv4():
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
        "tags": ["t1", "t2", "t3"],
        "name": "New Host 4",
        "comments": "",
        "color": "black",
        "icon": "Objects/host",
        "groups": [],
        "nat-settings": {"auto-rule": False},
        "ipv4-address": "192.0.2.1",
        "ipv6-address": "",
    }


@pytest.fixture(name="resp_host_ipv6")
def fixture_resp_host_ipv6():
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
        "tags": ["t1", "t2", "t3"],
        "name": "New Host 4",
        "comments": "",
        "color": "black",
        "icon": "Objects/host",
        "groups": [],
        "nat-settings": {"auto-rule": False},
        "ipv4-address": "",
        "ipv6-address": "2001:db8:0000:0000:0000:0000:0000:0005",
    }


@pytest.fixture(name="resp_network_ipv4")
def fixture_resp_network_ipv4():
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
        "tags": [
            {
                "folder": {
                    "uid": "a25a7783-9adb-4a65-9850-b97ee7860530",
                    "name": "/Global Objects",
                },
                "domain": {
                    "domain-type": "local domain",
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                },
                "type": "tag",
                "name": "tag1",
                "uid": "687715ca-674b-4642-981b-b6243fde04c0",
            }
        ],
        "name": "New Network 4",
        "comments": "",
        "color": "black",
        "icon": "Objects/network",
        "groups": [],
        "nat-settings": {"auto-rule": False},
        "subnet": "192.0.2.0",
        "subnet-mask": "255.255.255.0",
    }


@pytest.fixture(name="resp_network_ipv6")
def fixture_resp_network_ipv6():
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
        "tags": [
            {
                "folder": {
                    "uid": "a25a7783-9adb-4a65-9850-b97ee7860530",
                    "name": "/Global Objects",
                },
                "domain": {
                    "domain-type": "local domain",
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                },
                "type": "tag",
                "name": "tag1",
                "uid": "687715ca-674b-4642-981b-b6243fde04c0",
            }
        ],
        "name": "New Network 4",
        "comments": "",
        "color": "black",
        "icon": "Objects/network",
        "groups": [],
        "nat-settings": {"auto-rule": False},
        "subnet6": "2001:0DB8:ABCD:0012:0000:0000:0000:0005",
        "mask-length6": 128,
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
        "tags": [
            {
                "folder": {
                    "uid": "a25a7783-9adb-4a65-9850-b97ee7860530",
                    "name": "/Global Objects",
                },
                "domain": {
                    "domain-type": "local domain",
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                },
                "type": "tag",
                "name": "tag1",
                "uid": "687715ca-674b-4642-981b-b6243fde04c0",
            }
        ],
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
        "tags": [
            {
                "folder": {
                    "uid": "a25a7783-9adb-4a65-9850-b97ee7860530",
                    "name": "/Global Objects",
                },
                "domain": {
                    "domain-type": "local domain",
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                },
                "type": "tag",
                "name": "tag1",
                "uid": "687715ca-674b-4642-981b-b6243fde04c0",
            }
        ],
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


@pytest.fixture(name="resp_gsn_handover_group")
def fixture_resp_gsn_handover_group():
    return {
        "uid": "f140a9d1-4167-456a-931d-abdaa4c8aa7e",
        "name": "gsnhandovergroup",
        "type": "gsn-handover-group",
        "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain",
        },
        "tags": [
            {
                "folder": {
                    "uid": "a25a7783-9adb-4a65-9850-b97ee7860530",
                    "name": "/Global Objects",
                },
                "domain": {
                    "domain-type": "local domain",
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                },
                "type": "tag",
                "name": "tag1",
                "uid": "687715ca-674b-4642-981b-b6243fde04c0",
            }
        ],
        "read-only": True,
        "comments": "",
        "color": "black",
        "icon": "General/group",
        "groups": [],
        "members": [
            {
                "uid": "29438958-5569-49b7-a270-dfff5be51c3a",
                "name": "All_Internet",
                "type": "address-range",
                "domain": {
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                    "domain-type": "domain",
                },
                "ipv4-address-first": "10.0.0.0",
                "ipv4-address-last": "255.255.255.255",
            }
        ],
        "enforce-gtp": True,
        "gtp-rate": 2048,
    }


@pytest.fixture(name="resp_address_range_ipv4")
def fixture_resp_address_range_ipv4():
    return {
        "uid": "196e93a9-b90b-4ab1-baa6-124e7289aa20",
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
                "posix": 1435470754504,
                "iso-8601": "2015-06-28T08:52+0300",
            },
            "last-modifier": "aa",
            "creation-time": {
                "posix": 1435470754504,
                "iso-8601": "2015-06-28T08:52+0300",
            },
            "creator": "aa",
        },
        "tags": [
            {
                "folder": {
                    "uid": "a25a7783-9adb-4a65-9850-b97ee7860530",
                    "name": "/Global Objects",
                },
                "domain": {
                    "domain-type": "local domain",
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                },
                "type": "tag",
                "name": "tag1",
                "uid": "687715ca-674b-4642-981b-b6243fde04c0",
            }
        ],
        "name": "New Address Range 1",
        "comments": "",
        "color": "black",
        "icon": "Objects/ip",
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
        "nat-settings": {"auto-rule": False},
        "ipv4-address-first": "192.0.2.1",
        "ipv4-address-last": "192.0.2.10",
        "ipv6-address-first": "",
        "ipv6-address-last": "",
    }


@pytest.fixture(name="resp_address_range_ipv6")
def fixture_resp_address_range_ipv6():
    return {
        "uid": "196e93a9-b90b-4ab1-baa6-124e7289aa20",
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
                "posix": 1435470754504,
                "iso-8601": "2015-06-28T08:52+0300",
            },
            "last-modifier": "aa",
            "creation-time": {
                "posix": 1435470754504,
                "iso-8601": "2015-06-28T08:52+0300",
            },
            "creator": "aa",
        },
        "tags": [
            {
                "folder": {
                    "uid": "a25a7783-9adb-4a65-9850-b97ee7860530",
                    "name": "/Global Objects",
                },
                "domain": {
                    "domain-type": "local domain",
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                },
                "type": "tag",
                "name": "tag1",
                "uid": "687715ca-674b-4642-981b-b6243fde04c0",
            }
        ],
        "name": "New Address Range 1",
        "comments": "",
        "color": "black",
        "icon": "Objects/ip",
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
        "nat-settings": {"auto-rule": False},
        "ipv4-address-first": "",
        "ipv4-address-last": "",
        "ipv6-address-first": "2001:db8::",
        "ipv6-address-last": "2001:db8:0000:0000:0000:0000:0000:000f",
    }


@pytest.fixture(name="resp_multicast_address_range_single_ip")
def fixture_resp_multicast_address_range_single_ip():
    return {
        "uid": "faff3fdf-01b9-4c58-97dc-176c409b5bc1",
        "name": "New Multicast Address Range",
        "type": "multicast-address-range",
        "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain",
        },
        "meta-info": {
            "lock": "unlocked",
            "validation-state": "ok",
            "last-modify-time": {
                "posix": 1483966213026,
                "iso-8601": "2017-01-09T14:50+0200",
            },
            "last-modifier": "aa",
            "creation-time": {
                "posix": 1483966213026,
                "iso-8601": "2017-01-09T14:50+0200",
            },
            "creator": "aa",
        },
        "tags": [
            {
                "folder": {
                    "uid": "a25a7783-9adb-4a65-9850-b97ee7860530",
                    "name": "/Global Objects",
                },
                "domain": {
                    "domain-type": "local domain",
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                },
                "type": "tag",
                "name": "tag1",
                "uid": "687715ca-674b-4642-981b-b6243fde04c0",
            }
        ],
        "read-only": True,
        "comments": "",
        "color": "black",
        "icon": "Objects/ip",
        "groups": [],
        "ipv4-address-first": "224.0.0.5",
        "ipv4-address-last": "224.0.0.5",
    }


@pytest.fixture(name="resp_multicast_address_range_ipv4")
def fixture_resp_multicast_address_range_ipv4():
    return {
        "uid": "faff3fdf-01b9-4c58-97dc-176c409b5bc1",
        "name": "New Multicast Address Range",
        "type": "multicast-address-range",
        "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain",
        },
        "meta-info": {
            "lock": "unlocked",
            "validation-state": "ok",
            "last-modify-time": {
                "posix": 1483966213026,
                "iso-8601": "2017-01-09T14:50+0200",
            },
            "last-modifier": "aa",
            "creation-time": {
                "posix": 1483966213026,
                "iso-8601": "2017-01-09T14:50+0200",
            },
            "creator": "aa",
        },
        "tags": [
            {
                "folder": {
                    "uid": "a25a7783-9adb-4a65-9850-b97ee7860530",
                    "name": "/Global Objects",
                },
                "domain": {
                    "domain-type": "local domain",
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                },
                "type": "tag",
                "name": "tag1",
                "uid": "687715ca-674b-4642-981b-b6243fde04c0",
            }
        ],
        "read-only": True,
        "comments": "",
        "color": "black",
        "icon": "Objects/ip",
        "groups": [],
        "ipv4-address-first": "224.0.0.1",
        "ipv4-address-last": "224.0.0.4",
    }


@pytest.fixture(name="resp_multicast_address_range_ipv6")
def fixture_resp_multicast_address_range_ipv6():
    return {
        "uid": "faff3fdf-01b9-4c58-97dc-176c409b5bc1",
        "name": "New Multicast Address Range",
        "type": "multicast-address-range",
        "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain",
        },
        "meta-info": {
            "lock": "unlocked",
            "validation-state": "ok",
            "last-modify-time": {
                "posix": 1483966213026,
                "iso-8601": "2017-01-09T14:50+0200",
            },
            "last-modifier": "aa",
            "creation-time": {
                "posix": 1483966213026,
                "iso-8601": "2017-01-09T14:50+0200",
            },
            "creator": "aa",
        },
        "tags": [
            {
                "folder": {
                    "uid": "a25a7783-9adb-4a65-9850-b97ee7860530",
                    "name": "/Global Objects",
                },
                "domain": {
                    "domain-type": "local domain",
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                },
                "type": "tag",
                "name": "tag1",
                "uid": "687715ca-674b-4642-981b-b6243fde04c0",
            }
        ],
        "read-only": True,
        "comments": "",
        "color": "black",
        "icon": "Objects/ip",
        "groups": [],
        "ipv6-address-first": "2001:db8:0000:0000:0000:0000:0000:0002",
        "ipv6-address-last": "2001:db8:0000:0000:0000:0000:0000:0004",
    }


@pytest.fixture(name="resp_group_with_exclusion")
def fixture_resp_group_with_exclusion():
    return {
        "uid": "dce451da-c9c7-46a9-bdb5-8fc953a6f172",
        "name": "DemoGroupWithExclusion",
        "type": "group-with-exclusion",
        "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain",
        },
        "meta-info": {
            "lock": "locked by current session",
            "validation-state": "ok",
            "last-modify-time": {
                "posix": 1528268215283,
                "iso-8601": "2018-06-06T09:56+0300",
            },
            "last-modifier": "aa",
            "creation-time": {
                "posix": 1528268215283,
                "iso-8601": "2018-06-06T09:56+0300",
            },
            "creator": "aa",
        },
        "tags": [
            {
                "folder": {
                    "uid": "a25a7783-9adb-4a65-9850-b97ee7860530",
                    "name": "/Global Objects",
                },
                "domain": {
                    "domain-type": "local domain",
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                },
                "type": "tag",
                "name": "tag1",
                "uid": "687715ca-674b-4642-981b-b6243fde04c0",
            }
        ],
        "read-only": False,
        "comments": "",
        "color": "black",
        "icon": "General/group",
        "ranges": {
            "ipv4": [
                {"start": "10.10.10.0", "end": "10.10.10.127"},
                {"start": "10.10.14.1", "end": "10.10.14.1"},
            ],
            "ipv6": [],
            "others": [],
            "excluded-others": [],
        },
    }


@pytest.fixture(name="resp_simple_gateway_ipv4")
def fixture_resp_simple_gateway_ipv4():
    return {
        "uid": "99457705-dc26-40ce-b9cd-5633eb09b1aa",
        "domain": {
            "domain-type": "domain",
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
        },
        "meta-info": {
            "lock": "unlocked",
            "validation-state": "ok",
            "read-only": False,
            "last-modify-time": {
                "posix": 1451485835851,
                "iso-8601": "2015-12-30T16:30+0200",
            },
            "last-modifier": "aa",
            "creation-time": {
                "posix": 1451485835851,
                "iso-8601": "2015-12-30T16:30+0200",
            },
            "creator": "aa",
        },
        "tags": [
            {
                "folder": {
                    "uid": "a25a7783-9adb-4a65-9850-b97ee7860530",
                    "name": "/Global Objects",
                },
                "domain": {
                    "domain-type": "local domain",
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                },
                "type": "tag",
                "name": "tag1",
                "uid": "687715ca-674b-4642-981b-b6243fde04c0",
            }
        ],
        "name": "gw1",
        "comments": "",
        "color": "black",
        "icon": "General/globalsNa",
        "groups": [],
        "ipv4-address": "192.0.2.1",
        "ipv6-address": "::0",
        "dynamic-ip": False,
        "version": "R80",
        "os-name": "Gaia",
        "hardware": "Open server",
        "sic-name": "",
        "sic-state": "uninitialized",
        "interfaces": [],
        "firewall": True,
        "firewall-settings": {
            "auto-maximum-limit-for-concurrent-connections": True,
            "maximum-limit-for-concurrent-connections": 25000,
            "auto-calculate-connections-hash-table-size-and-memory-pool": True,
            "connections-hash-size": 131072,
            "memory-pool-size": 6,
            "maximum-memory-pool-size": 30,
        },
        "vpn": False,
        "application-control": False,
        "url-filtering": False,
        "data-awareness": False,
        "ips": False,
        "anti-bot": False,
        "anti-virus": False,
        "threat-emulation": False,
        "save-logs-locally": False,
        "send-alerts-to-server": ["test_server_1"],
        "send-logs-to-server": ["test_server_2"],
        "send-logs-to-backup-server": [],
        "logs-settings": {
            "rotate-log-by-file-size": False,
            "rotate-log-file-size-threshold": 1000,
            "rotate-log-on-schedule": False,
            "alert-when-free-disk-space-below-metrics": "mbytes",
            "alert-when-free-disk-space-below": True,
            "alert-when-free-disk-space-below-threshold": 20,
            "alert-when-free-disk-space-below-type": "popup alert",
            "delete-when-free-disk-space-below-metrics": "mbytes",
            "delete-when-free-disk-space-below": True,
            "delete-when-free-disk-space-below-threshold": 5000,
            "before-delete-keep-logs-from-the-last-days": False,
            "before-delete-keep-logs-from-the-last-days-threshold": 0,
            "before-delete-run-script": False,
            "before-delete-run-script-command": "",
            "stop-logging-when-free-disk-space-below-metrics": "mbytes",
            "stop-logging-when-free-disk-space-below": True,
            "stop-logging-when-free-disk-space-below-threshold": 100,
            "reject-connections-when-free-disk-space-below-threshold": False,
            "reserve-for-packet-capture-metrics": "mbytes",
            "reserve-for-packet-capture-threshold": 500,
            "delete-index-files-when-index-size-above-metrics": "mbytes",
            "delete-index-files-when-index-size-above": False,
            "delete-index-files-when-index-size-above-threshold": 100000,
            "delete-index-files-older-than-days": True,
            "delete-index-files-older-than-days-threshold": 14,
            "forward-logs-to-log-server": False,
            "perform-log-rotate-before-log-forwarding": False,
            "update-account-log-every": 3600,
            "detect-new-citrix-ica-application-names": False,
            "turn-on-qos-logging": True,
        },
    }


@pytest.fixture(name="resp_simple_gateway_ipv6")
def fixture_resp_simple_gateway_ipv6():
    return {
        "uid": "99457705-dc26-40ce-b9cd-5633eb09b1aa",
        "domain": {
            "domain-type": "domain",
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
        },
        "meta-info": {
            "lock": "unlocked",
            "validation-state": "ok",
            "read-only": False,
            "last-modify-time": {
                "posix": 1451485835851,
                "iso-8601": "2015-12-30T16:30+0200",
            },
            "last-modifier": "aa",
            "creation-time": {
                "posix": 1451485835851,
                "iso-8601": "2015-12-30T16:30+0200",
            },
            "creator": "aa",
        },
        "tags": [
            {
                "folder": {
                    "uid": "a25a7783-9adb-4a65-9850-b97ee7860530",
                    "name": "/Global Objects",
                },
                "domain": {
                    "domain-type": "local domain",
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                },
                "type": "tag",
                "name": "tag1",
                "uid": "687715ca-674b-4642-981b-b6243fde04c0",
            }
        ],
        "name": "gw1",
        "comments": "",
        "color": "black",
        "icon": "General/globalsNa",
        "groups": [],
        "ipv4-address": "",
        "ipv6-address": "2001:db8:0000:0000:0000:0000:0000:000c",
        "dynamic-ip": False,
        "version": "R80",
        "os-name": "Gaia",
        "hardware": "Open server",
        "sic-name": "",
        "sic-state": "uninitialized",
        "interfaces": [],
        "firewall": True,
        "firewall-settings": {
            "auto-maximum-limit-for-concurrent-connections": True,
            "maximum-limit-for-concurrent-connections": 25000,
            "auto-calculate-connections-hash-table-size-and-memory-pool": True,
            "connections-hash-size": 131072,
            "memory-pool-size": 6,
            "maximum-memory-pool-size": 30,
        },
        "vpn": False,
        "application-control": False,
        "url-filtering": False,
        "data-awareness": False,
        "ips": False,
        "anti-bot": False,
        "anti-virus": False,
        "threat-emulation": False,
        "save-logs-locally": False,
        "send-alerts-to-server": ["test_server_1"],
        "send-logs-to-server": ["test_server_2"],
        "send-logs-to-backup-server": [],
        "logs-settings": {
            "rotate-log-by-file-size": False,
            "rotate-log-file-size-threshold": 1000,
            "rotate-log-on-schedule": False,
            "alert-when-free-disk-space-below-metrics": "mbytes",
            "alert-when-free-disk-space-below": True,
            "alert-when-free-disk-space-below-threshold": 20,
            "alert-when-free-disk-space-below-type": "popup alert",
            "delete-when-free-disk-space-below-metrics": "mbytes",
            "delete-when-free-disk-space-below": True,
            "delete-when-free-disk-space-below-threshold": 5000,
            "before-delete-keep-logs-from-the-last-days": False,
            "before-delete-keep-logs-from-the-last-days-threshold": 0,
            "before-delete-run-script": False,
            "before-delete-run-script-command": "",
            "stop-logging-when-free-disk-space-below-metrics": "mbytes",
            "stop-logging-when-free-disk-space-below": True,
            "stop-logging-when-free-disk-space-below-threshold": 100,
            "reject-connections-when-free-disk-space-below-threshold": False,
            "reserve-for-packet-capture-metrics": "mbytes",
            "reserve-for-packet-capture-threshold": 500,
            "delete-index-files-when-index-size-above-metrics": "mbytes",
            "delete-index-files-when-index-size-above": False,
            "delete-index-files-when-index-size-above-threshold": 100000,
            "delete-index-files-older-than-days": True,
            "delete-index-files-older-than-days-threshold": 14,
            "forward-logs-to-log-server": False,
            "perform-log-rotate-before-log-forwarding": False,
            "update-account-log-every": 3600,
            "detect-new-citrix-ica-application-names": False,
            "turn-on-qos-logging": True,
        },
    }


@pytest.fixture(name="resp_simple_cluster_ipv4")
def fixture_resp_simple_cluster_ipv4():
    return {
        "uid": "4a5d882a-5568-2c3b-aa78-751ab23d6c11",
        "name": "cluster1",
        "color": "yellow",
        "version": "R80.30",
        "ipv4-address": "17.23.5.1",
        "ipv6-address": "",
        "os-name": "Gaia",
        "cluster-mode": "cluster-xl-ha",
        "firewall": True,
        "vpn": False,
        "interfaces": [
            {
                "name": "eth0",
                "ip-address": "17.23.5.1",
                "network-mask": "255.255.255.0",
                "interface-type": "cluster",
                "topology": "EXTERNAL",
                "anti-spoofing": True,
            },
            {
                "name": "eth1",
                "interface-type": "sync",
                "topology": "INTERNAL",
                "topology-settings": {
                    "ip-address-behind-this-interface": "network defined by the interface ip and net mask",
                    "interface-leads-to-dmz": False,
                },
            },
            {
                "name": "eth2",
                "ip-address": "192.168.1.1",
                "network-mask": "255.255.255.0",
                "interface-type": "cluster",
                "topology": "INTERNAL",
                "anti-spoofing": True,
                "topology-settings": {
                    "ip-address-behind-this-interface": "network defined by the interface ip and net mask",
                    "interface-leads-to-dmz": False,
                },
            },
        ],
        "members": [
            {
                "name": "member1",
                "one-time-password": "abcd",
                "ip-address": "17.23.5.2",
                "interfaces": [
                    {
                        "name": "eth0",
                        "ip-address": "17.23.5.2",
                        "network-mask": "255.255.255.0",
                    },
                    {
                        "name": "eth1",
                        "ip-address": "1.1.2.4",
                        "network-mask": "255.255.255.0",
                    },
                    {
                        "name": "eth2",
                        "ip-address": "192.168.1.2",
                        "network-mask": "255.255.255.0",
                    },
                ],
            },
            {
                "name": "member2",
                "one-time-password": "abcd",
                "ip-address": "17.23.5.3",
                "interfaces": [
                    {
                        "name": "eth0",
                        "ip-address": "17.23.5.3",
                        "network-mask": "255.255.255.0",
                    },
                    {
                        "name": "eth1",
                        "ip-address": "1.1.2.5",
                        "network-mask": "255.255.255.0",
                    },
                    {
                        "name": "eth2",
                        "ip-address": "192.168.1.3",
                        "network-mask": "255.255.255.0",
                    },
                ],
            },
        ],
    }


@pytest.fixture(name="resp_simple_cluster_ipv6")
def fixture_resp_simple_cluster_ipv6():
    return {
        "uid": "4a5d882a-5568-2c3b-aa78-751ab23d6c11",
        "name": "cluster1",
        "color": "yellow",
        "version": "R80.30",
        "ipv4-address": "",
        "ipv6-address": "2001:db8:0000:0000:0000:0000:0000:000b",
        "os-name": "Gaia",
        "cluster-mode": "cluster-xl-ha",
        "firewall": True,
        "vpn": False,
        "interfaces": [
            {
                "name": "eth0",
                "ip-address": "17.23.5.1",
                "network-mask": "255.255.255.0",
                "interface-type": "cluster",
                "topology": "EXTERNAL",
                "anti-spoofing": True,
            },
            {
                "name": "eth1",
                "interface-type": "sync",
                "topology": "INTERNAL",
                "topology-settings": {
                    "ip-address-behind-this-interface": "network defined by the interface ip and net mask",
                    "interface-leads-to-dmz": False,
                },
            },
            {
                "name": "eth2",
                "ip-address": "192.168.1.1",
                "network-mask": "255.255.255.0",
                "interface-type": "cluster",
                "topology": "INTERNAL",
                "anti-spoofing": True,
                "topology-settings": {
                    "ip-address-behind-this-interface": "network defined by the interface ip and net mask",
                    "interface-leads-to-dmz": False,
                },
            },
        ],
        "members": [
            {
                "name": "member1",
                "one-time-password": "abcd",
                "ip-address": "17.23.5.2",
                "interfaces": [
                    {
                        "name": "eth0",
                        "ip-address": "17.23.5.2",
                        "network-mask": "255.255.255.0",
                    },
                    {
                        "name": "eth1",
                        "ip-address": "1.1.2.4",
                        "network-mask": "255.255.255.0",
                    },
                    {
                        "name": "eth2",
                        "ip-address": "192.168.1.2",
                        "network-mask": "255.255.255.0",
                    },
                ],
            },
            {
                "name": "member2",
                "one-time-password": "abcd",
                "ip-address": "17.23.5.3",
                "interfaces": [
                    {
                        "name": "eth0",
                        "ip-address": "17.23.5.3",
                        "network-mask": "255.255.255.0",
                    },
                    {
                        "name": "eth1",
                        "ip-address": "1.1.2.5",
                        "network-mask": "255.255.255.0",
                    },
                    {
                        "name": "eth2",
                        "ip-address": "192.168.1.3",
                        "network-mask": "255.255.255.0",
                    },
                ],
            },
        ],
    }


@pytest.fixture(name="resp_get_interfaces")
def fixture_resp_get_interfaces():
    return {
        "tasks": [
            {
                "task-name": "get-interfaces",
                "task-id": "01234567-89ab-cdef-9e1f-0e1e68312345",
                "status": "succeeded",
                "progress-percentage": 100,
                "suppressed": False,
                "task-details": [{"interfaces": ["eth0", "eth1"]}],
            }
        ]
    }


@pytest.fixture(name="resp_checkpoint_host_ipv4")
def fixture_resp_checkpoint_host_ipv4():
    return {
        "uid": "f50f3810-d16c-4239-88d0-9f37ac581387",
        "name": "secondarylogserver",
        "type": "checkpoint-host",
        "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain",
        },
        "tags": [
            {
                "folder": {
                    "uid": "a25a7783-9adb-4a65-9850-b97ee7860530",
                    "name": "/Global Objects",
                },
                "domain": {
                    "domain-type": "local domain",
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                },
                "type": "tag",
                "name": "tag1",
                "uid": "687715ca-674b-4642-981b-b6243fde04c0",
            }
        ],
        "read-only": True,
        "comments": "",
        "color": "black",
        "icon": "General/globalsNa",
        "groups": [],
        "nat-settings": {"auto-rule": False},
        "ipv4-address": "5.5.5.5",
        "interfaces": [],
        "version": "R81",
        "os": "Gaia",
        "hardware": "Open server",
        "sic-state": "uninitialized",
        "management-blades": {
            "logging-and-status": True,
            "smart-event-server": False,
            "smart-event-correlation": False,
            "network-policy-management": True,
            "user-directory": False,
            "compliance": False,
            "endpoint-policy": False,
            "secondary": True,
            "identity-logging": False,
        },
        "logs-settings": {
            "rotate-log-by-file-size": False,
            "rotate-log-file-size-threshold": 1000,
            "rotate-log-on-schedule": False,
            "alert-when-free-disk-space-below-metrics": "mbytes",
            "alert-when-free-disk-space-below": True,
            "alert-when-free-disk-space-below-threshold": 20,
            "alert-when-free-disk-space-below-type": "popup alert",
            "delete-when-free-disk-space-below-metrics": "mbytes",
            "delete-when-free-disk-space-below": True,
            "delete-when-free-disk-space-below-threshold": 5000,
            "before-delete-keep-logs-from-the-last-days": False,
            "before-delete-keep-logs-from-the-last-days-threshold": 3664,
            "before-delete-run-script": False,
            "before-delete-run-script-command": "",
            "stop-logging-when-free-disk-space-below-metrics": "mbytes",
            "stop-logging-when-free-disk-space-below": False,
            "stop-logging-when-free-disk-space-below-threshold": 100,
            "delete-index-files-older-than-days": False,
            "delete-index-files-older-than-days-threshold": 14,
            "forward-logs-to-log-server": False,
            "update-account-log-every": 3600,
            "detect-new-citrix-ica-application-names": False,
            "turn-on-qos-logging": True,
            "enable-log-indexing": True,
            "smart-event-intro-correlation-unit": True,
            "accept-syslog-messages": False,
        },
        "send-alerts-to-server": [
            {
                "uid": "6da0cc30-4ac4-c544-bd20-d8ba9bf7f51c",
                "name": "ice-main-take-183",
                "type": "checkpoint-host",
                "domain": {
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                    "domain-type": "domain",
                },
            }
        ],
        "send-logs-to-server": [
            {
                "uid": "6da0cc30-4ac4-c544-bd20-d8ba9bf7f51c",
                "name": "ice-main-take-183",
                "type": "checkpoint-host",
                "domain": {
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                    "domain-type": "domain",
                },
            }
        ],
        "send-logs-to-backup-server": [],
        "save-logs-locally": False,
    }


@pytest.fixture(name="resp_checkpoint_host_ipv6")
def fixture_resp_checkpoint_host_ipv6():
    return {
        "uid": "f50f3810-d16c-4239-88d0-9f37ac581387",
        "name": "secondarylogserver",
        "type": "checkpoint-host",
        "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain",
        },
        "tags": [
            {
                "folder": {
                    "uid": "a25a7783-9adb-4a65-9850-b97ee7860530",
                    "name": "/Global Objects",
                },
                "domain": {
                    "domain-type": "local domain",
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                },
                "type": "tag",
                "name": "tag1",
                "uid": "687715ca-674b-4642-981b-b6243fde04c0",
            }
        ],
        "read-only": True,
        "comments": "",
        "color": "black",
        "icon": "General/globalsNa",
        "groups": [],
        "nat-settings": {"auto-rule": False},
        "ipv6-address": "2001:db8:0000:0000:0000:0000:0000:000a",
        "interfaces": [],
        "version": "R81",
        "os": "Gaia",
        "hardware": "Open server",
        "sic-state": "uninitialized",
        "management-blades": {
            "logging-and-status": True,
            "smart-event-server": False,
            "smart-event-correlation": False,
            "network-policy-management": True,
            "user-directory": False,
            "compliance": False,
            "endpoint-policy": False,
            "secondary": True,
            "identity-logging": False,
        },
        "logs-settings": {
            "rotate-log-by-file-size": False,
            "rotate-log-file-size-threshold": 1000,
            "rotate-log-on-schedule": False,
            "alert-when-free-disk-space-below-metrics": "mbytes",
            "alert-when-free-disk-space-below": True,
            "alert-when-free-disk-space-below-threshold": 20,
            "alert-when-free-disk-space-below-type": "popup alert",
            "delete-when-free-disk-space-below-metrics": "mbytes",
            "delete-when-free-disk-space-below": True,
            "delete-when-free-disk-space-below-threshold": 5000,
            "before-delete-keep-logs-from-the-last-days": False,
            "before-delete-keep-logs-from-the-last-days-threshold": 3664,
            "before-delete-run-script": False,
            "before-delete-run-script-command": "",
            "stop-logging-when-free-disk-space-below-metrics": "mbytes",
            "stop-logging-when-free-disk-space-below": False,
            "stop-logging-when-free-disk-space-below-threshold": 100,
            "delete-index-files-older-than-days": False,
            "delete-index-files-older-than-days-threshold": 14,
            "forward-logs-to-log-server": False,
            "update-account-log-every": 3600,
            "detect-new-citrix-ica-application-names": False,
            "turn-on-qos-logging": True,
            "enable-log-indexing": True,
            "smart-event-intro-correlation-unit": True,
            "accept-syslog-messages": False,
        },
    }


@pytest.fixture(name="resp_security_zone")
def fixture_resp_security_zone():
    return {
        "folder": {
            "uid": "a25a7783-9adb-4a65-9850-b97ee7860530",
            "name": "/Global Objects",
        },
        "domain": {
            "domain-type": "local domain",
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
        },
        "type": "security-zone",
        "name": "SZone1",
        "uid": "cecd7d2e-c5bb-40d2-bd34-7afe8c37a062",
    }


@pytest.fixture(name="resp_time")
def fixture_resp_time():
    return {
        "uid": "aa785d6d-7785-aad5-36a3-ab2d74c966ee",
        "name": "timeObject1",
        "start-now": True,
        "end": {"date": "24-Nov-2014", "time": "21:22"},
        "end-never": "false",
        "hours-ranges": [
            {"from": "00:00", "to": "00:00", "enabled": True, "index": 1},
            {"from": "00:00", "to": "00:00", "enabled": False, "index": 2},
        ],
        "recurrence": {
            "pattern": "Daily",
            "month": "Any",
            "weekdays": ["Sun", "Mon"],
            "days": ["1"],
        },
        "tags": [
            {
                "folder": {
                    "uid": "a25a7783-9adb-4a65-9850-b97ee7860530",
                    "name": "/Global Objects",
                },
                "domain": {
                    "domain-type": "local domain",
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                },
                "type": "tag",
                "name": "tag1",
                "uid": "687715ca-674b-4642-981b-b6243fde04c0",
            }
        ],
    }


@pytest.fixture(name="resp_time_group")
def fixture_resp_time_group():
    return {
        "uid": "d5878541-abbd-ad58-d23a-01a12352abc6",
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
        "tags": [
            {
                "folder": {
                    "uid": "a25a7783-9adb-4a65-9850-b97ee7860530",
                    "name": "/Global Objects",
                },
                "domain": {
                    "domain-type": "local domain",
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                },
                "type": "tag",
                "name": "tag1",
                "uid": "687715ca-674b-4642-981b-b6243fde04c0",
            }
        ],
        "name": "New Time Group",
        "comments": "",
        "color": "black",
        "icon": "General/group",
        "groups": [],
        "members": [],
    }


@pytest.fixture(name="resp_dynamic_object")
def fixture_resp_dynamic_object():
    return {
        "uid": "c5a7f50c-a951-45be-8b82-48441c9f48de",
        "name": "Dynamic_Object_1",
        "type": "dynamic-object",
        "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain",
        },
        "meta-info": {
            "lock": "unlocked",
            "validation-state": "ok",
            "last-modify-time": {
                "posix": 1478597722485,
                "iso-8601": "2016-11-08T11:35+0200",
            },
            "last-modifier": "aa",
            "creation-time": {
                "posix": 1478597722485,
                "iso-8601": "2016-11-08T11:35+0200",
            },
            "creator": "aa",
        },
        "tags": [
            {
                "folder": {
                    "uid": "a25a7783-9adb-4a65-9850-b97ee7860530",
                    "name": "/Global Objects",
                },
                "domain": {
                    "domain-type": "local domain",
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                },
                "type": "tag",
                "name": "tag1",
                "uid": "687715ca-674b-4642-981b-b6243fde04c0",
            }
        ],
        "read-only": True,
        "comments": "My Dynamic Object 1",
        "color": "yellow",
        "icon": "NetworkObjects/dynamicObject",
    }


@pytest.fixture(name="resp_tag")
def fixture_resp_tag():
    return {
        "uid": "728a4212-a521-46a2-a5a1-b6536a9aecd5",
        "folder": {
            "uid": "a25a7783-9adb-4a65-9850-b97ee7860530",
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
                "posix": 1432132584715,
                "iso-8601": "2015-05-20T17:36+0300",
            },
            "last-modifier": "aa",
            "creation-time": {
                "posix": 1432132584715,
                "iso-8601": "2015-05-20T17:36+0300",
            },
            "creator": "aa",
        },
        "tags": [
            {
                "folder": {
                    "uid": "a25a7783-9adb-4a65-9850-b97ee7860530",
                    "name": "/Global Objects",
                },
                "domain": {
                    "domain-type": "local domain",
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                },
                "type": "tag",
                "name": "tag1",
                "uid": "687715ca-674b-4642-981b-b6243fde04c0",
            },
            {
                "folder": {
                    "uid": "a25a7783-9adb-4a65-9850-b97ee7860530",
                    "name": "/Global Objects",
                },
                "domain": {
                    "domain-type": "local domain",
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                },
                "type": "tag",
                "name": "tag2",
                "uid": "f1ee4a33-6577-45da-9d4f-cc352a349c80",
            },
        ],
        "name": "My New Tag1",
        "comments": "",
        "color": "black",
        "icon": "General/globalsNa",
    }


@pytest.fixture(name="resp_dns_domain")
def fixture_resp_dns_domain():
    return {
        "uid": "ea6b168b-87d8-4ab6-9a8c-89c422dbde88",
        "name": ".www.example.com",
        "type": "dns-domain",
        "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain",
        },
        "meta-info": {
            "lock": "unlocked",
            "validation-state": "ok",
            "last-modify-time": {
                "posix": 1478675596098,
                "iso-8601": "2016-11-09T09:13+0200",
            },
            "last-modifier": "aa",
            "creation-time": {
                "posix": 1478675596098,
                "iso-8601": "2016-11-09T09:13+0200",
            },
            "creator": "aa",
        },
        "tags": [
            {
                "folder": {
                    "uid": "a25a7783-9adb-4a65-9850-b97ee7860530",
                    "name": "/Global Objects",
                },
                "domain": {
                    "domain-type": "local domain",
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                },
                "type": "tag",
                "name": "tag1",
                "uid": "687715ca-674b-4642-981b-b6243fde04c0",
            }
        ],
        "read-only": True,
        "comments": "",
        "color": "black",
        "icon": "Objects/domain",
        "is-sub-domain": False,
    }


@pytest.fixture(name="resp_opsec_application")
def fixture_resp_opsec_application():
    return {
        "uid": "1741bb6c-3b19-456c-a635-b96c8456a0e8",
        "name": "MyOpsecApplication",
        "type": "opsec-application",
        "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain",
        },
        "host": "SomeHost",
        "meta-info": {
            "lock": "unlocked",
            "validation-state": "ok",
            "last-modify-time": {
                "posix": 1481003908596,
                "iso-8601": "2016-12-06T07:58+0200",
            },
            "last-modifier": "aa",
            "creation-time": {
                "posix": 1481003908596,
                "iso-8601": "2016-12-06T07:58+0200",
            },
            "creator": "aa",
        },
        "tags": [
            {
                "folder": {
                    "uid": "a25a7783-9adb-4a65-9850-b97ee7860530",
                    "name": "/Global Objects",
                },
                "domain": {
                    "domain-type": "local domain",
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                },
                "type": "tag",
                "name": "tag1",
                "uid": "687715ca-674b-4642-981b-b6243fde04c0",
            }
        ],
        "read-only": True,
        "comments": "",
        "color": "black",
        "icon": "OPSECapplications/OPSEC",
        "cpmi": {
            "use-administrator-credentials": False,
            "administrator-profile": "super user",
        },
    }


@pytest.fixture(name="resp_lsv_profile")
def fixture_resp_lsv_profile():
    return {
        "uid": "160de00a-c8b8-4cb4-ae4b-8623d0e6f8b6",
        "name": "New lsv-profile",
        "type": "lsv-profile",
        "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain",
        },
        "meta-info": {
            "lock": "unlocked",
            "validation-state": "ok",
            "last-modify-time": {
                "posix": 1562087584480,
                "iso-8601": "2019-07-02T20:13+0300",
            },
            "last-modifier": "aa",
            "creation-time": {
                "posix": 1562087584480,
                "iso-8601": "2019-07-02T20:13+0300",
            },
            "creator": "aa",
        },
        "tags": [
            {
                "folder": {
                    "uid": "a25a7783-9adb-4a65-9850-b97ee7860530",
                    "name": "/Global Objects",
                },
                "domain": {
                    "domain-type": "local domain",
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                },
                "type": "tag",
                "name": "tag1",
                "uid": "687715ca-674b-4642-981b-b6243fde04c0",
            }
        ],
        "read-only": True,
        "comments": "",
        "color": "black",
        "icon": "Profiles/lsv_profile",
        "certificate-authority": "896977ae-64d3-e44f-945d-148def7383f7",
        "vpn-domain": {"limit-peer-domain-size": False, "max-allowed-addresses": 256},
        "allowed-ip-addresses": [],
        "restrict-allowed-addresses": False,
    }


@pytest.fixture(name="resp_tacacs_server")
def fixture_resp_tacacs_server():
    return {
        "uid": "c9d1de16-407a-42bc-a28d-3b9d7f933766",
        "name": "tacacs7",
        "type": "tacacs-server",
        "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain",
        },
        "meta-info": {
            "lock": "unlocked",
            "validation-state": "ok",
            "last-modify-time": {
                "posix": 1583675379149,
                "iso-8601": "2020-03-08T15:49+0200",
            },
            "last-modifier": "aa",
            "creation-time": {
                "posix": 1583675379149,
                "iso-8601": "2020-03-08T15:49+0200",
            },
            "creator": "aa",
        },
        "tags": [
            {
                "folder": {
                    "uid": "a25a7783-9adb-4a65-9850-b97ee7860530",
                    "name": "/Global Objects",
                },
                "domain": {
                    "domain-type": "local domain",
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                },
                "type": "tag",
                "name": "tag1",
                "uid": "687715ca-674b-4642-981b-b6243fde04c0",
            }
        ],
        "read-only": True,
        "comments": "",
        "color": "black",
        "icon": "Objects/account_unit",
        "groups": [],
        "server-type": "TACACS",
        "server": {"name": "h1", "uid": "eead9bf5-4640-432c-979b-5d7ae7a8bfb7"},
        "priority": 1,
    }


@pytest.fixture(name="resp_tacacs_group")
def fixture_resp_tacacs_group():
    return {
        "uid": "dd857ad5-a354-3991-cddc-58dc5ae69f65",
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
        "tags": [
            {
                "folder": {
                    "uid": "a25a7783-9adb-4a65-9850-b97ee7860530",
                    "name": "/Global Objects",
                },
                "domain": {
                    "domain-type": "local domain",
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                },
                "type": "tag",
                "name": "tag1",
                "uid": "687715ca-674b-4642-981b-b6243fde04c0",
            }
        ],
        "name": "New TACACS Group 3",
        "comments": "",
        "color": "black",
        "icon": "General/group",
        "groups": [],
        "members": [
            {
                "uid": "c9d1de16-407a-42bc-a28d-3b9d7f933766",
                "name": "tacacs7",
                "type": "tacacs-server",
                "domain": {
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                    "domain-type": "domain",
                },
                "meta-info": {
                    "lock": "unlocked",
                    "validation-state": "ok",
                    "last-modify-time": {
                        "posix": 1583675379149,
                        "iso-8601": "2020-03-08T15:49+0200",
                    },
                    "last-modifier": "aa",
                    "creation-time": {
                        "posix": 1583675379149,
                        "iso-8601": "2020-03-08T15:49+0200",
                    },
                    "creator": "aa",
                },
                "tags": [
                    {
                        "folder": {
                            "uid": "a25a7783-9adb-4a65-9850-b97ee7860530",
                            "name": "/Global Objects",
                        },
                        "domain": {
                            "domain-type": "local domain",
                            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                            "name": "SMC User",
                        },
                        "type": "tag",
                        "name": "tag1",
                        "uid": "687715ca-674b-4642-981b-b6243fde04c0",
                    }
                ],
                "read-only": True,
                "comments": "",
                "color": "black",
                "icon": "Objects/account_unit",
                "groups": [],
                "server-type": "TACACS",
                "server": {"name": "h1", "uid": "eead9bf5-4640-432c-979b-5d7ae7a8bfb7"},
                "priority": 1,
            }
        ],
    }


@pytest.fixture(name="resp_access_point_name")
def fixture_resp_access_point_name():
    return {
        "uid": "5064644d-6cc7-4703-823c-54f01ab720e6",
        "name": "myaccesspointname",
        "type": "access-point-name",
        "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain",
        },
        "tags": [
            {
                "folder": {
                    "uid": "a25a7783-9adb-4a65-9850-b97ee7860530",
                    "name": "/Global Objects",
                },
                "domain": {
                    "domain-type": "local domain",
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                },
                "type": "tag",
                "name": "tag1",
                "uid": "687715ca-674b-4642-981b-b6243fde04c0",
            }
        ],
        "read-only": True,
        "comments": "",
        "color": "black",
        "icon": "NetworkObjects/AccessPointName",
        "groups": [],
        "apn": "apnname",
        "enforce-end-user-domain": True,
        "end-user-domain": {
            "uid": "b307ca15-2ee8-414a-b261-ac7fb7464736",
            "name": "All_Internet",
            "type": "address-range",
            "domain": {
                "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                "name": "SMC User",
                "domain-type": "domain",
            },
            "ipv4-address-first": "10.0.0.0",
            "ipv4-address-last": "255.255.255.255",
        },
        "block-traffic-other-end-user-domains": True,
        "block-traffic-this-end-user-domain": True,
    }


@pytest.fixture(name="resp_lsm_gateway")
def fixture_resp_lsm_gateway():
    return {
        "uid": "f3b6df08-d973-4f16-8cfb-1f9562c6d120",
        "name": "lsm_gateway",
        "type": "lsm-gateway",
        "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain",
        },
        "meta-info": {
            "lock": "unlocked",
            "validation-state": "ok",
            "last-modify-time": {
                "posix": 1607433843108,
                "iso-8601": "2020-12-08T15:24+0200",
            },
            "last-modifier": "System",
            "creation-time": {
                "posix": 1607433831474,
                "iso-8601": "2020-12-08T15:23+0200",
            },
            "creator": "aa",
        },
        "tags": [
            {
                "folder": {
                    "uid": "a25a7783-9adb-4a65-9850-b97ee7860530",
                    "name": "/Global Objects",
                },
                "domain": {
                    "domain-type": "local domain",
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                },
                "type": "tag",
                "name": "tag1",
                "uid": "687715ca-674b-4642-981b-b6243fde04c0",
            }
        ],
        "read-only": False,
        "comments": "",
        "color": "black",
        "icon": "NetworkObjects/ROBO/ROBO_CP",
        "security-profile": "lsm_profile",
        "sic-name": "CN=lsm_gateway,O=R81.10_API..wm5cer",
        "sic-state": "Initialized",
        "ip-address": "1.2.3.4",
        "version": "R81.10",
        "os-name": "Gaia",
        "provisioning-state": "using-profile",
        "provisioning-settings": {"provisioning-profile": "prv_profile"},
    }


@pytest.fixture(name="resp_lsm_cluster")
def fixture_resp_lsm_cluster():
    return {
        "uid": "d1c363bc-c4c6-4903-9426-495d800b47ae",
        "name": "Gaia_gaia_cluster",
        "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain",
        },
        "meta-info": {
            "lock": "unlocked",
            "validation-state": "ok",
            "last-modify-time": {
                "posix": 1608633933685,
                "iso-8601": "2020-12-22T12:45+0200",
            },
            "last-modifier": "System",
            "creation-time": {
                "posix": 1608633909531,
                "iso-8601": "2020-12-22T12:45+0200",
            },
            "creator": "aa",
        },
        "tags": [
            {
                "folder": {
                    "uid": "a25a7783-9adb-4a65-9850-b97ee7860530",
                    "name": "/Global Objects",
                },
                "domain": {
                    "domain-type": "local domain",
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                },
                "type": "tag",
                "name": "tag1",
                "uid": "687715ca-674b-4642-981b-b6243fde04c0",
            }
        ],
        "read-only": False,
        "comments": "this object was created via API",
        "color": "black",
        "icon": "NetworkObjects/ROBO/ROBO_CLUSTER",
        "security-profile": "gaia_cluster",
        "main-ip-address": "192.168.68.197",
        "version": "R81.10",
        "os-name": "Gaia",
        "members": [
            {
                "member-uid": "6c015875-6776-4066-8735-9c4f43e3787d",
                "member-name": "Gaia_gw1",
                "sic-name": "CN=Gaia_gw1,O=R81.10_API..wm5cer",
                "sic-state": "Initialized",
                "main-ip-address": "192.168.8.200",
                "interfaces": [
                    {"name": "WAN", "ip-address": "192.168.8.200"},
                    {"name": "LAN1", "ip-address": "10.8.197.200"},
                ],
            },
            {
                "member-uid": "6e648bd7-c686-46db-a0f1-0d1d794f4ea9",
                "member-name": "Gaia_gw2",
                "sic-name": "CN=Gaia_gw2,O=R81.10_API_Cluster..wm5cer",
                "sic-state": "Initialized",
                "main-ip-address": "192.168.8.202",
                "interfaces": [
                    {"name": "WAN", "ip-address": "192.168.8.202"},
                    {"name": "LAN1", "ip-address": "10.8.197.202"},
                ],
            },
        ],
        "interfaces": [
            {
                "name": "WAN",
                "member-network-override": "192.168.68.0",
                "cluster-ip-address-override": "192.168.68.197",
            },
            {
                "name": "LAN1",
                "member-network-override": "10.8.197.0",
                "cluster-ip-address-override": "10.8.197.1",
            },
        ],
    }
