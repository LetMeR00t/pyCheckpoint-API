#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script is used to create a new host and add it to an existing group.
   The new host will be using the red color, with a comment "This host was created thanks to the API" and
   will have two tags named "test1" and "test2"
"""

import logging
import time

import restfly

from pycheckpoint_api.firewallManagement import FirewallManagement
from pycheckpoint_api.models import Color

# Setup the logger configuration. If you have any trouble, turn the logging mode to logging.DEBUG
logging.basicConfig(
    filename="pycheckpoint_api-example-add-host-to-group.log",
    encoding="utf-8",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# GLOBAL VARIABLE
HOSTNAME = ""
PORT = 443
USER = ""
PASSWORD = ""
VERSION = "1.8"
DOMAIN = ""

# Initialize the API
api = None

try:
    # Please note that, as it's an example, we enabled the SSL verify to False to avoid having SSL certificate issues.
    # However, it's highly recommanded to use certificates with know certificate authorities.
    logger.info("Trying to login to the API...")

    with FirewallManagement(
        hostname=HOSTNAME,
        port=PORT,
        user=USER,
        password=PASSWORD,
        version=VERSION,
        domain=DOMAIN,
        ssl_verify=False,
    ) as firewall:

        # Start a timer
        start = time.time()

        # Ask for the host name
        INPUT_HOST_NAME = input("Enter the new host name: ")

        # Ask for the IPv4 information
        INPUT_IP = input("Enter the IPv4 address (x.x.x.x): ")

        # Ask for the group
        INPUT_GROUP = input(
            "Enter the name of the group in which you want to add this new host: "
        )

        # Execute the action
        logger.info("Trying to create the new host...")

        try:
            new_host = firewall.network_objects.host.add(
                name=INPUT_HOST_NAME,
                ip_address=INPUT_IP,
                groups=INPUT_GROUP,
                color=Color.RED,
                comments="This host was created thanks to the API",
                tags=["test1", "test2"],
            )

            logger.info("Host created successfully !")
        except Exception as e:
            logger.error("An error occured to create the new host.")

        # End timer
        timer = time.time() - start

        logger.info("-----------------------------------")
        logger.info(
            "Execution time: "
            + str(int(timer / 60))
            + "min "
            + str(round(timer % 60))
            + "s"
        )

except restfly.errors.BadRequestError as e:
    print(e)
    for p in dir(e.response.request):
        print(p, getattr(e.response.request, p))
