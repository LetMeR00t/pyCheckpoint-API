import responses


@responses.activate
def test_add_access_point_name(firewallManagement, resp_access_point_name):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-access-point-name",
        json=resp_access_point_name,
        status=200,
    )

    resp = firewallManagement.network_objects.access_point_name.add(
        name="myaccesspointname",
        apn="apnname",
        enforce_end_user_domain=True,
        end_user_domain="All_Internet",
    )

    assert resp.uid == "5064644d-6cc7-4703-823c-54f01ab720e6"
    assert resp.name == "myaccesspointname"


@responses.activate
def test_show_access_point_name(firewallManagement, resp_access_point_name):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-access-point-name",
        json=resp_access_point_name,
        status=200,
    )

    resp = firewallManagement.network_objects.access_point_name.show(
        uid="5064644d-6cc7-4703-823c-54f01ab720e6"
    )

    assert resp.uid == "5064644d-6cc7-4703-823c-54f01ab720e6"
    assert resp.name == "myaccesspointname"


@responses.activate
def test_set_access_point_name(firewallManagement, resp_access_point_name):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-access-point-name",
        json=resp_access_point_name,
        status=200,
    )

    resp = firewallManagement.network_objects.access_point_name.set(
        uid="5064644d-6cc7-4703-823c-54f01ab720e6", new_name="myaccesspointname"
    )

    assert resp.uid == "5064644d-6cc7-4703-823c-54f01ab720e6"
    assert resp.name == "myaccesspointname"


@responses.activate
def test_delete_access_point_name(firewallManagement, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-access-point-name",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.network_objects.access_point_name.delete(
        uid="5064644d-6cc7-4703-823c-54f01ab720e6"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_access_point_names(firewallManagement, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-access-point-names",
        json=resp_from_to_objects,
        status=200,
    )

    resp = (
        firewallManagement.network_objects.access_point_name.show_access_point_names()
    )

    assert isinstance(resp.total, int)
