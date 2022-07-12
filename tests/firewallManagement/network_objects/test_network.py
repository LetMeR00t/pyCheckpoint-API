import responses
import pytest

from pycheckpoint_api.firewallManagement.exception import MandatoryFieldMissing


@responses.activate
def test_add_network(firewallManagement, resp_network_ipv4, resp_network_ipv6):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-network",
        json=resp_network_ipv4,
        status=200,
    )

    resp = firewallManagement.network_objects.network.add(
        name="New Network 4",
        subnet="192.0.2.0",
        subnet_mask="255.255.255.0",
        broadcast="disallow",
        nat_settings={"auto-rule": False},
        tags=["t1"],
    )

    assert resp.uid == "d5e8d56f-2d77-4824-a5d2-c4a7885dd4a7"
    assert resp.name == "New Network 4"
    assert resp.subnet == "192.0.2.0"
    assert resp.subnet_mask == "255.255.255.0"

    resp = firewallManagement.network_objects.network.add(
        name="New Network 4", subnet4="192.0.2.0", mask_length="24"
    )

    assert resp.uid == "d5e8d56f-2d77-4824-a5d2-c4a7885dd4a7"
    assert resp.name == "New Network 4"
    assert resp.subnet == "192.0.2.0"
    assert resp.subnet_mask == "255.255.255.0"

    resp = firewallManagement.network_objects.network.add(
        name="New Network 4", subnet4="192.0.2.0", mask_length4="24"
    )

    assert resp.uid == "d5e8d56f-2d77-4824-a5d2-c4a7885dd4a7"
    assert resp.name == "New Network 4"
    assert resp.subnet == "192.0.2.0"
    assert resp.subnet_mask == "255.255.255.0"

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-network",
        json=resp_network_ipv6,
        status=200,
    )

    resp = firewallManagement.network_objects.network.add(
        name="New Network 4",
        subnet6="2001:0DB8:ABCD:0012:0000:0000:0000:0005",
        mask_length6=128,
    )

    assert resp.uid == "d5e8d56f-2d77-4824-a5d2-c4a7885dd4a7"
    assert resp.name == "New Network 4"
    assert resp.subnet6 == "2001:0DB8:ABCD:0012:0000:0000:0000:0005"
    assert resp.mask_length6 == 128

    # Missing IP information
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.network_objects.network.add(name="network1")
    # Missing mask information
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.network_objects.network.add(
            name="network1", subnet="192.0.2.0"
        )


@responses.activate
def test_show_network(firewallManagement, resp_network_ipv4):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-network",
        json=resp_network_ipv4,
        status=200,
    )

    resp = firewallManagement.network_objects.network.show(
        uid="d5e8d56f-2d77-4824-a5d2-c4a7885dd4a7"
    )

    assert resp.uid == "d5e8d56f-2d77-4824-a5d2-c4a7885dd4a7"
    assert resp.name == "New Network 4"
    assert resp.subnet == "192.0.2.0"
    assert resp.subnet_mask == "255.255.255.0"


@responses.activate
def test_set_network(firewallManagement, resp_network_ipv4, resp_network_ipv6):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-network",
        json=resp_network_ipv4,
        status=200,
    )

    resp = firewallManagement.network_objects.network.set(
        uid="d5e8d56f-2d77-4824-a5d2-c4s7885dd4z7",
        new_name="New Network 4",
        subnet="192.0.2.0",
        subnet_mask="255.255.255.0",
        broadcast="disallow",
        nat_settings={"auto-rule": False},
        tags=["t1"],
    )

    assert resp.uid == "d5e8d56f-2d77-4824-a5d2-c4a7885dd4a7"
    assert resp.name == "New Network 4"
    assert resp.subnet == "192.0.2.0"
    assert resp.subnet_mask == "255.255.255.0"

    resp = firewallManagement.network_objects.network.set(
        name="New Network 4", subnet4="192.0.2.0", mask_length="24"
    )

    assert resp.uid == "d5e8d56f-2d77-4824-a5d2-c4a7885dd4a7"
    assert resp.name == "New Network 4"
    assert resp.subnet == "192.0.2.0"
    assert resp.subnet_mask == "255.255.255.0"

    resp = firewallManagement.network_objects.network.set(
        name="New Network 4", subnet4="192.0.2.0", mask_length4="24"
    )

    assert resp.uid == "d5e8d56f-2d77-4824-a5d2-c4a7885dd4a7"
    assert resp.name == "New Network 4"
    assert resp.subnet == "192.0.2.0"
    assert resp.subnet_mask == "255.255.255.0"

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-network",
        json=resp_network_ipv6,
        status=200,
    )

    resp = firewallManagement.network_objects.network.set(
        name="New Network 4",
        subnet6="2001:0DB8:ABCD:0012:0000:0000:0000:0005",
        mask_length6=128,
    )

    assert resp.uid == "d5e8d56f-2d77-4824-a5d2-c4a7885dd4a7"
    assert resp.name == "New Network 4"
    assert resp.subnet6 == "2001:0DB8:ABCD:0012:0000:0000:0000:0005"
    assert resp.mask_length6 == 128

    # Missing mandatory field
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.network_objects.network.set()


@responses.activate
def test_delete_network(firewallManagement, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-network",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.network_objects.network.delete(
        uid="d5e8d56f-2d77-4824-a5d2-c4a7885dd4a7"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_networks(firewallManagement, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-networks",
        json=resp_from_to_objects,
        status=200,
    )

    resp = firewallManagement.network_objects.network.show_networks()

    assert isinstance(resp.total, int)
