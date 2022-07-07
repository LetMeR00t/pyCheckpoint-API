import responses


@responses.activate
def test_add_host(firewallManagement, resp_host):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-host",
        json=resp_host,
        status=200,
    )

    resp = firewallManagement.network_objects.host.add(
        name="New Host 4", ip_address="192.0.2.1", tags=["t1", "t2", "t3"]
    )

    assert resp.uid == "9423d36f-2d66-4754-b9e2-e7f4493756d4"
    assert resp.name == "New Host 4"
    assert resp.ipv4_address == "192.0.2.1"
    assert resp.tags == ["t1", "t2", "t3"]


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

    assert resp.uid == "9423d36f-2d66-4754-b9e2-e7f4493756d4"
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

    assert resp.uid == "9423d36f-2d66-4754-b9e2-e7f4493756d4"
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
