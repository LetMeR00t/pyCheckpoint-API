import responses
import pytest

from pycheckpoint_api.firewallManagement.exception import MandatoryFieldMissing


@responses.activate
def test_add_simple_gateway(
    firewallManagement, resp_simple_gateway_ipv4, resp_simple_gateway_ipv6
):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-simple-gateway",
        json=resp_simple_gateway_ipv4,
        status=200,
    )

    resp = firewallManagement.network_objects.simple_gateway.add(
        name="gw1",
        ip_address="192.0.2.1",
        anti_bot=True,
        anti_virus=True,
        application_control=True,
        content_awareness=True,
        firewall=True,
        firewall_settings=[],
        icap_server=True,
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
        logs_settings={
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
        one_time_password="iiRp7LA!ggCZgoEqbBNOrKonZ",
        os_name="Gaia",
        platform_portal_settings=[],
        tags=["t1"],
        save_logs_locally=False,
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

    assert resp.uid == "99457705-dc26-40ce-b9cd-5633eb09b1aa"
    assert resp.name == "gw1"
    assert resp.ipv4_address == "192.0.2.1"

    resp = firewallManagement.network_objects.simple_gateway.add(
        name="gw1", ipv4_address="192.0.2.1"
    )

    assert resp.uid == "99457705-dc26-40ce-b9cd-5633eb09b1aa"
    assert resp.name == "gw1"
    assert resp.ipv4_address == "192.0.2.1"

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-simple-gateway",
        json=resp_simple_gateway_ipv6,
        status=200,
    )
    resp = firewallManagement.network_objects.simple_gateway.add(
        name="gw1", ipv6_address="2001:db8:0000:0000:0000:0000:0000:000c"
    )

    assert resp.uid == "99457705-dc26-40ce-b9cd-5633eb09b1aa"
    assert resp.name == "gw1"
    assert resp.ipv6_address == "2001:db8:0000:0000:0000:0000:0000:000c"

    # Missing IP information
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.network_objects.simple_gateway.add(name="gw1")


@responses.activate
def test_show_simple_gateway(firewallManagement, resp_simple_gateway_ipv4):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-simple-gateway",
        json=resp_simple_gateway_ipv4,
        status=200,
    )

    resp = firewallManagement.network_objects.simple_gateway.show(
        uid="99457705-dc26-40ce-b9cd-5633eb09b1aa"
    )

    assert resp.uid == "99457705-dc26-40ce-b9cd-5633eb09b1aa"
    assert resp.name == "gw1"
    assert resp.ipv4_address == "192.0.2.1"


@responses.activate
def test_set_simple_gateway(
    firewallManagement, resp_simple_gateway_ipv4, resp_simple_gateway_ipv6
):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-simple-gateway",
        json=resp_simple_gateway_ipv4,
        status=200,
    )

    resp = firewallManagement.network_objects.simple_gateway.set(
        uid="99457705-dc26-40ce-b9cd-5633eb09b1aa",
        ip_address="192.0.2.1",
        anti_bot=True,
        anti_virus=True,
        application_control=True,
        content_awareness=True,
        firewall=True,
        firewall_settings=[],
        icap_server=True,
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
        logs_settings={
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
        one_time_password="iiRp7LA!ggCZgoEqbBNOrKonZ",
        os_name="Gaia",
        platform_portal_settings=[],
        tags=["t1"],
        save_logs_locally=False,
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

    assert resp.uid == "99457705-dc26-40ce-b9cd-5633eb09b1aa"
    assert resp.name == "gw1"
    assert resp.ipv4_address == "192.0.2.1"

    resp = firewallManagement.network_objects.simple_gateway.set(
        name="gw1", ipv4_address="192.0.2.1"
    )

    assert resp.uid == "99457705-dc26-40ce-b9cd-5633eb09b1aa"
    assert resp.name == "gw1"
    assert resp.ipv4_address == "192.0.2.1"

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-simple-gateway",
        json=resp_simple_gateway_ipv6,
        status=200,
    )
    resp = firewallManagement.network_objects.simple_gateway.set(
        name="gw1", ipv6_address="2001:db8:0000:0000:0000:0000:0000:000c"
    )

    assert resp.uid == "99457705-dc26-40ce-b9cd-5633eb09b1aa"
    assert resp.name == "gw1"
    assert resp.ipv6_address == "2001:db8:0000:0000:0000:0000:0000:000c"

    # Missing mandatory field
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.network_objects.simple_gateway.set()


@responses.activate
def test_delete_simple_gateway(firewallManagement, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-simple-gateway",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.network_objects.simple_gateway.delete(
        uid="99457705-dc26-40ce-b9cd-5633eb09b1aa"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_simple_gateways(firewallManagement, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-simple-gateways",
        json=resp_from_to_objects,
        status=200,
    )

    resp = firewallManagement.network_objects.simple_gateway.show_simple_gateways()

    assert isinstance(resp.total, int)
