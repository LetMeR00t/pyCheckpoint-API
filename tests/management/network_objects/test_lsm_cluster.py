import pytest
import responses

from pycheckpoint_api.management.exception import MandatoryFieldMissing


@responses.activate
def test_add_lsm_cluster(management, resp_lsm_cluster):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-lsm-cluster",
        json=resp_lsm_cluster,
        status=200,
    )

    resp = management.network_objects.lsm_cluster.add(
        name_prefix="Gaia_",
        main_ip_address="192.168.8.197",
        security_profile="gaia_cluster",
        interfaces=[
            {
                "name": "eth0",
                "new-name": "WAN",
                "member-network-override": "192.168.8.0",
                "ip-address-override": "192.168.8.197",
            },
            {
                "name": "eth1",
                "new-name": "LAN1",
                "member-network-override": "10.8.197.0",
                "ip-address-override": "10.8.197.1",
            },
            {"name": "eth2", "member-network-override": "10.10.10.0"},
        ],
        members=[
            {
                "name": "Gaia_gw1",
                "sic": {"ip-address": "192.168.8.200", "one-time-password": "aaaa"},
            },
            {
                "name": "Gaia_gw2",
                "sic": {"ip-address": "192.168.8.202", "one-time-password": "aaaa"},
            },
        ],
        tags=["t1"],
    )

    assert resp.uid == "d1c363bc-c4c6-4903-9426-495d800b47ae"
    assert resp.name == "Gaia_gaia_cluster"

    resp = management.network_objects.lsm_cluster.add(
        name_suffix="_cluster",
        main_ip_address="192.168.8.197",
        security_profile="gaia_cluster",
        interfaces=[
            {
                "name": "eth0",
                "new-name": "WAN",
                "member-network-override": "192.168.8.0",
                "ip-address-override": "192.168.8.197",
            },
            {
                "name": "eth1",
                "new-name": "LAN1",
                "member-network-override": "10.8.197.0",
                "ip-address-override": "10.8.197.1",
            },
            {"name": "eth2", "member-network-override": "10.10.10.0"},
        ],
        members=[
            {
                "name": "Gaia_gw1",
                "sic": {"ip-address": "192.168.8.200", "one-time-password": "aaaa"},
            },
            {
                "name": "Gaia_gw2",
                "sic": {"ip-address": "192.168.8.202", "one-time-password": "aaaa"},
            },
        ],
        tags=["t1"],
    )

    assert resp.uid == "d1c363bc-c4c6-4903-9426-495d800b47ae"
    assert resp.name == "Gaia_gaia_cluster"

    # Missing name prefix or suffit
    with pytest.raises(MandatoryFieldMissing):
        management.network_objects.lsm_cluster.add(
            main_ip_address="192.168.8.197",
            security_profile="gaia_cluster",
        )


@responses.activate
def test_show_lsm_cluster(management, resp_lsm_cluster):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-lsm-cluster",
        json=resp_lsm_cluster,
        status=200,
    )

    resp = management.network_objects.lsm_cluster.show(
        uid="d1c363bc-c4c6-4903-9426-495d800b47ae"
    )

    assert resp.uid == "d1c363bc-c4c6-4903-9426-495d800b47ae"
    assert resp.name == "Gaia_gaia_cluster"


@responses.activate
def test_set_lsm_cluster(management, resp_lsm_cluster):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-lsm-cluster",
        json=resp_lsm_cluster,
        status=200,
    )

    resp = management.network_objects.lsm_cluster.set(
        uid="d1c363bc-c4c6-4903-9426-495d800b47ae",
        new_name="Gaia_gaia_cluster",
        interfaces=[
            {
                "name": "eth0",
                "new-name": "WAN",
                "member-network-override": "192.168.8.0",
                "ip-address-override": "192.168.8.197",
            },
            {
                "name": "eth1",
                "new-name": "LAN1",
                "member-network-override": "10.8.197.0",
                "ip-address-override": "10.8.197.1",
            },
            {"name": "eth2", "member-network-override": "10.10.10.0"},
        ],
        members=[
            {
                "name": "Gaia_gw1",
                "sic": {"ip-address": "192.168.8.200", "one-time-password": "aaaa"},
            },
            {
                "name": "Gaia_gw2",
                "sic": {"ip-address": "192.168.8.202", "one-time-password": "aaaa"},
            },
        ],
        tags=["t1"],
    )

    assert resp.uid == "d1c363bc-c4c6-4903-9426-495d800b47ae"
    assert resp.name == "Gaia_gaia_cluster"

    resp = management.network_objects.lsm_cluster.set(
        name="Gaia_gaia_cluster old", new_name="Gaia_gaia_cluster"
    )

    assert resp.uid == "d1c363bc-c4c6-4903-9426-495d800b47ae"
    assert resp.name == "Gaia_gaia_cluster"

    # Missing name or UID
    with pytest.raises(MandatoryFieldMissing):
        management.network_objects.lsm_cluster.set()


@responses.activate
def test_delete_lsm_cluster(management, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-lsm-cluster",
        json=resp_message_ok,
        status=200,
    )

    resp = management.network_objects.lsm_cluster.delete(
        uid="d1c363bc-c4c6-4903-9426-495d800b47ae"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_lsm_clusters(management, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-lsm-clusters",
        json=resp_from_to_objects,
        status=200,
    )

    resp = management.network_objects.lsm_cluster.show_lsm_clusters()

    assert isinstance(resp.total, int)
