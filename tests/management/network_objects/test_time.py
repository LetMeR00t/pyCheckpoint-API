import pytest
import responses

from pycheckpoint_api.management.exception import MandatoryFieldMissing


@responses.activate
def test_add_time(management, resp_time):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-time",
        json=resp_time,
        status=200,
    )

    resp = management.network_objects.time.add(
        name="timeObject1",
        start_now="true",
        end={"date": "24-Nov-2014", "time": "21:22"},
        end_never=False,
        hours_ranges=[
            {"from": "00:00", "to": "00:00", "enabled": True, "index": 1},
            {"from": "00:00", "to": "00:00", "enabled": False, "index": 2},
        ],
        recurrence={
            "pattern": "Daily",
            "month": "Any",
            "weekdays": ["Sun", "Mon"],
            "days": ["1"],
        },
    )

    assert resp.uid == "aa785d6d-7785-aad5-36a3-ab2d74c966ee"
    assert resp.name == "timeObject1"
    assert resp.start_now is True

    resp = management.network_objects.time.add(
        name="timeObject1",
        start={"date": "24-Nov-2014", "time": "21:22"},
        end_never=True,
        hours_ranges=[
            {"from": "00:00", "to": "00:00", "enabled": True, "index": 1},
            {"from": "00:00", "to": "00:00", "enabled": False, "index": 2},
        ],
        recurrence={
            "pattern": "Daily",
            "month": "Any",
            "weekdays": ["Sun", "Mon"],
            "days": ["1"],
        },
        tags="t1",
    )

    assert resp.uid == "aa785d6d-7785-aad5-36a3-ab2d74c966ee"
    assert resp.name == "timeObject1"
    assert resp.start_now is True


@responses.activate
def test_show_time(management, resp_time):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-time",
        json=resp_time,
        status=200,
    )

    resp = management.network_objects.time.show(
        uid="d5e8d56f-2d77-4824-a5d2-c4a7885dd4a7"
    )

    assert resp.uid == "aa785d6d-7785-aad5-36a3-ab2d74c966ee"
    assert resp.name == "timeObject1"
    assert resp.start_now is True


@responses.activate
def test_set_time(management, resp_time):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-time",
        json=resp_time,
        status=200,
    )

    resp = management.network_objects.time.set(
        uid="d5e8d56f-2d77-4824-a5d2-c4a7885dd4a7",
        new_name="timeObject1",
        start_now=True,
        end={"date": "24-Nov-2014", "time": "21:22"},
        end_never=False,
        hours_ranges=[
            {"from": "00:00", "to": "00:00", "enabled": True, "index": 1},
            {"from": "00:00", "to": "00:00", "enabled": False, "index": 2},
        ],
        recurrence={
            "pattern": "Daily",
            "month": "Any",
            "weekdays": ["Sun", "Mon"],
            "days": ["1"],
        },
    )

    assert resp.uid == "aa785d6d-7785-aad5-36a3-ab2d74c966ee"
    assert resp.name == "timeObject1"
    assert resp.start_now is True

    resp = management.network_objects.time.set(
        name="timeObject1 Old",
        new_name="timeObject1",
        start={"date": "24-Nov-2014", "time": "21:22"},
        end_never=True,
        hours_ranges=[
            {"from": "00:00", "to": "00:00", "enabled": True, "index": 1},
            {"from": "00:00", "to": "00:00", "enabled": False, "index": 2},
        ],
        recurrence={
            "pattern": "Daily",
            "month": "Any",
            "weekdays": ["Sun", "Mon"],
            "days": ["1"],
        },
        tags="t1",
    )

    assert resp.uid == "aa785d6d-7785-aad5-36a3-ab2d74c966ee"
    assert resp.name == "timeObject1"
    assert resp.start_now is True

    # Missing name or UID information
    with pytest.raises(MandatoryFieldMissing):
        management.network_objects.time.set()


@responses.activate
def test_delete_time(management, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-time",
        json=resp_message_ok,
        status=200,
    )

    resp = management.network_objects.time.delete(
        uid="d5e8d56f-2d77-4824-a5d2-c4a7885dd4a7"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_times(management, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-times",
        json=resp_from_to_objects,
        status=200,
    )

    resp = management.network_objects.time.show_times()

    assert isinstance(resp.total, int)
