import pytest
import responses

from pycheckpoint_api.firewallManagement.exception import MandatoryFieldMissing


@responses.activate
def test_add_simple_cluster(firewallManagement, resp_task):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-simple-cluster",
        json=resp_task,
        status=200,
    )

    resp = firewallManagement.network_objects.simple_cluster.add(
        name="cluster1",
        ip_address="17.23.5.1",
        anti_bot=True,
        anti_virus=True,
        application_control=True,
        cluster_mode="cluster-xl-ha",
        content_awareness=True,
        data_awareness=True,
        firewall=True,
        firewall_settings=[],
        hardware="hardware",
        interfaces=[
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
        ips=True,
        members=["member1", "member2"],
        os_name="Gaia",
        platform_portal_settings=[],
        tags=["t1"],
        send_alerts_to_server=[
            {
                "uid": "6da0cc30-4ac4-c544-bd20-d8ba9bf7f51c",
            }
        ],
        send_logs_to_backup_server=[],
        send_logs_to_server=[
            {
                "uid": "6da0cc30-4ac4-c544-bd20-d8ba9bf7f51c",
            }
        ],
        threat_emulation=True,
        threat_extraction=True,
        threat_prevention_mode="custom",
        url_filtering=True,
        usercheck_portal_settings={"enabled": True},
        version="R81.10",
        vpn=False,
        vpn_settings=[],
    )

    assert resp.task_id == "01234567-89ab-cdef-a930-8c37a59972b3"

    resp = firewallManagement.network_objects.simple_cluster.add(
        name="cluster1", ipv4_address="192.0.2.1"
    )

    resp = firewallManagement.network_objects.simple_cluster.add(
        name="cluster1", ipv6_address="2001:db8:0000:0000:0000:0000:0000:000b"
    )

    assert resp.task_id == "01234567-89ab-cdef-a930-8c37a59972b3"


@responses.activate
def test_show_simple_cluster(
    firewallManagement, resp_simple_cluster_ipv4, resp_simple_cluster_ipv6
):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-simple-cluster",
        json=resp_simple_cluster_ipv4,
        status=200,
    )

    resp = firewallManagement.network_objects.simple_cluster.show(
        uid="4a5d882a-5568-2c3b-aa78-751ab23d6c11"
    )

    assert resp.uid == "4a5d882a-5568-2c3b-aa78-751ab23d6c11"
    assert resp.name == "cluster1"
    assert resp.ipv4_address == "17.23.5.1"

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-simple-cluster",
        json=resp_simple_cluster_ipv6,
        status=200,
    )

    resp = firewallManagement.network_objects.simple_cluster.show(
        uid="4a5d882a-5568-2c3b-aa78-751ab23d6c11"
    )

    assert resp.uid == "4a5d882a-5568-2c3b-aa78-751ab23d6c11"
    assert resp.name == "cluster1"
    assert resp.ipv6_address == "2001:db8:0000:0000:0000:0000:0000:000b"

    # Missing IP information
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.network_objects.simple_cluster.add(name="cluster1")


@responses.activate
def test_set_simple_cluster(firewallManagement, resp_task):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-simple-cluster",
        json=resp_task,
        status=200,
    )

    resp = firewallManagement.network_objects.simple_cluster.set(
        uid="4a5d882a-5568-2c3b-aa78-751ab23d6c11",
        new_name="cluster1",
        ip_address="17.23.5.1",
        anti_bot=True,
        anti_virus=True,
        application_control=True,
        cluster_mode="cluster-xl-ha",
        content_awareness=True,
        data_awareness=True,
        firewall=True,
        firewall_settings=[],
        hardware="hardware",
        interfaces=[
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
        ips=True,
        members=["member1", "member2"],
        os_name="Gaia",
        platform_portal_settings=[],
        tags=["t1"],
        send_alerts_to_server=[
            {
                "uid": "6da0cc30-4ac4-c544-bd20-d8ba9bf7f51c",
            }
        ],
        send_logs_to_backup_server=[],
        send_logs_to_server=[
            {
                "uid": "6da0cc30-4ac4-c544-bd20-d8ba9bf7f51c",
            }
        ],
        threat_emulation=True,
        threat_extraction=True,
        threat_prevention_mode="custom",
        url_filtering=True,
        usercheck_portal_settings={"enabled": True},
        version="R81.10",
        vpn=False,
        vpn_settings=[],
    )

    assert resp.task_id == "01234567-89ab-cdef-a930-8c37a59972b3"

    resp = firewallManagement.network_objects.simple_cluster.set(
        name="cluster1", ip_address="192.0.2.1"
    )

    assert resp.task_id == "01234567-89ab-cdef-a930-8c37a59972b3"

    resp = firewallManagement.network_objects.simple_cluster.set(
        name="cluster1", ipv4_address="192.0.2.1"
    )

    assert resp.task_id == "01234567-89ab-cdef-a930-8c37a59972b3"

    # None arguments
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.network_objects.simple_cluster.set()

    resp = firewallManagement.network_objects.simple_cluster.set(
        name="cluster1", ipv6_address="2001:db8:0000:0000:0000:0000:0000:000b"
    )

    assert resp.task_id == "01234567-89ab-cdef-a930-8c37a59972b3"


@responses.activate
def test_delete_simple_cluster(firewallManagement, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-simple-cluster",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.network_objects.simple_cluster.delete(
        uid="4a5d882a-5568-2c3b-aa78-751ab23d6c11"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_simple_clusters(firewallManagement, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-simple-clusters",
        json=resp_from_to_objects,
        status=200,
    )

    resp = firewallManagement.network_objects.simple_cluster.show_simple_clusters()

    assert isinstance(resp.total, int)
