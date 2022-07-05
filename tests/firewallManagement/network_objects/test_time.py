import responses


@responses.activate
def test_add_time(firewallManagement, resp_time):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-time",
        json=resp_time,
        status=200,
    )

    resp = firewallManagement.network_objects.time.add(
        name="timeObject1", start_now="true"
    )

    assert resp.uid == "aa785d6d-7785-aad5-36a3-ab2d74c966ee"
    assert resp.name == "timeObject1"
    assert resp.start_now is True


@responses.activate
def test_show_time(firewallManagement, resp_time):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-time",
        json=resp_time,
        status=200,
    )

    resp = firewallManagement.network_objects.time.show(
        uid="d5e8d56f-2d77-4824-a5d2-c4a7885dd4a7"
    )

    assert resp.uid == "aa785d6d-7785-aad5-36a3-ab2d74c966ee"
    assert resp.name == "timeObject1"
    assert resp.start_now is True


@responses.activate
def test_set_time(firewallManagement, resp_time):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-time",
        json=resp_time,
        status=200,
    )

    resp = firewallManagement.network_objects.time.set(
        uid="d5e8d56f-2d77-4824-a5d2-c4s7885dd4z7",
        subnet="192.0.2.0",
        subnet_mask="255.255.255.0",
    )

    assert resp.uid == "aa785d6d-7785-aad5-36a3-ab2d74c966ee"
    assert resp.name == "timeObject1"
    assert resp.start_now is True


@responses.activate
def test_delete_time(firewallManagement, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-time",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.network_objects.time.delete(
        uid="d5e8d56f-2d77-4824-a5d2-c4a7885dd4a7"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_times(firewallManagement, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-times",
        json=resp_from_to_objects,
        status=200,
    )

    resp = firewallManagement.network_objects.time.show_times()

    assert isinstance(resp.total, int)
