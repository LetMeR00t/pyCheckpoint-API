import pytest
import responses

from pycheckpoint_api.firewallManagement.exception import MandatoryFieldMissing


@responses.activate
def test_add_checkpoint_host(
    firewallManagement, resp_checkpoint_host_ipv4, resp_checkpoint_host_ipv6
):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-checkpoint-host",
        json=resp_checkpoint_host_ipv4,
        status=200,
    )

    resp = firewallManagement.network_objects.checkpoint_host.add(
        name="secondarylogserver",
        ip_address="5.5.5.5",
        management_blades={
            "network-policy-management": True,
            "logging-and-status": True,
        },
        hardware="Open server",
        interfaces=[],
        nat_settings={"auto-rule": False},
        one_time_password="VeEv7eL.czuc,94pDykUZWE;gcFgf;",
        os="Gaia",
        version="R81",
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
        tags=["t1"],
    )

    assert resp.uid == "f50f3810-d16c-4239-88d0-9f37ac581387"
    assert resp.name == "secondarylogserver"
    assert resp.ipv4_address == "5.5.5.5"

    resp = firewallManagement.network_objects.checkpoint_host.add(
        name="secondarylogserver", ipv4_address="5.5.5.5"
    )

    assert resp.uid == "f50f3810-d16c-4239-88d0-9f37ac581387"
    assert resp.name == "secondarylogserver"
    assert resp.ipv4_address == "5.5.5.5"

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-checkpoint-host",
        json=resp_checkpoint_host_ipv6,
        status=200,
    )

    resp = firewallManagement.network_objects.checkpoint_host.add(
        name="secondarylogserver",
        ipv6_address="2001:db8:0000:0000:0000:0000:0000:000a",
    )

    assert resp.uid == "f50f3810-d16c-4239-88d0-9f37ac581387"
    assert resp.name == "secondarylogserver"
    assert resp.ipv6_address == "2001:db8:0000:0000:0000:0000:0000:000a"

    # None IP address information
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.network_objects.checkpoint_host.add(
            name="secondarylogserver"
        )


@responses.activate
def test_show_checkpoint_host(firewallManagement, resp_checkpoint_host_ipv4):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-checkpoint-host",
        json=resp_checkpoint_host_ipv4,
        status=200,
    )

    resp = firewallManagement.network_objects.checkpoint_host.show(
        uid="f50f3810-d16c-4239-88d0-9f37ac581387"
    )

    assert resp.uid == "f50f3810-d16c-4239-88d0-9f37ac581387"
    assert resp.name == "secondarylogserver"
    assert resp.ipv4_address == "5.5.5.5"


@responses.activate
def test_set_checkpoint_host(
    firewallManagement, resp_checkpoint_host_ipv4, resp_checkpoint_host_ipv6
):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-checkpoint-host",
        json=resp_checkpoint_host_ipv4,
        status=200,
    )

    resp = firewallManagement.network_objects.checkpoint_host.set(
        uid="f50f3810-d16c-4239-88d0-9f37ac581387",
        ip_address="5.5.5.5",
        new_name="secondarylogserver",
        hardware="Open server",
        interfaces=[],
        nat_settings={"auto-rule": False},
        one_time_password="VeEv7eL.czuc,94pDykUZWE;gcFgf;",
        os="Gaia",
        version="R81",
        management_blades={
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
        tags=["t1"],
    )

    assert resp.uid == "f50f3810-d16c-4239-88d0-9f37ac581387"
    assert resp.name == "secondarylogserver"
    assert resp.ipv4_address == "5.5.5.5"

    resp = firewallManagement.network_objects.checkpoint_host.set(
        name="secondarylogserver", ipv4_address="5.5.5.5"
    )

    assert resp.uid == "f50f3810-d16c-4239-88d0-9f37ac581387"
    assert resp.name == "secondarylogserver"
    assert resp.ipv4_address == "5.5.5.5"

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-checkpoint-host",
        json=resp_checkpoint_host_ipv6,
        status=200,
    )

    resp = firewallManagement.network_objects.checkpoint_host.set(
        name="secondarylogserver",
        ipv6_address="2001:db8:0000:0000:0000:0000:0000:000a",
    )

    assert resp.uid == "f50f3810-d16c-4239-88d0-9f37ac581387"
    assert resp.name == "secondarylogserver"
    assert resp.ipv6_address == "2001:db8:0000:0000:0000:0000:0000:000a"

    # None arguments
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.network_objects.checkpoint_host.set()


@responses.activate
def test_delete_checkpoint_host(firewallManagement, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-checkpoint-host",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.network_objects.checkpoint_host.delete(
        uid="99457705-dc26-40ce-b9cd-5633eb09b1aa"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_checkpoint_hosts(firewallManagement, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-checkpoint-hosts",
        json=resp_from_to_objects,
        status=200,
    )

    resp = firewallManagement.network_objects.checkpoint_host.show_checkpoint_hosts()

    assert isinstance(resp.total, int)
