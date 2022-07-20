import pytest
import responses

from pycheckpoint_api.firewallManagement.exception import MandatoryFieldMissing


@responses.activate
def test_add_time_group(firewallManagement, resp_time_group):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-time-group",
        json=resp_time_group,
        status=200,
    )

    resp = firewallManagement.network_objects.time_group.add(
        name="New Group 4", members=[], tags=["t1"]
    )

    assert resp.uid == "d5878541-abbd-ad58-d23a-01a12352abc6"
    assert resp.name == "New Time Group"


@responses.activate
def test_show_time_group(firewallManagement, resp_time_group):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-time-group",
        json=resp_time_group,
        status=200,
    )

    resp = firewallManagement.network_objects.time_group.show(
        uid="d5878541-abbd-ad58-d23a-01a12352abc6"
    )

    assert resp.uid == "d5878541-abbd-ad58-d23a-01a12352abc6"
    assert resp.name == "New Time Group"


@responses.activate
def test_set_time_group(firewallManagement, resp_time_group):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-time-group",
        json=resp_time_group,
        status=200,
    )

    resp = firewallManagement.network_objects.time_group.set(
        uid="d5878541-abbd-ad58-d23a-01a12352abc6",
        new_name="New Time Group",
        members=[],
        tags=["t1"],
    )

    assert resp.uid == "d5878541-abbd-ad58-d23a-01a12352abc6"
    assert resp.name == "New Time Group"

    resp = firewallManagement.network_objects.time_group.set(
        name="Old Time Group",
        new_name="New Time Group",
    )

    assert resp.uid == "d5878541-abbd-ad58-d23a-01a12352abc6"
    assert resp.name == "New Time Group"

    # Missing name or UID information
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.network_objects.time_group.set()


@responses.activate
def test_delete_time_group(firewallManagement, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-time-group",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.network_objects.time_group.delete(
        uid="d5878541-abbd-ad58-d23a-01a12352abc6"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_time_groups(firewallManagement, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-time-groups",
        json=resp_from_to_objects,
        status=200,
    )

    resp = firewallManagement.network_objects.time_group.show_time_groups()

    assert isinstance(resp.total, int)
