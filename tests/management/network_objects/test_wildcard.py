import pytest
import responses

from pycheckpoint_api.management.exception import MandatoryFieldMissing


@responses.activate
def test_add_wildcard(management, resp_wildcard_ipv4, resp_wildcard_ipv6):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-wildcard",
        json=resp_wildcard_ipv4,
        status=200,
    )

    resp = management.network_objects.wildcard.add(
        name="New Wildcard 4", ip_address="192.168.2.1", groups=[], tags=["t1"]
    )

    assert resp.uid == "d8a5e4dd-2a93-4847-aaa8-d5d33a695da5"
    assert resp.name == "New Wildcard 4"
    assert resp.ipv4_address == "192.168.2.1"
    assert resp.ipv4_mask_wildcard == "0.0.0.128"

    resp = management.network_objects.wildcard.add(
        name="New Wildcard 4",
        ipv4_address="192.168.2.1",
        ipv4_mask_wildcard="0.0.128.128",
    )

    assert resp.uid == "d8a5e4dd-2a93-4847-aaa8-d5d33a695da5"
    assert resp.name == "New Wildcard 4"
    assert resp.ipv4_address == "192.168.2.1"
    assert resp.ipv4_mask_wildcard == "0.0.0.128"

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-wildcard",
        json=resp_wildcard_ipv6,
        status=200,
    )

    resp = management.network_objects.wildcard.add(
        name="New Wildcard 6",
        ipv6_address="2001:db8::",
        ipv6_mask_wildcard="64",
    )

    assert resp.uid == "d8a5e4dd-2a93-4847-aaa8-d5d33a695da5"
    assert resp.name == "New Wildcard 6"
    assert resp.ipv6_address == "2001:db8::"
    assert resp.ipv6_mask_wildcard == "64"


@responses.activate
def test_show_wildcard(management, resp_wildcard_ipv4):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-wildcard",
        json=resp_wildcard_ipv4,
        status=200,
    )

    resp = management.network_objects.wildcard.show(
        uid="9423d36f-2d66-4754-b9e2-e7f4493756d4"
    )

    assert resp.uid == "d8a5e4dd-2a93-4847-aaa8-d5d33a695da5"
    assert resp.name == "New Wildcard 4"
    assert resp.ipv4_address == "192.168.2.1"
    assert resp.ipv4_mask_wildcard == "0.0.0.128"


@responses.activate
def test_set_wildcard(management, resp_wildcard_ipv4, resp_wildcard_ipv6):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-wildcard",
        json=resp_wildcard_ipv4,
        status=200,
    )

    resp = management.network_objects.wildcard.set(
        uid="d8a5e4dd-2a93-4847-aaa8-d5d33a695da5",
        new_name="New Wildcard 4",
        groups=[],
        tags=["t1"],
    )

    assert resp.uid == "d8a5e4dd-2a93-4847-aaa8-d5d33a695da5"
    assert resp.name == "New Wildcard 4"
    assert resp.ipv4_address == "192.168.2.1"
    assert resp.ipv4_mask_wildcard == "0.0.0.128"

    resp = management.network_objects.wildcard.set(
        name="New Wildcard 4",
        ipv4_address="192.168.2.1",
        ipv4_mask_wildcard="0.0.128.128",
    )

    assert resp.uid == "d8a5e4dd-2a93-4847-aaa8-d5d33a695da5"
    assert resp.name == "New Wildcard 4"
    assert resp.ipv4_address == "192.168.2.1"
    assert resp.ipv4_mask_wildcard == "0.0.0.128"

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-wildcard",
        json=resp_wildcard_ipv6,
        status=200,
    )

    resp = management.network_objects.wildcard.set(
        name="New Wildcard 6",
        ipv6_address="2001:db8::",
        ipv6_mask_wildcard="64",
    )

    assert resp.uid == "d8a5e4dd-2a93-4847-aaa8-d5d33a695da5"
    assert resp.name == "New Wildcard 6"
    assert resp.ipv6_address == "2001:db8::"
    assert resp.ipv6_mask_wildcard == "64"

    # Missing name or UID information
    with pytest.raises(MandatoryFieldMissing):
        management.network_objects.wildcard.set()


@responses.activate
def test_delete_wildcard(management, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-wildcard",
        json=resp_message_ok,
        status=200,
    )

    resp = management.network_objects.wildcard.delete(
        uid="d8a5e4dd-2a93-4847-aaa8-d5d33a695da5"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_wildcards(management, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-wildcards",
        json=resp_from_to_objects,
        status=200,
    )

    resp = management.network_objects.wildcard.show_wildcards()

    assert isinstance(resp.total, int)
