import pytest
import responses

from pycheckpoint_api.firewallManagement.exception import MandatoryFieldMissing


@responses.activate
def test_add_service_udp(firewallManagement, resp_service_udp):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-service-udp",
        json=resp_service_udp,
        status=200,
    )

    resp = firewallManagement.service_applications.service_udp.add(
        name="New_UDP_Service_1",
        port=5669,
        acccept_replies=True,
        keep_connections_open_after_policy_installation=False,
        session_timeout=0,
        match_for_any=True,
        sync_connections_on_cluster=True,
        override_default_settings=False,
        protocol="DNS_UDP",
        source_port=1234,
        tags=["t1"],
        use_default_session_timeout=True,
        aggressive_aging={"enable": True, "timeout": 360, "use-default-timeout": False},
    )

    assert resp.uid == "64a4c8d1-7fed-4320-9826-0570bbb4a5bd"
    assert resp.name == "New_UDP_Service_1"
    assert resp.port == "5669"


@responses.activate
def test_show_service_udp(firewallManagement, resp_service_udp):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-service-udp",
        json=resp_service_udp,
        status=200,
    )

    resp = firewallManagement.service_applications.service_udp.show(
        uid="64a4c8d1-7fed-4320-9826-0570bbb4a5bd"
    )

    assert resp.uid == "64a4c8d1-7fed-4320-9826-0570bbb4a5bd"
    assert resp.name == "New_UDP_Service_1"
    assert resp.port == "5669"


@responses.activate
def test_set_service_udp(firewallManagement, resp_service_udp):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-service-udp",
        json=resp_service_udp,
        status=200,
    )

    resp = firewallManagement.service_applications.service_udp.set(
        uid="64a4c8d1-7fed-4320-9826-0570bbb4a5bd",
        new_name="New_UDP_Service_1",
        ip_address="192.0.2.1",
        port=5669,
        acccept_replies=True,
        keep_connections_open_after_policy_installation=False,
        session_timeout=0,
        match_for_any=True,
        sync_connections_on_cluster=True,
        override_default_settings=False,
        protocol="DNS_UDP",
        source_port=1234,
        tags=["t1"],
        use_default_session_timeout=True,
        aggressive_aging={"enable": True, "timeout": 360, "use-default-timeout": False},
    )

    assert resp.uid == "64a4c8d1-7fed-4320-9826-0570bbb4a5bd"
    assert resp.name == "New_UDP_Service_1"
    assert resp.port == "5669"

    resp = firewallManagement.service_applications.service_udp.set(
        name="New_UDP_Service_1",
        ip_address="192.0.2.1",
    )

    assert resp.uid == "64a4c8d1-7fed-4320-9826-0570bbb4a5bd"
    assert resp.name == "New_UDP_Service_1"
    assert resp.port == "5669"

    # None arguments
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.service_applications.service_udp.set()


@responses.activate
def test_delete_service_udp(firewallManagement, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-service-udp",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.service_applications.service_udp.delete(
        uid="64a4c8d1-7fed-4320-9826-0570bbb4a5bd"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_services_udp(firewallManagement, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-services-udp",
        json=resp_from_to_objects,
        status=200,
    )

    resp = firewallManagement.service_applications.service_udp.show_services_udp()

    assert isinstance(resp.total, int)
