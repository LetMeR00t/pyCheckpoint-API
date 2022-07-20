import pytest
import responses

from pycheckpoint_api.firewallManagement.exception import MandatoryFieldMissing


@responses.activate
def test_add_lsm_gateway(firewallManagement, resp_lsm_gateway):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-lsm-gateway",
        json=resp_lsm_gateway,
        status=200,
    )

    resp = firewallManagement.network_objects.lsm_gateway.add(
        name="lsm_gateway",
        security_profile="lsm_profile",
        sic={"ip-address": "1.2.3.4", "one-time-password": "aaaa"},
        provisioning_state="using-profile",
        provisioning_settings={"provisioning-profile": "prv_profile"},
        tags=["t1"],
    )

    assert resp.uid == "f3b6df08-d973-4f16-8cfb-1f9562c6d120"
    assert resp.name == "lsm_gateway"


@responses.activate
def test_show_lsm_gateway(firewallManagement, resp_lsm_gateway):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-lsm-gateway",
        json=resp_lsm_gateway,
        status=200,
    )

    resp = firewallManagement.network_objects.lsm_gateway.show(
        uid="f3b6df08-d973-4f16-8cfb-1f9562c6d120"
    )

    assert resp.uid == "f3b6df08-d973-4f16-8cfb-1f9562c6d120"
    assert resp.name == "lsm_gateway"


@responses.activate
def test_set_lsm_gateway(firewallManagement, resp_lsm_gateway):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-lsm-gateway",
        json=resp_lsm_gateway,
        status=200,
    )

    resp = firewallManagement.network_objects.lsm_gateway.set(
        uid="f3b6df08-d973-4f16-8cfb-1f9562c6d120",
        new_name="lsm_gateway",
        security_profile="lsm_profile",
        sic={"ip-address": "1.2.3.4", "one-time-password": "aaaa"},
        provisioning_state="using-profile",
        provisioning_settings={"provisioning-profile": "prv_profile"},
        tags=["t1"],
    )

    assert resp.uid == "f3b6df08-d973-4f16-8cfb-1f9562c6d120"
    assert resp.name == "lsm_gateway"

    resp = firewallManagement.network_objects.lsm_gateway.set(
        name="lsm_gateway old", new_name="lsm_gateway"
    )

    assert resp.uid == "f3b6df08-d973-4f16-8cfb-1f9562c6d120"
    assert resp.name == "lsm_gateway"

    # Missing name or UID information
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.network_objects.lsm_gateway.set()


@responses.activate
def test_delete_lsm_gateway(firewallManagement, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-lsm-gateway",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.network_objects.lsm_gateway.delete(
        uid="f3b6df08-d973-4f16-8cfb-1f9562c6d120"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_lsm_gateways(firewallManagement, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-lsm-gateways",
        json=resp_from_to_objects,
        status=200,
    )

    resp = firewallManagement.network_objects.lsm_gateway.show_lsm_gateways()

    assert isinstance(resp.total, int)
