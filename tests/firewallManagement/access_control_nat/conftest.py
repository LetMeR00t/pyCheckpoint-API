import pytest


@pytest.fixture(name="resp_access_rule")
def fixture_resp_access_rule():
    return {
        "uid": "1df8a4b0-fa8b-428b-b649-626b74bf7f81",
        "name": "Rule 1",
        "type": "access-rule",
        "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain",
        },
        "enabled": True,
        "comments": "",
        "meta-info": {
            "lock": "locked by current session",
            "validation-state": "ok",
            "last-modify-time": {
                "posix": 1482659046483,
                "iso-8601": "2016-12-25T11:44+0200",
            },
            "last-modifier": "aa",
            "creation-time": {
                "posix": 1482659046483,
                "iso-8601": "2016-12-25T11:44+0200",
            },
            "creator": "aa",
        },
        "install-on": [
            {
                "uid": "6c488338-8eec-4103-ad21-cd461ac2c476",
                "name": "Policy Targets",
                "type": "Global",
                "domain": {
                    "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                    "name": "Check Point Data",
                    "domain-type": "data domain",
                },
            }
        ],
        "source": [
            {
                "uid": "97aeb369-9aea-11d5-bd16-0090272ccb30",
                "name": "Any",
                "type": "CpmiAnyObject",
                "domain": {
                    "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                    "name": "Check Point Data",
                    "domain-type": "data domain",
                },
            }
        ],
        "source-negate": False,
        "destination": [
            {
                "uid": "97aeb369-9aea-11d5-bd16-0090272ccb30",
                "name": "Any",
                "type": "CpmiAnyObject",
                "domain": {
                    "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                    "name": "Check Point Data",
                    "domain-type": "data domain",
                },
            }
        ],
        "destination-negate": False,
        "service": [
            {
                "uid": "97aeb3d9-9aea-11d5-bd16-0090272ccb30",
                "name": "smtp",
                "type": "service-tcp",
                "domain": {
                    "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                    "name": "Check Point Data",
                    "domain-type": "data domain",
                },
                "port": "25",
            },
            {
                "uid": "97aeb44f-9aea-11d5-bd16-0090272ccb30",
                "name": "AOL",
                "type": "service-tcp",
                "domain": {
                    "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                    "name": "Check Point Data",
                    "domain-type": "data domain",
                },
                "port": "5190",
            },
        ],
        "service-negate": False,
        "vpn": [
            {
                "uid": "8fcd975f-33b1-4322-b033-6fb251554d45",
                "name": "MyIntranet",
                "type": "vpn-community-meshed",
                "domain": {
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                    "domain-type": "domain",
                },
            }
        ],
        "action": {
            "uid": "6c488338-8eec-4103-ad21-cd461ac2c473",
            "name": "Drop",
            "type": "RulebaseAction",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain",
            },
        },
        "action-settings": {"enable-identity-captive-portal": False},
        "content": [
            {
                "uid": "97aeb369-9aea-11d5-bd16-0090272ccb30",
                "name": "Any",
                "type": "CpmiAnyObject",
                "domain": {
                    "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                    "name": "Check Point Data",
                    "domain-type": "data domain",
                },
            }
        ],
        "content-negate": False,
        "content-direction": "any",
        "track": {
            "uid": "29e53e3d-23bf-48fe-b6b1-d59bd88036f9",
            "name": "None",
            "type": "Track",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain",
            },
        },
        "track-alert": "none",
        "time": [
            {
                "uid": "97aeb369-9aea-11d5-bd16-0090272ccb30",
                "name": "Any",
                "type": "CpmiAnyObject",
                "domain": {
                    "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                    "name": "Check Point Data",
                    "domain-type": "data domain",
                },
            }
        ],
        "custom-fields": {"field-1": "", "field-2": "", "field-3": ""},
    }


