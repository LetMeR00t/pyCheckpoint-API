[![pyCheckpoint-API](https://raw.githubusercontent.com/LetMeR00t/pyCheckpoint-API/main/images/logo.png)](https://github.com/LetMeR00t/pyCheckpoint-API)
# pyCheckpoint-API - An unofficial Python SDK for Checkpoint Firewalls API

[![PyPI Version](https://img.shields.io/pypi/v/pycheckpoint-api.svg)](https://pypi.org/project/pyCheckpoint-API)
[![GitHub Release](https://img.shields.io/github/release/LetMeR00t/pyCheckpoint-API.svg)](https://github.com/LetMeR00t/pyCheckpoint-API/releases/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/pycheckpoint-api.svg)](https://pypi.python.org/pypi/pycheckpoint-api/)
[![Documentation Status](https://readthedocs.org/projects/pycheckpoint-api/badge/?version=latest)](https://pycheckpoint-api.readthedocs.io/?badge=latest)
[![Build Status](https://github.com/LetMeR00t/pyCheckpoint-API/actions/workflows/build_by_version.yml/badge.svg)](https://github.com/LetMeR00t/pyCheckpoint-API/actions/workflows/build_by_version.yml)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/352850b074e74a6890a2412c85b738c0)](https://www.codacy.com/gh/LetMeR00t/pyCheckpoint-API/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=LetMeR00t/pyCheckpoint-API&amp;utm_campaign=Badge_Grade)
[![codecov](https://codecov.io/gh/LetMeR00t/pyCheckpoint-API/branch/main/graph/badge.svg?token=0A583STZI7)](https://codecov.io/gh/LetMeR00t/pyCheckpoint-API)
[![License](https://img.shields.io/github/license/LetMeR00t/pyCheckpoint-API.svg)](https://github.com/LetMeR00t/pyCheckpoint-API)

pyCheckpoint-API is an SDK that provides a uniform and easy-to-use interface for each of the Checkpoint Firewall product API versions.

This SDK is not affiliated with, nor supported by Checkpoint in any way.

## Overview
Checkpoint firewalls solution are now using a well detailed API. This SDK simplifies software development using the Checkpoint Firewall API in Python.

This SDK is based on the [Checkpoint official API documentation](https://sc1.checkpoint.com/documents/latest/APIs/#introduction~v1.8%20).

This SDK leverages the [RESTfly framework](https://restfly.readthedocs.io/en/latest/index.html) developed by Steve McGrath.

This SDK implementation was largely inspired from the [pyZscaler](https://github.com/mitchos/pyZscaler) SDK development.


## Features
- Simplified authentication with Checkpoint API versions.
- Uniform interaction with the Checkpoint API versions.
- Uses [python-box](https://github.com/cdgriffith/Box/wiki) to add dot notation access to json data structures.
- Various quality of life enhancements for object CRUD methods.

## Products
- [Checkpoint](https://www.checkpoint.com/) Firewall

## Installation

The most recent version can be installed from pypi as per below.

    $ pip install pycheckpoint-api

## Usage

Before you can interact with the Checkpoint API, you may need to generate API keys directly in the management interface or use a classic username/password at each connection.

Once you have the requirements and you have installed pyCheckpoint-API, you're ready to go.

### Quick Examples

#### API login/logout
```python
from pycheckpoint_api.firewallManagement import FirewallManagementAPI
from pprint import pprint

# Please note that, as it's an example, we enabled the SSL verify to False to avoid having SSL certificate issues.
# However, it's highly recommanded to use certificates with know certificate authorities.
# If you want to use an API key instead, remove the 'user' and 'password' fields and use the 'api_key' field.
with FirewallManagementAPI(
    hostname='HOSTNAME',
    port='PORT',
    user='USER',
    password='PASSWORD',
    version='VERSION',
    domain='DOMAIN',
    ssl_verify=False,
) as api:

    pprint(
        "Connection is successfull, we have a token: "
        + api._session.headers["X-chkp-sid"]
    )

# Since we are out of the previous block, the API has been disconnected
pprint("Logout is successfull")
```

## Documentation
### Web API Coverage
Legend: 
* 🟢 means "Fully covered"
* 🟡 means "Partially covered"
* 🔴 means "Not covered yet"

Here is the list of endpoints that are currently supported by this SDK and base on the [Checkpoint official API reference](https://sc1.checkpoint.com/documents/latest/APIs/#introduction~v1.8%20).:
* 🟢 Session Management
* 🟢 Network Objects
* 🔴 Compliance
* 🔴 Gaia Best Practice
* 🔴 Data Center
* 🔴 Azure Active Directory
* 🔴 Updatable Objects
* 🟡 Service & Applications
  * 🟢 Service TCP
  * 🟢 Service UDP
  * 🟢 Service ICMP
  * 🟢 Service ICMP6
  * 🟢 Service SCTP
  * 🟢 Service Other
  * 🟢 Service Group
  * 🔴 Application
  * 🔴 Application Category
  * 🔴 Application Group
  * 🔴 Service DCE-RPC
  * 🔴 Service RPC
  * 🔴 Service GTP
  * 🔴 Service Citrix TCP
  * 🔴 Service Compound TCP
* 🔴 Access Control & NAT
* 🔴 VPN
* 🔴 VSX
* 🔴 Threat Prevention
* 🔴 HTTPS Inspection
* 🔴 Policy
* 🔴 Multi-Domain
* 🔴 Migration
* 🔴 SmartTasks
* 🔴 Package Deployment
* 🔴 Users
* 🔴 High Availability
* 🔴 Manage & Settings
* 🔴 Logs
* 🔴 Misc.

### API Documentation
TODO

### User Documentation
TODO

## Is It Tested?
Yes! pyCheckpoint-API has a complete test suite that fully covers all implemented methods

## Contributing

Contributions to pyCheckpoint-API are absolutely welcome.

Please see the [Contribution Guidelines](https://github.com/LetMeR00t/pyCheckpoint-API/blob/main/CONTRIBUTING.md) for more information.

[Poetry](https://python-poetry.org/docs/) is currently being used for builds and management. You'll want to have poetry installed and available in your environment.

Once Poetry is installed, you can create and validate your development environment using those commands:

    $ poetry install
    ...
    $ poetry build
    ...
    $ poetry shell
    ...
    $ pytest

You should then see the output of pytest results with all tests passed.

## Issues
Please feel free to open an issue using [Github Issues](https://github.com/LetMeR00t/pyCheckpoint-API/issues) if you run into any problems using pyCheckpoint-API.

## License
MIT License

Copyright (c) 2022 LmR

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
