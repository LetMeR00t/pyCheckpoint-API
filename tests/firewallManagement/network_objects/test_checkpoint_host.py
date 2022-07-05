import responses


@responses.activate
def test_add_checkpoint_host(firewallManagement, resp_checkpoint_host):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-checkpoint-host",
        json=resp_checkpoint_host,
        status=200,
    )

    resp = firewallManagement.network_objects.checkpoint_host.add(
        name="secondarylogserver",
        ipv4_address="5.5.5.5",
        management_blades={
            "network-policy-management": True,
            "logging-and-status": True,
        },
    )

    assert resp.uid == "f50f3810-d16c-4239-88d0-9f37ac581387"
    assert resp.name == "secondarylogserver"
    assert resp.ipv4_address == "5.5.5.5"


@responses.activate
def test_show_checkpoint_host(firewallManagement, resp_checkpoint_host):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-checkpoint-host",
        json=resp_checkpoint_host,
        status=200,
    )

    resp = firewallManagement.network_objects.checkpoint_host.show(
        uid="f50f3810-d16c-4239-88d0-9f37ac581387"
    )

    assert resp.uid == "f50f3810-d16c-4239-88d0-9f37ac581387"
    assert resp.name == "secondarylogserver"
    assert resp.ipv4_address == "5.5.5.5"


@responses.activate
def test_set_checkpoint_host(firewallManagement, resp_checkpoint_host):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-checkpoint-host",
        json=resp_checkpoint_host,
        status=200,
    )

    resp = firewallManagement.network_objects.checkpoint_host.set(
        uid="f50f3810-d16c-4239-88d0-9f37ac581387", ip_address="5.5.5.5"
    )

    assert resp.uid == "f50f3810-d16c-4239-88d0-9f37ac581387"
    assert resp.name == "secondarylogserver"
    assert resp.ipv4_address == "5.5.5.5"


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
