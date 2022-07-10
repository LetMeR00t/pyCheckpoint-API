import responses
import pytest

from pycheckpoint_api.firewallManagement.exception import MandatoryFieldMissing
from pycheckpoint_api.models import Color


@responses.activate
def test_add_address_range_ipv4(
    firewallManagement, resp_address_range_ipv4, resp_address_range_ipv6
):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-address-range",
        json=resp_address_range_ipv4,
        status=200,
    )

    resp = firewallManagement.network_objects.address_range.add(
        name="New Address Range 1",
        ip_address_first="192.0.2.1",
        ip_address_last="192.0.2.10",
        nat_settings={"auto-rule": False},
        tags=["t1"],
    )

    assert resp.uid == "196e93a9-b90b-4ab1-baa6-124e7289aa20"
    assert resp.name == "New Address Range 1"
    assert resp.ipv4_address_first == "192.0.2.1"
    assert resp.ipv4_address_last == "192.0.2.10"

    resp = firewallManagement.network_objects.address_range.add(
        name="New Address Range 1",
        ipv4_address_first="192.0.2.1",
        ipv4_address_last="192.0.2.10",
    )

    assert resp.uid == "196e93a9-b90b-4ab1-baa6-124e7289aa20"
    assert resp.name == "New Address Range 1"
    assert resp.ipv4_address_first == "192.0.2.1"
    assert resp.ipv4_address_last == "192.0.2.10"

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-address-range",
        json=resp_address_range_ipv6,
        status=200,
    )

    resp = firewallManagement.network_objects.address_range.add(
        name="New Address Range 1",
        ipv6_address_first="2001:db8::",
        ipv6_address_last="2001:db8:0000:0000:0000:0000:0000:000f",
    )

    assert resp.uid == "196e93a9-b90b-4ab1-baa6-124e7289aa20"
    assert resp.name == "New Address Range 1"
    assert resp.ipv6_address_first == "2001:db8::"
    assert resp.ipv6_address_last == "2001:db8:0000:0000:0000:0000:0000:000f"

    # None IP address information
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.network_objects.address_range.add(name="New Address Range 1")

    # Missing IP last address information
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.network_objects.address_range.add(
            name="New Address Range 1", ipv6_address_first="2001:db8::"
        )


@responses.activate
def test_show_address_range(firewallManagement, resp_address_range_ipv4):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-address-range",
        json=resp_address_range_ipv4,
        status=200,
    )

    resp = firewallManagement.network_objects.address_range.show(
        uid="196e93a9-b90b-4ab1-baa6-124e7289aa20"
    )

    assert resp.uid == "196e93a9-b90b-4ab1-baa6-124e7289aa20"
    assert resp.name == "New Address Range 1"
    assert resp.ipv4_address_first == "192.0.2.1"
    assert resp.ipv4_address_last == "192.0.2.10"


@responses.activate
def test_set_address_range(
    firewallManagement, resp_address_range_ipv4, resp_address_range_ipv6
):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-address-range",
        json=resp_address_range_ipv4,
        status=200,
    )

    resp = firewallManagement.network_objects.address_range.set(
        uid="196e93a9-b90b-4ab1-baa6-124e7289aa20",
        new_name="New Address Range 1",
        color=Color.GREEN,
        ip_address_first="192.0.2.1",
        ip_address_last="192.0.2.10",
        groups="New Group 1",
        nat_settings={"auto-rule": False},
        tags=["t1"],
    )

    assert resp.uid == "196e93a9-b90b-4ab1-baa6-124e7289aa20"
    assert resp.name == "New Address Range 1"
    assert resp.ipv4_address_first == "192.0.2.1"
    assert resp.ipv4_address_last == "192.0.2.10"

    resp = firewallManagement.network_objects.address_range.set(
        name="New Address Range 1",
        ipv4_address_first="192.0.2.1",
        ipv4_address_last="192.0.2.10",
    )

    assert resp.uid == "196e93a9-b90b-4ab1-baa6-124e7289aa20"
    assert resp.name == "New Address Range 1"
    assert resp.ipv4_address_first == "192.0.2.1"
    assert resp.ipv4_address_last == "192.0.2.10"

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-address-range",
        json=resp_address_range_ipv6,
        status=200,
    )

    resp = firewallManagement.network_objects.address_range.set(
        uid="196e93a9-b90b-4ab1-baa6-124e7289aa20",
        ipv6_address_first="2001:db8::",
        ipv6_address_last="2001:db8:0000:0000:0000:0000:0000:000f",
    )

    assert resp.uid == "196e93a9-b90b-4ab1-baa6-124e7289aa20"
    assert resp.name == "New Address Range 1"
    assert resp.ipv6_address_first == "2001:db8::"
    assert resp.ipv6_address_last == "2001:db8:0000:0000:0000:0000:0000:000f"

    # None IP address information
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.network_objects.address_range.set()


@responses.activate
def test_delete_host(firewallManagement, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-address-range",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.network_objects.address_range.delete(
        uid="196e93a9-b90b-4ab1-baa6-124e7289aa20"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_address_ranges(firewallManagement, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-address-ranges",
        json=resp_from_to_objects,
        status=200,
    )

    resp = firewallManagement.network_objects.address_range.show_address_ranges()

    assert isinstance(resp.total, int)
