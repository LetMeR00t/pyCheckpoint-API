import pytest
import responses

from pycheckpoint_api.management.exception import MandatoryFieldMissing


@responses.activate
def test_add_security_zone(management, resp_security_zone):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-security-zone",
        json=resp_security_zone,
        status=200,
    )

    resp = management.network_objects.security_zone.add(name="SZone1", tags=["t1"])

    assert resp.uid == "cecd7d2e-c5bb-40d2-bd34-7afe8c37a062"
    assert resp.name == "SZone1"


@responses.activate
def test_show_security_zone(management, resp_security_zone):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-security-zone",
        json=resp_security_zone,
        status=200,
    )

    resp = management.network_objects.security_zone.show(
        uid="cecd7d2e-c5bb-40d2-bd34-7afe8c37a062"
    )

    assert resp.uid == "cecd7d2e-c5bb-40d2-bd34-7afe8c37a062"
    assert resp.name == "SZone1"


@responses.activate
def test_set_security_zone(management, resp_security_zone):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-security-zone",
        json=resp_security_zone,
        status=200,
    )

    resp = management.network_objects.security_zone.set(
        uid="cecd7d2e-c5bb-40d2-bd34-7afe8c37a062", new_name="SZone1", tags=["t1"]
    )

    assert resp.uid == "cecd7d2e-c5bb-40d2-bd34-7afe8c37a062"
    assert resp.name == "SZone1"

    resp = management.network_objects.security_zone.set(
        name="Old SZone1", new_name="SZone1"
    )

    assert resp.uid == "cecd7d2e-c5bb-40d2-bd34-7afe8c37a062"
    assert resp.name == "SZone1"

    # Missing name or UID information
    with pytest.raises(MandatoryFieldMissing):
        management.network_objects.security_zone.set()


@responses.activate
def test_delete_security_zone(management, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-security-zone",
        json=resp_message_ok,
        status=200,
    )

    resp = management.network_objects.security_zone.delete(
        uid="cecd7d2e-c5bb-40d2-bd34-7afe8c37a062"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_security_zones(management, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-security-zones",
        json=resp_from_to_objects,
        status=200,
    )

    resp = management.network_objects.security_zone.show_security_zones()

    assert isinstance(resp.total, int)
