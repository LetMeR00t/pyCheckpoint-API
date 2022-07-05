import responses


@responses.activate
def test_abort_get_interfaces(firewallManagement, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/abort-get-interfaces",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.network_objects.network_interface.abort_get_interfaces(
        task_id="01234567-89ab-cdef-a930-8c37a59972b3"
    )

    assert resp.message == "OK"


@responses.activate
def test_get_interfaces(firewallManagement, resp_get_interfaces):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/get-interfaces",
        json=resp_get_interfaces,
        status=200,
    )

    resp = firewallManagement.network_objects.network_interface.get_interfaces(
        target_name="gw123", with_topology=True
    )

    assert resp.tasks[0].task_id == "01234567-89ab-cdef-9e1f-0e1e68312345"
