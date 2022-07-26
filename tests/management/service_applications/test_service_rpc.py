import pytest
import responses

from pycheckpoint_api.management.exception import MandatoryFieldMissing


@responses.activate
def test_add_service_rpc(management, resp_service_rpc):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-service-rpc",
        json=resp_service_rpc,
        status=200,
    )

    resp = management.service_applications.service_rpc.add(
        name="New_RPC_Service_2",
        program_number="5669",
        keep_connections_open_after_policy_installation=False,
        tags=["t1"],
    )

    assert resp.uid == "66333250-0680-46c3-a894-ebe1fef657f4"
    assert resp.name == "New_RPC_Service_2"


@responses.activate
def test_show_service_rpc(management, resp_service_rpc):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-service-rpc",
        json=resp_service_rpc,
        status=200,
    )

    resp = management.service_applications.service_rpc.show(
        uid="66333250-0680-46c3-a894-ebe1fef657f4"
    )

    assert resp.uid == "66333250-0680-46c3-a894-ebe1fef657f4"
    assert resp.name == "New_RPC_Service_2"


@responses.activate
def test_set_service_rpc(management, resp_service_rpc):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-service-rpc",
        json=resp_service_rpc,
        status=200,
    )

    resp = management.service_applications.service_rpc.set(
        uid="66333250-0680-46c3-a894-ebe1fef657f4",
        new_name="New_RPC_Service_2",
        program_number="5669",
        keep_connections_open_after_policy_installation=False,
        tags=["t1"],
    )

    assert resp.uid == "66333250-0680-46c3-a894-ebe1fef657f4"
    assert resp.name == "New_RPC_Service_2"

    resp = management.service_applications.service_rpc.set(
        name="New_RPC_Service_2",
        interface_uuid="97aeb460-9aea-11d5-bd16-0090272ccb30",
    )

    assert resp.uid == "66333250-0680-46c3-a894-ebe1fef657f4"
    assert resp.name == "New_RPC_Service_2"

    # None arguments
    with pytest.raises(MandatoryFieldMissing):
        management.service_applications.service_rpc.set()


@responses.activate
def test_delete_service_rpc(management, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-service-rpc",
        json=resp_message_ok,
        status=200,
    )

    resp = management.service_applications.service_rpc.delete(
        uid="66333250-0680-46c3-a894-ebe1fef657f4"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_services_rpc(management, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-services-rpc",
        json=resp_from_to_objects,
        status=200,
    )

    resp = management.service_applications.service_rpc.show_services_rpc()

    assert isinstance(resp.total, int)
