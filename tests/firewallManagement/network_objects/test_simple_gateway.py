import responses


@responses.activate
def test_add_simple_gateway(firewallManagement, resp_simple_gateway):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-simple-gateway",
        json=resp_simple_gateway,
        status=200,
    )

    resp = firewallManagement.network_objects.simple_gateway.add(
        name="gw1", ip_address="192.0.2.1"
    )

    assert resp.uid == "99457705-dc26-40ce-b9cd-5633eb09b1aa"
    assert resp.name == "gw1"
    assert resp.ipv4_address == "192.0.2.1"


@responses.activate
def test_show_simple_gateway(firewallManagement, resp_simple_gateway):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-simple-gateway",
        json=resp_simple_gateway,
        status=200,
    )

    resp = firewallManagement.network_objects.simple_gateway.show(
        uid="99457705-dc26-40ce-b9cd-5633eb09b1aa"
    )

    assert resp.uid == "99457705-dc26-40ce-b9cd-5633eb09b1aa"
    assert resp.name == "gw1"
    assert resp.ipv4_address == "192.0.2.1"


@responses.activate
def test_set_simple_gateway(firewallManagement, resp_simple_gateway):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-simple-gateway",
        json=resp_simple_gateway,
        status=200,
    )

    resp = firewallManagement.network_objects.simple_gateway.set(
        uid="99457705-dc26-40ce-b9cd-5633eb09b1aa", ip_address="192.0.2.1"
    )

    assert resp.uid == "99457705-dc26-40ce-b9cd-5633eb09b1aa"
    assert resp.name == "gw1"
    assert resp.ipv4_address == "192.0.2.1"


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
