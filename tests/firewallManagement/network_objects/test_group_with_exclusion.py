import responses


@responses.activate
def test_add_group_with_exclusion(firewallManagement, resp_group_with_exclusion):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-group-with-exclusion",
        json=resp_group_with_exclusion,
        status=200,
    )

    resp = firewallManagement.network_objects.group_with_exclusion.add(
        name="DemoGroupWithExclusion", include="New Group 1", exception="New Group 2"
    )

    assert resp.uid == "dce451da-c9c7-46a9-bdb5-8fc953a6f172"
    assert resp.name == "DemoGroupWithExclusion"


@responses.activate
def test_show_group_with_exclusion(firewallManagement, resp_group_with_exclusion):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-group-with-exclusion",
        json=resp_group_with_exclusion,
        status=200,
    )

    resp = firewallManagement.network_objects.group_with_exclusion.show(
        uid="ed997ff8-6709-4d71-a713-99bf01711cd5"
    )

    assert resp.uid == "dce451da-c9c7-46a9-bdb5-8fc953a6f172"
    assert resp.name == "DemoGroupWithExclusion"


@responses.activate
def test_set_group_with_exclusion(firewallManagement, resp_group_with_exclusion):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-group-with-exclusion",
        json=resp_group_with_exclusion,
        status=200,
    )

    resp = firewallManagement.network_objects.group_with_exclusion.set(
        uid="ed997ff8-6709-4d71-a713-99bf01711cd5", new_name="New Group 3"
    )

    assert resp.uid == "dce451da-c9c7-46a9-bdb5-8fc953a6f172"
    assert resp.name == "DemoGroupWithExclusion"


@responses.activate
def test_delete_group_with_exclusion(firewallManagement, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-group-with-exclusion",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.network_objects.group_with_exclusion.delete(
        uid="ed997ff8-6709-4d71-a713-99bf01711cd5"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_groups_with_exclusion(firewallManagement, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-groups-with-exclusion",
        json=resp_from_to_objects,
        status=200,
    )

    resp = (
        firewallManagement.network_objects.group_with_exclusion.show_groups_with_exclusion()
    )

    assert isinstance(resp.total, int)
