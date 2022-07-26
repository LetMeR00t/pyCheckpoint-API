import pytest
import responses

from pycheckpoint_api.management.exception import MandatoryFieldMissing


@responses.activate
def test_add_service_tcp(management, resp_service_tcp):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-service-tcp",
        json=resp_service_tcp,
        status=200,
    )

    resp = management.service_applications.service_tcp.add(
        name="New_TCP_Service_1",
        port=5669,
        keep_connections_open_after_policy_installation=False,
        session_timeout=0,
        match_for_any=True,
        sync_connections_on_cluster=True,
        override_default_settings=False,
        protocol="DNS_TCP",
        use_default_session_timeout=True,
        source_port=1234,
        aggressive_aging={"enable": True, "timeout": 360, "use-default-timeout": False},
        tags=["t1"],
    )

    assert resp.uid == "bee785c5-998b-4a45-80e8-3fa91181aba9"
    assert resp.name == "New_TCP_Service_1"
    assert resp.port == "5669"


@responses.activate
def test_show_service_tcp(management, resp_service_tcp):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-service-tcp",
        json=resp_service_tcp,
        status=200,
    )

    resp = management.service_applications.service_tcp.show(
        uid="bee785c5-998b-4a45-80e8-3fa91181aba9"
    )

    assert resp.uid == "bee785c5-998b-4a45-80e8-3fa91181aba9"
    assert resp.name == "New_TCP_Service_1"
    assert resp.port == "5669"


@responses.activate
def test_set_service_tcp(management, resp_service_tcp):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-service-tcp",
        json=resp_service_tcp,
        status=200,
    )

    resp = management.service_applications.service_tcp.set(
        uid="bee785c5-998b-4a45-80e8-3fa91181aba9",
        new_name="New_TCP_Service_1",
        ip_address="192.0.2.1",
        port=5669,
        keep_connections_open_after_policy_installation=False,
        session_timeout=0,
        match_for_any=True,
        sync_connections_on_cluster=True,
        override_default_settings=False,
        protocol="DNS_TCP",
        use_default_session_timeout=True,
        source_port=1234,
        aggressive_aging={"enable": True, "timeout": 360, "use-default-timeout": False},
        tags=["t1"],
    )

    assert resp.uid == "bee785c5-998b-4a45-80e8-3fa91181aba9"
    assert resp.name == "New_TCP_Service_1"
    assert resp.port == "5669"

    resp = management.service_applications.service_tcp.set(
        name="New_TCP_Service_1",
        ip_address="192.0.2.1",
    )

    assert resp.uid == "bee785c5-998b-4a45-80e8-3fa91181aba9"
    assert resp.name == "New_TCP_Service_1"
    assert resp.port == "5669"

    # None arguments
    with pytest.raises(MandatoryFieldMissing):
        management.service_applications.service_tcp.set()


@responses.activate
def test_delete_service_tcp(management, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-service-tcp",
        json=resp_message_ok,
        status=200,
    )

    resp = management.service_applications.service_tcp.delete(
        uid="bee785c5-998b-4a45-80e8-3fa91181aba9"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_services_tcp(management, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-services-tcp",
        json=resp_from_to_objects,
        status=200,
    )

    resp = management.service_applications.service_tcp.show_services_tcp()

    assert isinstance(resp.total, int)
