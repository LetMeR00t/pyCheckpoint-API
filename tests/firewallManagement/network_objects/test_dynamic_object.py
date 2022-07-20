import pytest
import responses

from pycheckpoint_api.firewallManagement.exception import MandatoryFieldMissing


@responses.activate
def test_add_dynamic_object(firewallManagement, resp_dynamic_object):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-dynamic-object",
        json=resp_dynamic_object,
        status=200,
    )

    resp = firewallManagement.network_objects.dynamic_object.add(
        name="Dynamic_Object_1", comments="My Dynamic Object 1", tags=["t1"]
    )

    assert resp.uid == "c5a7f50c-a951-45be-8b82-48441c9f48de"
    assert resp.name == "Dynamic_Object_1"


@responses.activate
def test_show_dynamic_object(firewallManagement, resp_dynamic_object):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-dynamic-object",
        json=resp_dynamic_object,
        status=200,
    )

    resp = firewallManagement.network_objects.dynamic_object.show(
        uid="c5a7f50c-a951-45be-8b82-48441c9f48de"
    )

    assert resp.uid == "c5a7f50c-a951-45be-8b82-48441c9f48de"
    assert resp.name == "Dynamic_Object_1"


@responses.activate
def test_set_dynamic_object(firewallManagement, resp_dynamic_object):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-dynamic-object",
        json=resp_dynamic_object,
        status=200,
    )

    resp = firewallManagement.network_objects.dynamic_object.set(
        uid="c5a7f50c-a951-45be-8b82-48441c9f48de",
        new_name="Dynamic_Object_1",
        tags=["t1"],
    )

    assert resp.uid == "c5a7f50c-a951-45be-8b82-48441c9f48de"
    assert resp.name == "Dynamic_Object_1"

    resp = firewallManagement.network_objects.dynamic_object.set(
        name="Old Dynamic_Object_1", new_name="Dynamic_Object_1"
    )

    assert resp.uid == "c5a7f50c-a951-45be-8b82-48441c9f48de"
    assert resp.name == "Dynamic_Object_1"

    # Missing name or UID information
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.network_objects.dynamic_object.set()


@responses.activate
def test_delete_dynamic_object(firewallManagement, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-dynamic-object",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.network_objects.dynamic_object.delete(
        uid="c5a7f50c-a951-45be-8b82-48441c9f48de"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_dynamic_objects(firewallManagement, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-dynamic-objects",
        json=resp_from_to_objects,
        status=200,
    )

    resp = firewallManagement.network_objects.dynamic_object.show_dynamic_objects()

    assert isinstance(resp.total, int)
