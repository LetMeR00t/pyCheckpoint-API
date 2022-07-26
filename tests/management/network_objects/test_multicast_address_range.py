import pytest
import responses

from pycheckpoint_api.management.exception import MandatoryFieldMissing


@responses.activate
def test_add_multicast_address_range(
    management,
    resp_multicast_address_range_single_ip,
    resp_multicast_address_range_ipv4,
    resp_multicast_address_range_ipv6,
):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-multicast-address-range",
        json=resp_multicast_address_range_single_ip,
        status=200,
    )

    resp = management.network_objects.multicast_address_range.add(
        name="New Multicast Address Range",
        ip_address="224.0.0.5",
        tags=["t1"],
    )

    assert resp.uid == "faff3fdf-01b9-4c58-97dc-176c409b5bc1"
    assert resp.name == "New Multicast Address Range"
    assert resp.ipv4_address_first == "224.0.0.5"
    assert resp.ipv4_address_last == "224.0.0.5"

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-multicast-address-range",
        json=resp_multicast_address_range_ipv4,
        status=200,
    )

    resp = management.network_objects.multicast_address_range.add(
        name="New Multicast Address Range",
        ip_address_first="224.0.0.1",
        ip_address_last="224.0.0.4",
        tags=["t1"],
    )

    assert resp.uid == "faff3fdf-01b9-4c58-97dc-176c409b5bc1"
    assert resp.name == "New Multicast Address Range"
    assert resp.ipv4_address_first == "224.0.0.1"
    assert resp.ipv4_address_last == "224.0.0.4"

    resp = management.network_objects.multicast_address_range.add(
        name="New Multicast Address Range",
        ipv4_address_first="224.0.0.1",
        ipv4_address_last="224.0.0.4",
        tags=["t1"],
    )

    assert resp.uid == "faff3fdf-01b9-4c58-97dc-176c409b5bc1"
    assert resp.name == "New Multicast Address Range"
    assert resp.ipv4_address_first == "224.0.0.1"
    assert resp.ipv4_address_last == "224.0.0.4"

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-multicast-address-range",
        json=resp_multicast_address_range_ipv6,
        status=200,
    )

    resp = management.network_objects.multicast_address_range.add(
        name="New Multicast Address Range",
        ipv6_address_first="2001:db8:0000:0000:0000:0000:0000:0002",
        ipv6_address_last="2001:db8:0000:0000:0000:0000:0000:0004",
    )

    assert resp.uid == "faff3fdf-01b9-4c58-97dc-176c409b5bc1"
    assert resp.name == "New Multicast Address Range"
    assert resp.ipv6_address_first == "2001:db8:0000:0000:0000:0000:0000:0002"
    assert resp.ipv6_address_last == "2001:db8:0000:0000:0000:0000:0000:0004"


@responses.activate
def test_show_multicast_address_range(management, resp_multicast_address_range_ipv4):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-multicast-address-range",
        json=resp_multicast_address_range_ipv4,
        status=200,
    )

    resp = management.network_objects.multicast_address_range.show(
        uid="196e93a9-b90b-4ab1-baa6-124e7289aa20"
    )

    assert resp.uid == "faff3fdf-01b9-4c58-97dc-176c409b5bc1"
    assert resp.name == "New Multicast Address Range"
    assert resp.ipv4_address_first == "224.0.0.1"
    assert resp.ipv4_address_last == "224.0.0.4"


@responses.activate
def test_set_multicast_address_range(
    management,
    resp_multicast_address_range_single_ip,
    resp_multicast_address_range_ipv4,
    resp_multicast_address_range_ipv6,
):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-multicast-address-range",
        json=resp_multicast_address_range_single_ip,
        status=200,
    )

    resp = management.network_objects.multicast_address_range.set(
        uid="faff3fdf-01b9-4c58-97dc-176c409b5bc1",
        new_name="New Multicast Address Range",
        ip_address="224.0.0.5",
        tags=["t1"],
    )

    assert resp.uid == "faff3fdf-01b9-4c58-97dc-176c409b5bc1"
    assert resp.name == "New Multicast Address Range"
    assert resp.ipv4_address_first == "224.0.0.5"
    assert resp.ipv4_address_last == "224.0.0.5"

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-multicast-address-range",
        json=resp_multicast_address_range_ipv4,
        status=200,
    )

    resp = management.network_objects.multicast_address_range.set(
        name="New Multicast Address Range",
        ip_address_first="224.0.0.1",
        ip_address_last="224.0.0.4",
    )

    assert resp.uid == "faff3fdf-01b9-4c58-97dc-176c409b5bc1"
    assert resp.name == "New Multicast Address Range"
    assert resp.ipv4_address_first == "224.0.0.1"
    assert resp.ipv4_address_last == "224.0.0.4"

    resp = management.network_objects.multicast_address_range.set(
        name="New Multicast Address Range",
        ipv4_address_first="224.0.0.1",
        ipv4_address_last="224.0.0.4",
    )

    assert resp.uid == "faff3fdf-01b9-4c58-97dc-176c409b5bc1"
    assert resp.name == "New Multicast Address Range"
    assert resp.ipv4_address_first == "224.0.0.1"
    assert resp.ipv4_address_last == "224.0.0.4"

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-multicast-address-range",
        json=resp_multicast_address_range_ipv6,
        status=200,
    )

    resp = management.network_objects.multicast_address_range.set(
        name="New Multicast Address Range",
        ipv6_address_first="2001:db8:0000:0000:0000:0000:0000:0002",
        ipv6_address_last="2001:db8:0000:0000:0000:0000:0000:0004",
    )

    assert resp.uid == "faff3fdf-01b9-4c58-97dc-176c409b5bc1"
    assert resp.name == "New Multicast Address Range"
    assert resp.ipv6_address_first == "2001:db8:0000:0000:0000:0000:0000:0002"
    assert resp.ipv6_address_last == "2001:db8:0000:0000:0000:0000:0000:0004"

    with pytest.raises(MandatoryFieldMissing):
        management.network_objects.multicast_address_range.set()


@responses.activate
def test_delete_multicast_address_range(management, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-multicast-address-range",
        json=resp_message_ok,
        status=200,
    )

    resp = management.network_objects.multicast_address_range.delete(
        uid="faff3fdf-01b9-4c58-97dc-176c409b5bc1"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_multicast_address_ranges(management, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-multicast-address-ranges",
        json=resp_from_to_objects,
        status=200,
    )

    resp = (
        management.network_objects.multicast_address_range.show_multicast_address_ranges()
    )

    assert isinstance(resp.total, int)
