# from box import Box
import responses

# from pycheckpoint.firewallManagement.exception import MandatoryFieldMissing


@responses.activate
def test_add_host(firewallManagement, resp_host):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-host",
        json=resp_host,
        status=200,
    )

    resp = firewallManagement.network_objects.host.add(
        name="New Host 4", ip_address="192.0.2.1"
    )

    assert resp.name == "New Host 4"
    assert resp.ipv4_address == "192.0.2.1"


@responses.activate
def test_show_host(firewallManagement, resp_host):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-host",
        json=resp_host,
        status=200,
    )

    resp = firewallManagement.network_objects.host.show(
        uid="9423d36f-2d66-4754-b9e2-e7f4493756d4"
    )

    assert resp.name == "New Host 4"
    assert resp.ipv4_address == "192.0.2.1"


@responses.activate
def test_set_host(firewallManagement, resp_host):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-host",
        json=resp_host,
        status=200,
    )

    resp = firewallManagement.network_objects.host.set(
        uid="9423d36f-2d66-4754-b9e2-e7f4493756d4", ip_address="192.0.2.1"
    )

    assert resp.name == "New Host 4"
    assert resp.ipv4_address == "192.0.2.1"


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


@responses.activate
def test_show_hosts(firewallManagement, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-hosts",
        json=resp_from_to_objects,
        status=200,
    )

    resp = firewallManagement.network_objects.host.show_hosts()

    assert isinstance(resp.total, int)


@responses.activate
def test_add_network(firewallManagement, resp_network):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-network",
        json=resp_network,
        status=200,
    )

    resp = firewallManagement.network_objects.network.add(
        name="New Host 4", subnet="192.0.2.0", subnet_mask="255.255.255.0"
    )

    assert resp.uid == "d5e8d56f-2d77-4824-a5d2-c4s7885dd4z7"
    assert resp.name == "New Host 4"
    assert resp.subnet == "192.0.2.0"
    assert resp.subnet_mask == "255.255.255.0"


@responses.activate
def test_show_network(firewallManagement, resp_network):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-network",
        json=resp_network,
        status=200,
    )

    resp = firewallManagement.network_objects.network.show(
        uid="d5e8d56f-2d77-4824-a5d2-c4s7885dd4z7"
    )

    assert resp.name == "New Host 4"
    assert resp.subnet == "192.0.2.0"
    assert resp.subnet_mask == "255.255.255.0"


@responses.activate
def test_set_network(firewallManagement, resp_network):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-network",
        json=resp_network,
        status=200,
    )

    resp = firewallManagement.network_objects.network.set(
        uid="d5e8d56f-2d77-4824-a5d2-c4s7885dd4z7",
        subnet="192.0.2.0",
        subnet_mask="255.255.255.0",
    )

    assert resp.name == "New Host 4"
    assert resp.subnet == "192.0.2.0"
    assert resp.subnet_mask == "255.255.255.0"


@responses.activate
def test_delete_network(firewallManagement, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-network",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.network_objects.network.delete(
        uid="9423d36f-2d66-4754-b9e2-e7f4493756d4"
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
