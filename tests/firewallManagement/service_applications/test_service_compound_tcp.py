import pytest
import responses

from pycheckpoint_api.firewallManagement.exception import MandatoryFieldMissing


@responses.activate
def test_add_service_compound_tcp(firewallManagement, resp_service_compound_tcp):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-service-compound-tcp",
        json=resp_service_compound_tcp,
        status=200,
    )

    resp = firewallManagement.service_applications.service_compound_tcp.add(
        name="mycompoundtcp",
        compound_service="pointcast",
        keep_connections_open_after_policy_installation=False,
        tags=["t1"],
    )

    assert resp.uid == "1f0f2270-b297-4400-afa4-d9f56a1cb407"
    assert resp.name == "mycompoundtcp"


@responses.activate
def test_show_service_compound_tcp(firewallManagement, resp_service_compound_tcp):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-service-compound-tcp",
        json=resp_service_compound_tcp,
        status=200,
    )

    resp = firewallManagement.service_applications.service_compound_tcp.show(
        uid="1f0f2270-b297-4400-afa4-d9f56a1cb407"
    )

    assert resp.uid == "1f0f2270-b297-4400-afa4-d9f56a1cb407"
    assert resp.name == "mycompoundtcp"


@responses.activate
def test_set_service_compound_tcp(firewallManagement, resp_service_compound_tcp):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-service-compound-tcp",
        json=resp_service_compound_tcp,
        status=200,
    )

    resp = firewallManagement.service_applications.service_compound_tcp.set(
        uid="1f0f2270-b297-4400-afa4-d9f56a1cb407",
        new_name="mycompoundtcp",
        compound_service="pointcast",
        keep_connections_open_after_policy_installation=False,
        tags=["t1"],
    )

    assert resp.uid == "1f0f2270-b297-4400-afa4-d9f56a1cb407"
    assert resp.name == "mycompoundtcp"

    resp = firewallManagement.service_applications.service_compound_tcp.set(
        name="mycompoundtcp",
        interface_uuid="97aeb460-9aea-11d5-bd16-0090272ccb30",
    )

    assert resp.uid == "1f0f2270-b297-4400-afa4-d9f56a1cb407"
    assert resp.name == "mycompoundtcp"

    # None arguments
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.service_applications.service_compound_tcp.set()


@responses.activate
def test_delete_service_compound_tcp(firewallManagement, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-service-compound-tcp",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.service_applications.service_compound_tcp.delete(
        uid="1f0f2270-b297-4400-afa4-d9f56a1cb407"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_services_compound_tcp(firewallManagement, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-services-compound-tcp",
        json=resp_from_to_objects,
        status=200,
    )

    resp = (
        firewallManagement.service_applications.service_compound_tcp.show_services_compound_tcp()
    )

    assert isinstance(resp.total, int)
