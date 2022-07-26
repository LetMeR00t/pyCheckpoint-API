import pytest
import responses

from pycheckpoint_api.management.exception import MandatoryFieldMissing


@responses.activate
def test_add_service_icmp(management, resp_service_icmp):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-service-icmp",
        json=resp_service_icmp,
        status=200,
    )

    resp = management.service_applications.service_icmp.add(
        name="Icmp1",
        port=5669,
        keep_connections_open_after_policy_installation=False,
        session_timeout=0,
        match_for_any=True,
        sync_connections_on_cluster=True,
        aggressive_aging={"enable": True, "timeout": 360, "use-default-timeout": False},
        tags=["t1"],
    )

    assert resp.uid == "22c8faba-3a24-4e99-ae6f-e798014facc2"
    assert resp.name == "Icmp1"
    assert resp.icmp_type == 5
    assert resp.icmp_code == 7


@responses.activate
def test_show_service_icmp(management, resp_service_icmp):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-service-icmp",
        json=resp_service_icmp,
        status=200,
    )

    resp = management.service_applications.service_icmp.show(
        uid="22c8faba-3a24-4e99-ae6f-e798014facc2"
    )

    assert resp.uid == "22c8faba-3a24-4e99-ae6f-e798014facc2"
    assert resp.name == "Icmp1"
    assert resp.icmp_type == 5
    assert resp.icmp_code == 7


@responses.activate
def test_set_service_icmp(management, resp_service_icmp):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-service-icmp",
        json=resp_service_icmp,
        status=200,
    )

    resp = management.service_applications.service_icmp.set(
        uid="22c8faba-3a24-4e99-ae6f-e798014facc2",
        new_name="Icmp1",
        ip_address="192.0.2.1",
        keep_connections_open_after_policy_installation=True,
        tags=["t1"],
    )

    assert resp.uid == "22c8faba-3a24-4e99-ae6f-e798014facc2"
    assert resp.name == "Icmp1"
    assert resp.icmp_type == 5
    assert resp.icmp_code == 7

    resp = management.service_applications.service_icmp.set(
        name="Icmp1", ip_address="192.0.2.1"
    )

    assert resp.uid == "22c8faba-3a24-4e99-ae6f-e798014facc2"
    assert resp.name == "Icmp1"
    assert resp.icmp_type == 5
    assert resp.icmp_code == 7

    # None arguments
    with pytest.raises(MandatoryFieldMissing):
        management.service_applications.service_icmp.set()


@responses.activate
def test_delete_service_icmp(management, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-service-icmp",
        json=resp_message_ok,
        status=200,
    )

    resp = management.service_applications.service_icmp.delete(
        uid="22c8faba-3a24-4e99-ae6f-e798014facc2"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_services_icmp(management, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-services-icmp",
        json=resp_from_to_objects,
        status=200,
    )

    resp = management.service_applications.service_icmp.show_services_icmp()

    assert isinstance(resp.total, int)
