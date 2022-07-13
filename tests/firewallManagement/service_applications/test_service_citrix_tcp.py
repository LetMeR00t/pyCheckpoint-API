import pytest
import responses

from pycheckpoint_api.firewallManagement.exception import MandatoryFieldMissing


@responses.activate
def test_add_service_citrix_tcp(firewallManagement, resp_service_citrix_tcp):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-service-citrix-tcp",
        json=resp_service_citrix_tcp,
        status=200,
    )

    resp = firewallManagement.service_applications.service_citrix_tcp.add(
        name="mycitrixtcp",
        application="My Citrix Application",
        tags=["t1"],
    )

    assert resp.uid == "3464de87-7e4c-4dde-8b67-89cf2f46c32c"
    assert resp.name == "mycitrixtcp"

    # None arguments
    with pytest.raises(TypeError):
        firewallManagement.service_applications.service_citrix_tcp.add()


@responses.activate
def test_show_service_citrix_tcp(firewallManagement, resp_service_citrix_tcp):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-service-citrix-tcp",
        json=resp_service_citrix_tcp,
        status=200,
    )

    resp = firewallManagement.service_applications.service_citrix_tcp.show(
        uid="3464de87-7e4c-4dde-8b67-89cf2f46c32c"
    )

    assert resp.uid == "3464de87-7e4c-4dde-8b67-89cf2f46c32c"
    assert resp.name == "mycitrixtcp"


@responses.activate
def test_set_service_citrix_tcp(firewallManagement, resp_service_citrix_tcp):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-service-citrix-tcp",
        json=resp_service_citrix_tcp,
        status=200,
    )

    resp = firewallManagement.service_applications.service_citrix_tcp.set(
        uid="3464de87-7e4c-4dde-8b67-89cf2f46c32c",
        new_name="mycitrixtcp",
        application="My Citrix Application",
        tags=["t1"],
    )

    assert resp.uid == "3464de87-7e4c-4dde-8b67-89cf2f46c32c"
    assert resp.name == "mycitrixtcp"

    resp = firewallManagement.service_applications.service_citrix_tcp.set(
        name="Old Name Group 3", new_name="mycitrixtcp"
    )

    assert resp.uid == "3464de87-7e4c-4dde-8b67-89cf2f46c32c"
    assert resp.name == "mycitrixtcp"

    # None arguments
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.service_applications.service_citrix_tcp.set()


@responses.activate
def test_delete_service_citrix_tcp(firewallManagement, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-service-citrix-tcp",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.service_applications.service_citrix_tcp.delete(
        uid="3464de87-7e4c-4dde-8b67-89cf2f46c32c"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_services_citrix_tcp(firewallManagement, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-services-citrix-tcp",
        json=resp_from_to_objects,
        status=200,
    )

    resp = (
        firewallManagement.service_applications.service_citrix_tcp.show_services_citrix_tcp()
    )

    assert isinstance(resp.total, int)
