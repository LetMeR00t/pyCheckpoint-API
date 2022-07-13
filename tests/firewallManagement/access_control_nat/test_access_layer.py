import responses
import pytest

from pycheckpoint_api.firewallManagement.exception import MandatoryFieldMissing


@responses.activate
def test_add_access_layer(firewallManagement, resp_access_layer):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-access-layer",
        json=resp_access_layer,
        status=200,
    )

    resp = firewallManagement.access_control_nat.access_layer.add(
        name="New Layer 1",
        add_default_rule=True,
        applications_and_url_filtering=False,
        content_awareness=False,
        detect_using_x_forward_for=True,
        firewall=True,
        mobile_access=False,
        shared=False,
        tags=["t1"],
    )

    assert resp.uid == "81530aad-bc98-4e8f-a62d-079424ddd955"
    assert resp.name == "New Layer 1"


@responses.activate
def test_show_access_layer(firewallManagement, resp_access_layer):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-access-layer",
        json=resp_access_layer,
        status=200,
    )

    resp = firewallManagement.access_control_nat.access_layer.show(
        uid="81530aad-bc98-4e8f-a62d-079424ddd955"
    )

    assert resp.uid == "81530aad-bc98-4e8f-a62d-079424ddd955"
    assert resp.name == "New Layer 1"

    resp = firewallManagement.access_control_nat.access_layer.show(name="New Layer 1")

    assert resp.uid == "81530aad-bc98-4e8f-a62d-079424ddd955"
    assert resp.name == "New Layer 1"

    # Missing mandatory parameter
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.access_control_nat.access_layer.show()


@responses.activate
def test_set_access_layer(firewallManagement, resp_access_layer):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-access-layer",
        json=resp_access_layer,
        status=200,
    )

    resp = firewallManagement.access_control_nat.access_layer.set(
        name="New Layer 1",
        add_default_rule=True,
        applications_and_url_filtering=False,
        content_awareness=False,
        detect_using_x_forward_for=True,
        firewall=True,
        mobile_access=False,
        shared=False,
        tags=["t1"],
    )

    assert resp.uid == "81530aad-bc98-4e8f-a62d-079424ddd955"
    assert resp.name == "New Layer 1"

    resp = firewallManagement.access_control_nat.access_layer.set(
        uid="81530aad-bc98-4e8f-a62d-079424ddd955",
        new_name="New Layer 1",
    )

    assert resp.uid == "81530aad-bc98-4e8f-a62d-079424ddd955"
    assert resp.name == "New Layer 1"

    # Missing mandatory parameter
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.access_control_nat.access_layer.set()


@responses.activate
def test_delete_access_layer(firewallManagement, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-access-layer",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.access_control_nat.access_layer.delete(
        layer="Network", uid="81530aad-bc98-4e8f-a62d-079424ddd955"
    )

    assert resp.message == "OK"

    resp = firewallManagement.access_control_nat.access_layer.delete(
        layer="Network", name="New Layer 1"
    )

    assert resp.message == "OK"

    # Missing mandatory parameter
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.access_control_nat.access_layer.delete()


@responses.activate
def test_show_access_layers(firewallManagement, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-access-layers",
        json=resp_from_to_objects,
        status=200,
    )

    resp = firewallManagement.access_control_nat.access_layer.show_access_layers(
        offset=0,
        limit=20,
        order={"ASC": "name"},
        details_level="standard",
        filter_results="",
    )

    assert isinstance(resp.total, int)
