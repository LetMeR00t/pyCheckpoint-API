import responses


@responses.activate
def test_add_service_sctp(firewallManagement, resp_service_sctp):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-service-sctp",
        json=resp_service_sctp,
        status=200,
    )

    resp = firewallManagement.service_applications.service_sctp.add(
        name="New_SCTP_Service_1",
        port=5669,
        keep_connections_open_after_policy_installation=False,
        session_timeout=0,
        match_for_any=True,
        sync_connections_on_cluster=True,
        aggressive_aging={"enable": True, "timeout": 360, "use-default-timeout": False},
    )

    assert resp.uid == "d0385c6d-72dd-4981-b951-4783b7100343"
    assert resp.name == "New_SCTP_Service_1"
    assert resp.port == "5669"


@responses.activate
def test_show_service_sctp(firewallManagement, resp_service_sctp):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-service-sctp",
        json=resp_service_sctp,
        status=200,
    )

    resp = firewallManagement.service_applications.service_sctp.show(
        uid="d0385c6d-72dd-4981-b951-4783b7100343"
    )

    assert resp.uid == "d0385c6d-72dd-4981-b951-4783b7100343"
    assert resp.name == "New_SCTP_Service_1"
    assert resp.port == "5669"


@responses.activate
def test_set_service_sctp(firewallManagement, resp_service_sctp):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-service-sctp",
        json=resp_service_sctp,
        status=200,
    )

    resp = firewallManagement.service_applications.service_sctp.set(
        uid="d0385c6d-72dd-4981-b951-4783b7100343", ip_address="192.0.2.1"
    )

    assert resp.uid == "d0385c6d-72dd-4981-b951-4783b7100343"
    assert resp.name == "New_SCTP_Service_1"
    assert resp.port == "5669"


@responses.activate
def test_delete_service_sctp(firewallManagement, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-service-sctp",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.service_applications.service_sctp.delete(
        uid="d0385c6d-72dd-4981-b951-4783b7100343"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_services_sctp(firewallManagement, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-services-sctp",
        json=resp_from_to_objects,
        status=200,
    )

    resp = firewallManagement.service_applications.service_sctp.show_services_sctp()

    assert isinstance(resp.total, int)
