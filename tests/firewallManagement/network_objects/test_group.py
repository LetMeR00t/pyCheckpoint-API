import responses


@responses.activate
def test_add_group(firewallManagement, resp_group):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-group",
        json=resp_group,
        status=200,
    )

    resp = firewallManagement.network_objects.group.add(name="New Group 4")

    assert resp.uid == "ed997ff8-6709-4d71-a713-99bf01711cd5"
    assert resp.name == "New Group 3"


@responses.activate
def test_show_group(firewallManagement, resp_group):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-group",
        json=resp_group,
        status=200,
    )

    resp = firewallManagement.network_objects.group.show(
        uid="ed997ff8-6709-4d71-a713-99bf01711cd5"
    )

    assert resp.uid == "ed997ff8-6709-4d71-a713-99bf01711cd5"
    assert resp.name == "New Group 3"


@responses.activate
def test_set_group(firewallManagement, resp_group):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-group",
        json=resp_group,
        status=200,
    )

    resp = firewallManagement.network_objects.group.set(
        uid="ed997ff8-6709-4d71-a713-99bf01711cd5", new_name="New Group 3"
    )

    assert resp.uid == "ed997ff8-6709-4d71-a713-99bf01711cd5"
    assert resp.name == "New Group 3"


@responses.activate
def test_delete_group(firewallManagement, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-group",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.network_objects.group.delete(
        uid="ed997ff8-6709-4d71-a713-99bf01711cd5"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_groups(firewallManagement, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-groups",
        json=resp_from_to_objects,
        status=200,
    )

    resp = firewallManagement.network_objects.group.show_objects()

    assert isinstance(resp.total, int)
