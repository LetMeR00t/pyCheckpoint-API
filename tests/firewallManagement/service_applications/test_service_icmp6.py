import pytest
import responses

from pycheckpoint_api.firewallManagement.exception import MandatoryFieldMissing


@responses.activate
def test_add_service_icmp6(firewallManagement, resp_service_icmp6):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-service-icmp6",
        json=resp_service_icmp6,
        status=200,
    )

    resp = firewallManagement.service_applications.service_icmp6.add(
        name="Icmp2",
        port=5669,
        keep_connections_open_after_policy_installation=False,
        session_timeout=0,
        match_for_any=True,
        sync_connections_on_cluster=True,
        aggressive_aging={"enable": True, "timeout": 360, "use-default-timeout": False},
        tags=["t1"],
    )

    assert resp.uid == "d9dcb753-1aa7-4e65-b5ff-b4878f8b3890"
    assert resp.name == "Icmp2"
    assert resp.icmp_type == 5
    assert resp.icmp_code == 7


@responses.activate
def test_show_service_icmp6(firewallManagement, resp_service_icmp6):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-service-icmp6",
        json=resp_service_icmp6,
        status=200,
    )

    resp = firewallManagement.service_applications.service_icmp6.show(
        uid="d9dcb753-1aa7-4e65-b5ff-b4878f8b3890"
    )

    assert resp.uid == "d9dcb753-1aa7-4e65-b5ff-b4878f8b3890"
    assert resp.name == "Icmp2"
    assert resp.icmp_type == 5
    assert resp.icmp_code == 7


@responses.activate
def test_set_service_icmp6(firewallManagement, resp_service_icmp6):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-service-icmp6",
        json=resp_service_icmp6,
        status=200,
    )

    resp = firewallManagement.service_applications.service_icmp6.set(
        uid="d9dcb753-1aa7-4e65-b5ff-b4878f8b3890",
        new_name="Icmp2",
        ip_address="192.0.2.1",
        tags=["t1"],
        keep_connections_open_after_policy_installation=True,
    )

    assert resp.uid == "d9dcb753-1aa7-4e65-b5ff-b4878f8b3890"
    assert resp.name == "Icmp2"
    assert resp.icmp_type == 5
    assert resp.icmp_code == 7

    resp = firewallManagement.service_applications.service_icmp6.set(
        name="Icmp2", ip_address="192.0.2.1"
    )

    assert resp.uid == "d9dcb753-1aa7-4e65-b5ff-b4878f8b3890"
    assert resp.name == "Icmp2"
    assert resp.icmp_type == 5
    assert resp.icmp_code == 7

    # None arguments
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.service_applications.service_icmp6.set()


@responses.activate
def test_delete_service_icmp6(firewallManagement, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-service-icmp6",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.service_applications.service_icmp6.delete(
        uid="d9dcb753-1aa7-4e65-b5ff-b4878f8b3890"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_services_icmp6(firewallManagement, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-services-icmp6",
        json=resp_from_to_objects,
        status=200,
    )

    resp = firewallManagement.service_applications.service_icmp6.show_services_icmp6()

    assert isinstance(resp.total, int)
