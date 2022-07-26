import pytest
import responses

from pycheckpoint_api.management.exception import MandatoryFieldMissing


@responses.activate
def test_add_gsn_handover_group(management, resp_gsn_handover_group):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-gsn-handover-group",
        json=resp_gsn_handover_group,
        status=200,
    )

    resp = management.network_objects.gsn_handover_group.add(
        name="gsnhandovergroup",
        enforce_gtp=True,
        gtp_rate=2048,
        members="All_Internet",
        tags="t1",
    )

    assert resp.uid == "f140a9d1-4167-456a-931d-abdaa4c8aa7e"
    assert resp.name == "gsnhandovergroup"


@responses.activate
def test_show_gsn_handover_group(management, resp_gsn_handover_group):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-gsn-handover-group",
        json=resp_gsn_handover_group,
        status=200,
    )

    resp = management.network_objects.gsn_handover_group.show(
        uid="f140a9d1-4167-456a-931d-abdaa4c8aa7e"
    )

    assert resp.uid == "f140a9d1-4167-456a-931d-abdaa4c8aa7e"
    assert resp.name == "gsnhandovergroup"

    resp = management.network_objects.gsn_handover_group.show(name="gsnhandovergroup")

    assert resp.uid == "f140a9d1-4167-456a-931d-abdaa4c8aa7e"
    assert resp.name == "gsnhandovergroup"


@responses.activate
def test_set_gsn_handover_group(management, resp_gsn_handover_group):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-gsn-handover-group",
        json=resp_gsn_handover_group,
        status=200,
    )

    resp = management.network_objects.gsn_handover_group.set(
        uid="f140a9d1-4167-456a-931d-abdaa4c8aa7e",
        new_name="gsnhandovergroup",
        enforce_gtp=True,
        gtp_rate=2048,
        members="All_Internet",
        tags="t1",
    )

    assert resp.uid == "f140a9d1-4167-456a-931d-abdaa4c8aa7e"
    assert resp.name == "gsnhandovergroup"

    resp = management.network_objects.gsn_handover_group.set(
        name="gsnhandovergroup Old",
        new_name="gsnhandovergroup",
    )

    assert resp.uid == "f140a9d1-4167-456a-931d-abdaa4c8aa7e"
    assert resp.name == "gsnhandovergroup"

    # Missing name or UID information
    with pytest.raises(MandatoryFieldMissing):
        management.network_objects.gsn_handover_group.set()


@responses.activate
def test_delete_gsn_handover_group(management, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-gsn-handover-group",
        json=resp_message_ok,
        status=200,
    )

    resp = management.network_objects.gsn_handover_group.delete(
        uid="f140a9d1-4167-456a-931d-abdaa4c8aa7e"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_gsn_handover_groups(management, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-gsn-handover-groups",
        json=resp_from_to_objects,
        status=200,
    )

    resp = management.network_objects.gsn_handover_group.show_gsn_handover_groups()

    assert isinstance(resp.total, int)
