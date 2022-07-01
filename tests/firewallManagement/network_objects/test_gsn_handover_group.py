import responses


@responses.activate
def test_add_gsn_handover_group(firewallManagement, resp_gsn_handover_group):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-gsn-handover-group",
        json=resp_gsn_handover_group,
        status=200,
    )

    resp = firewallManagement.network_objects.gsn_handover_group.add(
        name="gsnhandovergroup"
    )

    assert resp.uid == "f140a9d1-4167-456a-931d-abdaa4c8aa7e"
    assert resp.name == "gsnhandovergroup"


@responses.activate
def test_show_gsn_handover_group(firewallManagement, resp_gsn_handover_group):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-gsn-handover-group",
        json=resp_gsn_handover_group,
        status=200,
    )

    resp = firewallManagement.network_objects.gsn_handover_group.show(
        uid="f140a9d1-4167-456a-931d-abdaa4c8aa7e"
    )

    assert resp.uid == "f140a9d1-4167-456a-931d-abdaa4c8aa7e"
    assert resp.name == "gsnhandovergroup"


@responses.activate
def test_set_gsn_handover_group(firewallManagement, resp_gsn_handover_group):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-gsn-handover-group",
        json=resp_gsn_handover_group,
        status=200,
    )

    resp = firewallManagement.network_objects.gsn_handover_group.set(
        uid="f140a9d1-4167-456a-931d-abdaa4c8aa7e", new_name="gsnhandovergroup"
    )

    assert resp.uid == "f140a9d1-4167-456a-931d-abdaa4c8aa7e"
    assert resp.name == "gsnhandovergroup"


@responses.activate
def test_delete_gsn_handover_group(firewallManagement, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-gsn-handover-group",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.network_objects.gsn_handover_group.delete(
        uid="f140a9d1-4167-456a-931d-abdaa4c8aa7e"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_gsn_handover_groups(firewallManagement, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-gsn-handover-groups",
        json=resp_from_to_objects,
        status=200,
    )

    resp = (
        firewallManagement.network_objects.gsn_handover_group.show_gsn_handover_groups()
    )

    assert isinstance(resp.total, int)