@pytest.fixture(name="resp_access_rulebase")
def fixture_resp_access_rulebase():
    return {
        "from": 1,
        "to": 3,
        "total": 3,
        "name": "Network",
        "uid": "21127e7c-d19b-4c65-b9c3-8e20e66ea1ae",
        "rulebase": [
            {
                "from": 1,
                "to": 1,
                "rulebase": [
                    {
                        "uid": "cb20e1cc-0343-4e22-a6bb-30b92e97675c",
                        "enabled": True,
                        "comments": "",
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
                                "posix": 1445504073840,
                                "iso-8601": "2015-10-22T11:54+0300",
                            },
                            "last-modifier": "aa",
                            "creation-time": {
                                "posix": 1445245489542,
                                "iso-8601": "2015-10-19T12:04+0300",
                            },
                            "creator": "aa",
                        },
                        "install-on": [
                            {
                                "domainId": {
                                    "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                                    "name": "Check Point Data",
                                    "type": "data domain",
                                },
                                "color": "none",
                                "xmlType": "Global",
                                "uid": "6c488338-8eec-4103-ad21-cd461ac2c476",
                                "folder": {
                                    "uid": "a7a569db-cd04-4f1c-bc8d-94dbfc22b150",
                                    "name": "Check Point Settings",
                                },
                                "meta-info": {
                                    "validation-state": "ok",
                                    "last-modify-time": {
                                        "posix": 1444711969368,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "last-modifier": "System",
                                    "creation-time": {
                                        "posix": 1444711969368,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "creator": "System",
                                },
                                "tags": [],
                                "name": "Policy Targets",
                                "icon": "General/globalsAny",
                                "comments": "The policy target gateways",
                            }
                        ],
                        "name": "Rule1",
                        "source": [
                            {
                                "domainId": {
                                    "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                                    "name": "Check Point Data",
                                    "type": "data domain",
                                },
                                "color": "red",
                                "xmlType": "dynamic-object",
                                "uid": "fe9b9103-f1c0-499e-985a-d15ccc7ebaab",
                                "folder": {
                                    "uid": "a3a104fc-3987-4d22-9bf1-3fdbec0af39b",
                                    "name": "Global Objects",
                                },
                                "meta-info": {
                                    "validation-state": "ok",
                                    "last-modify-time": {
                                        "posix": 1444711955857,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "last-modifier": "System",
                                    "creation-time": {
                                        "posix": 1444711955857,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "creator": "System",
                                },
                                "tags": [],
                                "name": "CPDShield",
                                "icon": "NetworkObjects/dynamicObject",
                                "comments": "DSHIELD IP blocklist",
                                "display-name": "",
                            }
                        ],
                        "source-negate": False,
                        "destination": [
                            {
                                "domainId": {
                                    "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                                    "name": "Check Point Data",
                                    "type": "data domain",
                                },
                                "color": "black",
                                "xmlType": "CpmiAnyObject",
                                "uid": "97aeb369-9aea-11d5-bd16-0090272ccb30",
                                "folder": {
                                    "uid": "a3a104fc-3987-4d22-9bf1-3fdbec0af39b",
                                    "name": "Global Objects",
                                },
                                "meta-info": {
                                    "validation-state": "ok",
                                    "last-modify-time": {
                                        "posix": 1444711951589,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "last-modifier": "System",
                                    "creation-time": {
                                        "posix": 1444711951589,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "creator": "System",
                                },
                                "tags": [],
                                "name": "Any",
                                "icon": "General/globalsAny",
                                "display-name": "",
                            }
                        ],
                        "destination-negate": False,
                        "service": [
                            {
                                "domainId": {
                                    "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                                    "name": "Check Point Data",
                                    "type": "data domain",
                                },
                                "color": "black",
                                "xmlType": "CpmiAnyObject",
                                "uid": "97aeb369-9aea-11d5-bd16-0090272ccb30",
                                "folder": {
                                    "uid": "a3a104fc-3987-4d22-9bf1-3fdbec0af39b",
                                    "name": "Global Objects",
                                },
                                "meta-info": {
                                    "validation-state": "ok",
                                    "last-modify-time": {
                                        "posix": 1444711951589,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "last-modifier": "System",
                                    "creation-time": {
                                        "posix": 1444711951589,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "creator": "System",
                                },
                                "tags": [],
                                "name": "Any",
                                "icon": "General/globalsAny",
                                "display-name": "",
                            }
                        ],
                        "service-negate": False,
                        "vpn": [
                            {
                                "domainId": {
                                    "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                                    "name": "Check Point Data",
                                    "type": "data domain",
                                },
                                "color": "black",
                                "xmlType": "CpmiAnyObject",
                                "uid": "97aeb369-9aea-11d5-bd16-0090272ccb30",
                                "folder": {
                                    "uid": "a3a104fc-3987-4d22-9bf1-3fdbec0af39b",
                                    "name": "Global Objects",
                                },
                                "meta-info": {
                                    "validation-state": "ok",
                                    "last-modify-time": {
                                        "posix": 1444711951589,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "last-modifier": "System",
                                    "creation-time": {
                                        "posix": 1444711951589,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "creator": "System",
                                },
                                "tags": [],
                                "name": "Any",
                                "icon": "General/globalsAny",
                                "display-name": "",
                            }
                        ],
                        "action": {
                            "domainId": {
                                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                                "name": "Check Point Data",
                                "type": "data domain",
                            },
                            "color": "none",
                            "xmlType": "RulebaseAction",
                            "uid": "6c488338-8eec-4103-ad21-cd461ac2c473",
                            "folder": {
                                "uid": "a7a569db-cd04-4f1c-bc8d-94dbfc22b150",
                                "name": "Check Point Settings",
                            },
                            "meta-info": {
                                "validation-state": "ok",
                                "last-modify-time": {
                                    "posix": 1444711969650,
                                    "iso-8601": "2015-10-13T07:52+0300",
                                },
                                "last-modifier": "System",
                                "creation-time": {
                                    "posix": 1444711969650,
                                    "iso-8601": "2015-10-13T07:52+0300",
                                },
                                "creator": "System",
                            },
                            "tags": [],
                            "name": "Drop",
                            "icon": "Actions/actionsDrop",
                            "comments": "Drop",
                            "display-name": "Drop",
                        },
                        "action-settings": {"enable-identity-captive-portal": False},
                        "data": [
                            {
                                "domainId": {
                                    "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                                    "name": "Check Point Data",
                                    "type": "data domain",
                                },
                                "color": "black",
                                "xmlType": "CpmiAnyObject",
                                "uid": "97aeb369-9aea-11d5-bd16-0090272ccb30",
                                "folder": {
                                    "uid": "a3a104fc-3987-4d22-9bf1-3fdbec0af39b",
                                    "name": "Global Objects",
                                },
                                "meta-info": {
                                    "validation-state": "ok",
                                    "last-modify-time": {
                                        "posix": 1444711951589,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "last-modifier": "System",
                                    "creation-time": {
                                        "posix": 1444711951589,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "creator": "System",
                                },
                                "tags": [],
                                "name": "Any",
                                "icon": "General/globalsAny",
                                "display-name": "",
                            }
                        ],
                        "data-negate": False,
                        "data-direction": "any",
                        "track": {
                            "domainId": {
                                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                                "name": "Check Point Data",
                                "type": "data domain",
                            },
                            "color": "none",
                            "xmlType": "Track",
                            "uid": "29e53e3d-23bf-48fe-b6b1-d59bd88036f9",
                            "folder": {
                                "uid": "a7a569db-cd04-4f1c-bc8d-94dbfc22b150",
                                "name": "Check Point Settings",
                            },
                            "meta-info": {
                                "validation-state": "ok",
                                "last-modify-time": {
                                    "posix": 1444711969451,
                                    "iso-8601": "2015-10-13T07:52+0300",
                                },
                                "last-modifier": "System",
                                "creation-time": {
                                    "posix": 1444711969451,
                                    "iso-8601": "2015-10-13T07:52+0300",
                                },
                                "creator": "System",
                            },
                            "tags": [],
                            "name": "None",
                            "icon": "General/globalsNone",
                            "comments": "Extended Log used in Application Site rulebase",
                        },
                        "track-alert": "none",
                        "time": [
                            {
                                "domainId": {
                                    "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                                    "name": "Check Point Data",
                                    "type": "data domain",
                                },
                                "color": "black",
                                "xmlType": "CpmiAnyObject",
                                "uid": "97aeb369-9aea-11d5-bd16-0090272ccb30",
                                "folder": {
                                    "uid": "a3a104fc-3987-4d22-9bf1-3fdbec0af39b",
                                    "name": "Global Objects",
                                },
                                "meta-info": {
                                    "validation-state": "ok",
                                    "last-modify-time": {
                                        "posix": 1444711951589,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "last-modifier": "System",
                                    "creation-time": {
                                        "posix": 1444711951589,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "creator": "System",
                                },
                                "tags": [],
                                "name": "Any",
                                "icon": "General/globalsAny",
                                "display-name": "",
                            }
                        ],
                        "custom-fields": {"field-1": "", "field-2": "", "field-3": ""},
                        "rule-number": 1,
                        "type": "rule",
                    }
                ],
                "name": "Section1",
                "uid": "c53d4aac-6c1b-4c75-aea2-3105612c302c",
                "type": "section",
            },
            {
                "from": 2,
                "to": 3,
                "rulebase": [
                    {
                        "uid": "ae36ddad-4a82-456b-93aa-a97320ff47df",
                        "enabled": True,
                        "comments": "",
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
                                "posix": 1445504129222,
                                "iso-8601": "2015-10-22T11:55+0300",
                            },
                            "last-modifier": "aa",
                            "creation-time": {
                                "posix": 1445504082424,
                                "iso-8601": "2015-10-22T11:54+0300",
                            },
                            "creator": "aa",
                        },
                        "install-on": [
                            {
                                "domainId": {
                                    "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                                    "name": "Check Point Data",
                                    "type": "data domain",
                                },
                                "color": "none",
                                "xmlType": "Global",
                                "uid": "6c488338-8eec-4103-ad21-cd461ac2c476",
                                "folder": {
                                    "uid": "a7a569db-cd04-4f1c-bc8d-94dbfc22b150",
                                    "name": "Check Point Settings",
                                },
                                "meta-info": {
                                    "validation-state": "ok",
                                    "last-modify-time": {
                                        "posix": 1444711969368,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "last-modifier": "System",
                                    "creation-time": {
                                        "posix": 1444711969368,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "creator": "System",
                                },
                                "tags": [],
                                "name": "Policy Targets",
                                "icon": "General/globalsAny",
                                "comments": "The policy target gateways",
                            }
                        ],
                        "name": "Rule2",
                        "source": [
                            {
                                "domainId": {
                                    "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                                    "name": "Check Point Data",
                                    "type": "data domain",
                                },
                                "color": "black",
                                "xmlType": "CpmiAnyObject",
                                "uid": "97aeb369-9aea-11d5-bd16-0090272ccb30",
                                "folder": {
                                    "uid": "a3a104fc-3987-4d22-9bf1-3fdbec0af39b",
                                    "name": "Global Objects",
                                },
                                "meta-info": {
                                    "validation-state": "ok",
                                    "last-modify-time": {
                                        "posix": 1444711951589,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "last-modifier": "System",
                                    "creation-time": {
                                        "posix": 1444711951589,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "creator": "System",
                                },
                                "tags": [],
                                "name": "Any",
                                "icon": "General/globalsAny",
                                "display-name": "",
                            }
                        ],
                        "source-negate": False,
                        "destination": [
                            {
                                "domainId": {
                                    "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                                    "name": "Check Point Data",
                                    "type": "data domain",
                                },
                                "color": "red",
                                "xmlType": "dynamic-object",
                                "uid": "fe9b9103-f1c0-499e-985a-d15ccc7ebaab",
                                "folder": {
                                    "uid": "a3a104fc-3987-4d22-9bf1-3fdbec0af39b",
                                    "name": "Global Objects",
                                },
                                "meta-info": {
                                    "validation-state": "ok",
                                    "last-modify-time": {
                                        "posix": 1444711955857,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "last-modifier": "System",
                                    "creation-time": {
                                        "posix": 1444711955857,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "creator": "System",
                                },
                                "tags": [],
                                "name": "CPDShield",
                                "icon": "NetworkObjects/dynamicObject",
                                "comments": "DSHIELD IP blocklist",
                                "display-name": "",
                            }
                        ],
                        "destination-negate": False,
                        "service": [
                            {
                                "domainId": {
                                    "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                                    "name": "Check Point Data",
                                    "type": "data domain",
                                },
                                "color": "black",
                                "xmlType": "CpmiAnyObject",
                                "uid": "97aeb369-9aea-11d5-bd16-0090272ccb30",
                                "folder": {
                                    "uid": "a3a104fc-3987-4d22-9bf1-3fdbec0af39b",
                                    "name": "Global Objects",
                                },
                                "meta-info": {
                                    "validation-state": "ok",
                                    "last-modify-time": {
                                        "posix": 1444711951589,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "last-modifier": "System",
                                    "creation-time": {
                                        "posix": 1444711951589,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "creator": "System",
                                },
                                "tags": [],
                                "name": "Any",
                                "icon": "General/globalsAny",
                                "display-name": "",
                            }
                        ],
                        "service-negate": False,
                        "vpn": [
                            {
                                "domainId": {
                                    "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                                    "name": "Check Point Data",
                                    "type": "data domain",
                                },
                                "color": "black",
                                "xmlType": "CpmiAnyObject",
                                "uid": "97aeb369-9aea-11d5-bd16-0090272ccb30",
                                "folder": {
                                    "uid": "a3a104fc-3987-4d22-9bf1-3fdbec0af39b",
                                    "name": "Global Objects",
                                },
                                "meta-info": {
                                    "validation-state": "ok",
                                    "last-modify-time": {
                                        "posix": 1444711951589,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "last-modifier": "System",
                                    "creation-time": {
                                        "posix": 1444711951589,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "creator": "System",
                                },
                                "tags": [],
                                "name": "Any",
                                "icon": "General/globalsAny",
                                "display-name": "",
                            }
                        ],
                        "action": {
                            "domainId": {
                                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                                "name": "Check Point Data",
                                "type": "data domain",
                            },
                            "color": "none",
                            "xmlType": "RulebaseAction",
                            "uid": "6c488338-8eec-4103-ad21-cd461ac2c473",
                            "folder": {
                                "uid": "a7a569db-cd04-4f1c-bc8d-94dbfc22b150",
                                "name": "Check Point Settings",
                            },
                            "meta-info": {
                                "validation-state": "ok",
                                "last-modify-time": {
                                    "posix": 1444711969650,
                                    "iso-8601": "2015-10-13T07:52+0300",
                                },
                                "last-modifier": "System",
                                "creation-time": {
                                    "posix": 1444711969650,
                                    "iso-8601": "2015-10-13T07:52+0300",
                                },
                                "creator": "System",
                            },
                            "tags": [],
                            "name": "Drop",
                            "icon": "Actions/actionsDrop",
                            "comments": "Drop",
                            "display-name": "Drop",
                        },
                        "action-settings": {"enable-identity-captive-portal": False},
                        "data": [
                            {
                                "domainId": {
                                    "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                                    "name": "Check Point Data",
                                    "type": "data domain",
                                },
                                "color": "black",
                                "xmlType": "CpmiAnyObject",
                                "uid": "97aeb369-9aea-11d5-bd16-0090272ccb30",
                                "folder": {
                                    "uid": "a3a104fc-3987-4d22-9bf1-3fdbec0af39b",
                                    "name": "Global Objects",
                                },
                                "meta-info": {
                                    "validation-state": "ok",
                                    "last-modify-time": {
                                        "posix": 1444711951589,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "last-modifier": "System",
                                    "creation-time": {
                                        "posix": 1444711951589,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "creator": "System",
                                },
                                "tags": [],
                                "name": "Any",
                                "icon": "General/globalsAny",
                                "display-name": "",
                            }
                        ],
                        "data-negate": False,
                        "data-direction": "any",
                        "track": {
                            "domainId": {
                                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                                "name": "Check Point Data",
                                "type": "data domain",
                            },
                            "color": "none",
                            "xmlType": "Track",
                            "uid": "29e53e3d-23bf-48fe-b6b1-d59bd88036f9",
                            "folder": {
                                "uid": "a7a569db-cd04-4f1c-bc8d-94dbfc22b150",
                                "name": "Check Point Settings",
                            },
                            "meta-info": {
                                "validation-state": "ok",
                                "last-modify-time": {
                                    "posix": 1444711969451,
                                    "iso-8601": "2015-10-13T07:52+0300",
                                },
                                "last-modifier": "System",
                                "creation-time": {
                                    "posix": 1444711969451,
                                    "iso-8601": "2015-10-13T07:52+0300",
                                },
                                "creator": "System",
                            },
                            "tags": [],
                            "name": "None",
                            "icon": "General/globalsNone",
                            "comments": "Extended Log used in Application Site rulebase",
                        },
                        "track-alert": "none",
                        "time": [
                            {
                                "domainId": {
                                    "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                                    "name": "Check Point Data",
                                    "type": "data domain",
                                },
                                "color": "black",
                                "xmlType": "CpmiAnyObject",
                                "uid": "97aeb369-9aea-11d5-bd16-0090272ccb30",
                                "folder": {
                                    "uid": "a3a104fc-3987-4d22-9bf1-3fdbec0af39b",
                                    "name": "Global Objects",
                                },
                                "meta-info": {
                                    "validation-state": "ok",
                                    "last-modify-time": {
                                        "posix": 1444711951589,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "last-modifier": "System",
                                    "creation-time": {
                                        "posix": 1444711951589,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "creator": "System",
                                },
                                "tags": [],
                                "name": "Any",
                                "icon": "General/globalsAny",
                                "display-name": "",
                            }
                        ],
                        "custom-fields": {"field-1": "", "field-2": "", "field-3": ""},
                        "rule-number": 2,
                        "type": "rule",
                    },
                    {
                        "uid": "88e09e3a-a935-4b33-94f4-1f62b2d8b78a",
                        "enabled": True,
                        "comments": "",
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
                                "posix": 1445504138184,
                                "iso-8601": "2015-10-22T11:55+0300",
                            },
                            "last-modifier": "aa",
                            "creation-time": {
                                "posix": 1445504082982,
                                "iso-8601": "2015-10-22T11:54+0300",
                            },
                            "creator": "aa",
                        },
                        "install-on": [
                            {
                                "domainId": {
                                    "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                                    "name": "Check Point Data",
                                    "type": "data domain",
                                },
                                "color": "none",
                                "xmlType": "Global",
                                "uid": "6c488338-8eec-4103-ad21-cd461ac2c476",
                                "folder": {
                                    "uid": "a7a569db-cd04-4f1c-bc8d-94dbfc22b150",
                                    "name": "Check Point Settings",
                                },
                                "meta-info": {
                                    "validation-state": "ok",
                                    "last-modify-time": {
                                        "posix": 1444711969368,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "last-modifier": "System",
                                    "creation-time": {
                                        "posix": 1444711969368,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "creator": "System",
                                },
                                "tags": [],
                                "name": "Policy Targets",
                                "icon": "General/globalsAny",
                                "comments": "The policy target gateways",
                            }
                        ],
                        "name": "Rule3",
                        "source": [
                            {
                                "domainId": {
                                    "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                                    "name": "Check Point Data",
                                    "type": "data domain",
                                },
                                "color": "black",
                                "xmlType": "security-zone",
                                "uid": "e8131db2-8388-42a5-924a-82de32db20f7",
                                "folder": {
                                    "uid": "a3a104fc-3987-4d22-9bf1-3fdbec0af39b",
                                    "name": "Global Objects",
                                },
                                "meta-info": {
                                    "validation-state": "ok",
                                    "last-modify-time": {
                                        "posix": 1444711955871,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "last-modifier": "System",
                                    "creation-time": {
                                        "posix": 1444711955871,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "creator": "System",
                                },
                                "tags": [],
                                "name": "InternalZone",
                                "icon": "NetworkObjects/zone",
                                "comments": "",
                                "display-name": "",
                            }
                        ],
                        "source-negate": False,
                        "destination": [
                            {
                                "domainId": {
                                    "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                                    "name": "Check Point Data",
                                    "type": "data domain",
                                },
                                "color": "black",
                                "xmlType": "dynamic-object",
                                "uid": "cac127fb-24f5-4079-9404-be5c00d11393",
                                "folder": {
                                    "uid": "a3a104fc-3987-4d22-9bf1-3fdbec0af39b",
                                    "name": "Global Objects",
                                },
                                "meta-info": {
                                    "validation-state": "ok",
                                    "last-modify-time": {
                                        "posix": 1444711955855,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "last-modifier": "System",
                                    "creation-time": {
                                        "posix": 1444711955855,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "creator": "System",
                                },
                                "tags": [],
                                "name": "AuxiliaryNet",
                                "icon": "NetworkObjects/dynamicObject",
                                "comments": "",
                                "display-name": "",
                            }
                        ],
                        "destination-negate": False,
                        "service": [
                            {
                                "domainId": {
                                    "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                                    "name": "Check Point Data",
                                    "type": "data domain",
                                },
                                "color": "black",
                                "xmlType": "CpmiAnyObject",
                                "uid": "97aeb369-9aea-11d5-bd16-0090272ccb30",
                                "folder": {
                                    "uid": "a3a104fc-3987-4d22-9bf1-3fdbec0af39b",
                                    "name": "Global Objects",
                                },
                                "meta-info": {
                                    "validation-state": "ok",
                                    "last-modify-time": {
                                        "posix": 1444711951589,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "last-modifier": "System",
                                    "creation-time": {
                                        "posix": 1444711951589,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "creator": "System",
                                },
                                "tags": [],
                                "name": "Any",
                                "icon": "General/globalsAny",
                                "display-name": "",
                            }
                        ],
                        "service-negate": False,
                        "vpn": [
                            {
                                "domainId": {
                                    "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                                    "name": "Check Point Data",
                                    "type": "data domain",
                                },
                                "color": "black",
                                "xmlType": "CpmiAnyObject",
                                "uid": "97aeb369-9aea-11d5-bd16-0090272ccb30",
                                "folder": {
                                    "uid": "a3a104fc-3987-4d22-9bf1-3fdbec0af39b",
                                    "name": "Global Objects",
                                },
                                "meta-info": {
                                    "validation-state": "ok",
                                    "last-modify-time": {
                                        "posix": 1444711951589,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "last-modifier": "System",
                                    "creation-time": {
                                        "posix": 1444711951589,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "creator": "System",
                                },
                                "tags": [],
                                "name": "Any",
                                "icon": "General/globalsAny",
                                "display-name": "",
                            }
                        ],
                        "action": {
                            "domainId": {
                                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                                "name": "Check Point Data",
                                "type": "data domain",
                            },
                            "color": "none",
                            "xmlType": "RulebaseAction",
                            "uid": "6c488338-8eec-4103-ad21-cd461ac2c473",
                            "folder": {
                                "uid": "a7a569db-cd04-4f1c-bc8d-94dbfc22b150",
                                "name": "Check Point Settings",
                            },
                            "meta-info": {
                                "validation-state": "ok",
                                "last-modify-time": {
                                    "posix": 1444711969650,
                                    "iso-8601": "2015-10-13T07:52+0300",
                                },
                                "last-modifier": "System",
                                "creation-time": {
                                    "posix": 1444711969650,
                                    "iso-8601": "2015-10-13T07:52+0300",
                                },
                                "creator": "System",
                            },
                            "tags": [],
                            "name": "Drop",
                            "icon": "Actions/actionsDrop",
                            "comments": "Drop",
                            "display-name": "Drop",
                        },
                        "action-settings": {"enable-identity-captive-portal": False},
                        "data": [
                            {
                                "domainId": {
                                    "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                                    "name": "Check Point Data",
                                    "type": "data domain",
                                },
                                "color": "black",
                                "xmlType": "CpmiAnyObject",
                                "uid": "97aeb369-9aea-11d5-bd16-0090272ccb30",
                                "folder": {
                                    "uid": "a3a104fc-3987-4d22-9bf1-3fdbec0af39b",
                                    "name": "Global Objects",
                                },
                                "meta-info": {
                                    "validation-state": "ok",
                                    "last-modify-time": {
                                        "posix": 1444711951589,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "last-modifier": "System",
                                    "creation-time": {
                                        "posix": 1444711951589,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "creator": "System",
                                },
                                "tags": [],
                                "name": "Any",
                                "icon": "General/globalsAny",
                                "display-name": "",
                            }
                        ],
                        "data-negate": False,
                        "data-direction": "any",
                        "track": {
                            "domainId": {
                                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                                "name": "Check Point Data",
                                "type": "data domain",
                            },
                            "color": "none",
                            "xmlType": "Track",
                            "uid": "29e53e3d-23bf-48fe-b6b1-d59bd88036f9",
                            "folder": {
                                "uid": "a7a569db-cd04-4f1c-bc8d-94dbfc22b150",
                                "name": "Check Point Settings",
                            },
                            "meta-info": {
                                "validation-state": "ok",
                                "last-modify-time": {
                                    "posix": 1444711969451,
                                    "iso-8601": "2015-10-13T07:52+0300",
                                },
                                "last-modifier": "System",
                                "creation-time": {
                                    "posix": 1444711969451,
                                    "iso-8601": "2015-10-13T07:52+0300",
                                },
                                "creator": "System",
                            },
                            "tags": [],
                            "name": "None",
                            "icon": "General/globalsNone",
                            "comments": "Extended Log used in Application Site rulebase",
                        },
                        "track-alert": "none",
                        "time": [
                            {
                                "domainId": {
                                    "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                                    "name": "Check Point Data",
                                    "type": "data domain",
                                },
                                "color": "black",
                                "xmlType": "CpmiAnyObject",
                                "uid": "97aeb369-9aea-11d5-bd16-0090272ccb30",
                                "folder": {
                                    "uid": "a3a104fc-3987-4d22-9bf1-3fdbec0af39b",
                                    "name": "Global Objects",
                                },
                                "meta-info": {
                                    "validation-state": "ok",
                                    "last-modify-time": {
                                        "posix": 1444711951589,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "last-modifier": "System",
                                    "creation-time": {
                                        "posix": 1444711951589,
                                        "iso-8601": "2015-10-13T07:52+0300",
                                    },
                                    "creator": "System",
                                },
                                "tags": [],
                                "name": "Any",
                                "icon": "General/globalsAny",
                                "display-name": "",
                            }
                        ],
                        "custom-fields": {"field-1": "", "field-2": "", "field-3": ""},
                        "rule-number": 3,
                        "type": "rule",
                    },
                ],
                "name": "Seciton2",
                "uid": "58a00921-65a7-4258-9182-2340a203e4ee",
                "type": "section",
            },
        ],
    }


@pytest.fixture(name="resp_access_section")
def fixture_resp_access_section():
    return {
        "uid": "aa5d88e9-a589-abba-1471-5d6988519a26",
        "name": "New Section 1",
        "type": "access-section",
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
        "read-only": False,
    }


@pytest.fixture(name="resp_access_layer")
def fixture_resp_access_layer():
    return {
        "uid": "81530aad-bc98-4e8f-a62d-079424ddd955",
        "folder": {
            "uid": "3b1764a5-363a-4f63-a2ab-2ef90746c70c",
            "name": "/Global Objects",
        },
        "domain": {
            "domain-type": "local domain",
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
        },
        "meta-info": {
            "lock": "locked by current session",
            "validation-state": "ok",
            "read-only": False,
            "last-modify-time": {
                "posix": 1435737909731,
                "iso-8601": "2015-07-01T11:05+0300",
            },
            "last-modifier": "aa",
            "creation-time": {
                "posix": 1435737908063,
                "iso-8601": "2015-07-01T11:05+0300",
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
        "name": "New Layer 1",
        "comments": "",
        "color": "black",
        "icon": "ApplicationFirewall/rulebase",
        "applications-and-url-filtering": False,
        "content-awareness": False,
        "detect-using-x-forward-for": True,
        "firewall": True,
        "parent-layer": "",
        "mobile-access": False,
        "show-parent-rule": True,
    }
