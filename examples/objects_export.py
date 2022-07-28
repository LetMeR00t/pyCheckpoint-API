#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script is used to export several objects using the Checkpoint Firewall API
   Only collection of data are performed
   We are not gathering all kind of objects but only hosts, networks, security zones, multicast address ranges,
   checkpoint hosts and service-tcp
"""

import logging
import time

import restfly

from pycheckpoint_api.management import Management

# Setup the logger configuration. If you have any trouble, turn the logging mode to logging.DEBUG
logging.basicConfig(
    filename="pycheckpoint_api-example-objects-export.log",
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

CHECKPOINT_LIMIT = 100

# Initialize the API
api = None

try:
    # Please note that, as it's an example, we enabled the SSL verify to False to avoid having SSL certificate issues.
    # However, it's highly recommanded to use certificates with know certificate authorities.
    logger.info("Trying to login to the API...")

    with Management(
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

        # Get access layers
        access_layers = []
        resp = firewall.access_control_nat.access_layer.show_access_layers()
        if resp.total > 0:
            als = resp.access_layers
            for al in als:
                logger.debug("PROCESS access layer: " + str(al.to_dict()))
                if al.domain.domain_type == "domain":
                    access_layers.append(al)
        logger.info(
            "Access layers recovered (only domain): "
            + str([al.name for al in access_layers])
        )

        # Get packages
        packages = []
        resp = firewall.policy.package.show_packages()
        if resp.total > 0:
            ps = resp.packages
            for p in ps:
                logger.debug("PROCESS package: " + str(p.to_dict()))
                packages.append(p)
        logger.info("Packages recovered: " + str([p.name for p in packages]))

        # Get all hosts
        hosts = firewall.network_objects.host.show_hosts(
            show_all=True, limit=CHECKPOINT_LIMIT
        ).objects
        logger.info("Hosts recovered: " + str(len(hosts)))
        # Get all networks
        networks = firewall.network_objects.network.show_networks(
            show_all=True, limit=CHECKPOINT_LIMIT
        ).objects
        logger.info("Networks recovered: " + str(len(networks)))
        # Get all security zones
        security_zones = firewall.network_objects.security_zone.show_security_zones(
            show_all=True, limit=CHECKPOINT_LIMIT
        ).objects
        logger.info("Security zones recovered: " + str(len(security_zones)))
        # Get all multicast address ranges
        multicast_address_ranges = firewall.network_objects.multicast_address_range.show_multicast_address_ranges(
            show_all=True, limit=CHECKPOINT_LIMIT
        ).objects
        logger.info(
            "Multicast address ranges recovered: " + str(len(multicast_address_ranges))
        )
        # Get all checkpoint hosts
        checkpoint_hosts = (
            firewall.network_objects.checkpoint_host.show_checkpoint_hosts(
                show_all=True, limit=CHECKPOINT_LIMIT
            ).objects
        )
        logger.info("Checkpoint hosts recovered: " + str(len(checkpoint_hosts)))
        # Get all access point names
        access_point_names = (
            firewall.network_objects.access_point_name.show_access_point_names(
                show_all=True, limit=CHECKPOINT_LIMIT
            ).objects
        )
        logger.info("Access point names recovered: " + str(len(access_point_names)))
        # Get all service-tcp
        services_tcp = firewall.service_applications.service_tcp.show_services_tcp(
            show_all=True, limit=CHECKPOINT_LIMIT
        ).objects
        logger.info("Service TCP recovered: " + str(len(services_tcp)))

        # Get all generic-objects
        generic_objects = firewall.misc.generic_objects.get_rulebaseactions().objects
        logger.info("Generic objects recovered: " + str(len(generic_objects)))

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
    logger.info(e)
    for p in dir(e.response.request):
        logger.debug(p, getattr(e.response.request, p))
