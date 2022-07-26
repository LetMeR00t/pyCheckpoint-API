import pytest
import responses

from pycheckpoint_api.management.exception import MandatoryFieldMissing


@responses.activate
def test_add_tacacs_group(management, resp_tacacs_group):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-tacacs-group",
        json=resp_tacacs_group,
        status=200,
    )

    resp = management.network_objects.tacacs_group.add(
        name="New tacacs_group 4", members=["tacacs7"], tags=["t1"]
    )

    assert resp.uid == "dd857ad5-a354-3991-cddc-58dc5ae69f65"
    assert resp.name == "New TACACS Group 3"


@responses.activate
def test_show_tacacs_group(management, resp_tacacs_group):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-tacacs-group",
        json=resp_tacacs_group,
        status=200,
    )

    resp = management.network_objects.tacacs_group.show(
        uid="dd857ad5-a354-3991-cddc-58dc5ae69f65"
    )

    assert resp.uid == "dd857ad5-a354-3991-cddc-58dc5ae69f65"
    assert resp.name == "New TACACS Group 3"


@responses.activate
def test_set_tacacs_group(management, resp_tacacs_group):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-tacacs-group",
        json=resp_tacacs_group,
        status=200,
    )

    resp = management.network_objects.tacacs_group.set(
        uid="dd857ad5-a354-3991-cddc-58dc5ae69f65",
        new_name="New TACACS Group 3",
        members=["tacacs7"],
        tags=["t1"],
    )

    assert resp.uid == "dd857ad5-a354-3991-cddc-58dc5ae69f65"
    assert resp.name == "New TACACS Group 3"

    resp = management.network_objects.tacacs_group.set(
        name="Old TACACS Group 3", new_name="New TACACS Group 3"
    )

    assert resp.uid == "dd857ad5-a354-3991-cddc-58dc5ae69f65"
    assert resp.name == "New TACACS Group 3"

    # Missing name or UID information
    with pytest.raises(MandatoryFieldMissing):
        management.network_objects.tacacs_group.set()


@responses.activate
def test_delete_tacacs_group(management, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-tacacs-group",
        json=resp_message_ok,
        status=200,
    )

    resp = management.network_objects.tacacs_group.delete(
        uid="dd857ad5-a354-3991-cddc-58dc5ae69f65"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_tacacs_groups(management, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-tacacs-groups",
        json=resp_from_to_objects,
        status=200,
    )

    resp = management.network_objects.tacacs_group.show_tacacs_groups()

    assert isinstance(resp.total, int)
