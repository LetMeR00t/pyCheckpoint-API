import pytest
import responses

from pycheckpoint_api.firewallManagement.exception import MandatoryFieldMissing


@responses.activate
def test_add_host(firewallManagement, resp_host_ipv4, resp_host_ipv6):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-host",
        json=resp_host_ipv4,
        status=200,
    )

    resp = firewallManagement.network_objects.host.add(
        name="New Host 4",
        ip_address="192.0.2.1",
        tags=["t1", "t2", "t3"],
        interfaces="",
        host_servers={},
        nat_settings={
            "auto-rule": True,
            "method": "hide",
            "hide-behind": "ip-address",
            "ipv4-address": "192.0.2.1",
            "ipv6-address": "FE80::0202:B3FF:FE1E:8329",
            "install-on": "All",
        },
    )

    assert resp.uid == "9423d36f-2d66-4754-b9e2-e7f4493756d4"
    assert resp.name == "New Host 4"
    assert resp.ipv4_address == "192.0.2.1"
    assert resp.tags == ["t1", "t2", "t3"]

    resp = firewallManagement.network_objects.host.add(
        name="New Host 4",
        ipv4_address="192.0.2.1",
    )

    assert resp.uid == "9423d36f-2d66-4754-b9e2-e7f4493756d4"
    assert resp.name == "New Host 4"
    assert resp.ipv4_address == "192.0.2.1"
    assert resp.tags == ["t1", "t2", "t3"]

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-host",
        json=resp_host_ipv6,
        status=200,
    )

    resp = firewallManagement.network_objects.host.add(
        name="New Host 4",
        ipv6_address="2001:db8:0000:0000:0000:0000:0000:0005",
    )

    assert resp.uid == "9423d36f-2d66-4754-b9e2-e7f4493756d4"
    assert resp.name == "New Host 4"
    assert resp.ipv6_address == "2001:db8:0000:0000:0000:0000:0000:0005"
    assert resp.tags == ["t1", "t2", "t3"]

    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.network_objects.host.add(name="New Host 4")


@responses.activate
def test_show_host(firewallManagement, resp_host_ipv4):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-host",
        json=resp_host_ipv4,
        status=200,
    )

    resp = firewallManagement.network_objects.host.show(
        uid="9423d36f-2d66-4754-b9e2-e7f4493756d4"
    )

    assert resp.uid == "9423d36f-2d66-4754-b9e2-e7f4493756d4"
    assert resp.name == "New Host 4"
    assert resp.ipv4_address == "192.0.2.1"

    resp = firewallManagement.network_objects.host.show(name="New Host 4")

    assert resp.uid == "9423d36f-2d66-4754-b9e2-e7f4493756d4"
    assert resp.name == "New Host 4"
    assert resp.ipv4_address == "192.0.2.1"

    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.network_objects.host.show()


@responses.activate
def test_set_host(firewallManagement, resp_host_ipv4, resp_host_ipv6):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-host",
        json=resp_host_ipv4,
        status=200,
    )

    resp = firewallManagement.network_objects.host.set(
        uid="9423d36f-2d66-4754-b9e2-e7f4493756d4",
        new_name="New Host 4",
        ip_address="192.0.2.1",
        tags=["t1", "t2", "t3"],
        interfaces="",
        host_servers={},
        nat_settings={
            "auto-rule": True,
            "method": "hide",
            "hide-behind": "ip-address",
            "ipv4-address": "192.0.2.1",
            "ipv6-address": "FE80::0202:B3FF:FE1E:8329",
            "install-on": "All",
        },
    )

    assert resp.uid == "9423d36f-2d66-4754-b9e2-e7f4493756d4"
    assert resp.name == "New Host 4"
    assert resp.ipv4_address == "192.0.2.1"
    assert resp.tags == ["t1", "t2", "t3"]

    resp = firewallManagement.network_objects.host.set(
        name="New Host 4",
        ipv4_address="192.0.2.1",
    )

    assert resp.uid == "9423d36f-2d66-4754-b9e2-e7f4493756d4"
    assert resp.name == "New Host 4"
    assert resp.ipv4_address == "192.0.2.1"
    assert resp.tags == ["t1", "t2", "t3"]

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-host",
        json=resp_host_ipv6,
        status=200,
    )

    resp = firewallManagement.network_objects.host.set(
        name="New Host 4",
        ipv6_address="2001:db8:0000:0000:0000:0000:0000:0005",
    )

    assert resp.uid == "9423d36f-2d66-4754-b9e2-e7f4493756d4"
    assert resp.name == "New Host 4"
    assert resp.ipv6_address == "2001:db8:0000:0000:0000:0000:0000:0005"
    assert resp.tags == ["t1", "t2", "t3"]

    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.network_objects.host.set()


@responses.activate
def test_delete_host(firewallManagement, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-host",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.network_objects.host.delete(
        uid="9423d36f-2d66-4754-b9e2-e7f4493756d4"
    )

    assert resp.message == "OK"

    resp = firewallManagement.network_objects.host.delete(name="New Host 4")

    assert resp.message == "OK"

    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.network_objects.host.delete()


@responses.activate
def test_show_hosts(firewallManagement, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-hosts",
        json=resp_from_to_objects,
        status=200,
    )

    resp = firewallManagement.network_objects.host.show_hosts(
        filter_results="host_", order={"ASC": "name"}
    )

    assert isinstance(resp.total, int)
