import pytest
import responses

from pycheckpoint_api.firewallManagement.exception import MandatoryFieldMissing


@responses.activate
def test_add_access_point_name(firewallManagement, resp_access_point_name):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-access-point-name",
        json=resp_access_point_name,
        status=200,
    )

    resp = firewallManagement.network_objects.access_point_name.add(
        name="myaccesspointname",
        apn="apnname",
        enforce_end_user_domain=True,
        end_user_domain="All_Internet",
        block_traffic_other_end_user_domains=True,
        block_traffic_this_end_user_domain=True,
        tags=["t1"],
    )

    assert resp.uid == "5064644d-6cc7-4703-823c-54f01ab720e6"
    assert resp.name == "myaccesspointname"


@responses.activate
def test_show_access_point_name(firewallManagement, resp_access_point_name):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-access-point-name",
        json=resp_access_point_name,
        status=200,
    )

    resp = firewallManagement.network_objects.access_point_name.show(
        uid="5064644d-6cc7-4703-823c-54f01ab720e6"
    )

    assert resp.uid == "5064644d-6cc7-4703-823c-54f01ab720e6"
    assert resp.name == "myaccesspointname"


@responses.activate
def test_set_access_point_name(firewallManagement, resp_access_point_name):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-access-point-name",
        json=resp_access_point_name,
        status=200,
    )

    resp = firewallManagement.network_objects.access_point_name.set(
        uid="5064644d-6cc7-4703-823c-54f01ab720e6", new_name="myaccesspointname"
    )

    assert resp.uid == "5064644d-6cc7-4703-823c-54f01ab720e6"
    assert resp.name == "myaccesspointname"

    resp = firewallManagement.network_objects.access_point_name.set(
        name="myaccesspointname_oldname",
        new_name="myaccesspointname",
        tags=["t1"],
        apn="apnname",
        enforce_end_user_domain=True,
        block_traffic_other_end_user_domains=True,
        block_traffic_this_end_user_domain=True,
        end_user_domain="b307ca15-2ee8-414a-b261-ac7fb7464736",
    )

    assert resp.uid == "5064644d-6cc7-4703-823c-54f01ab720e6"
    assert resp.name == "myaccesspointname"

    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.network_objects.access_point_name.set()


@responses.activate
def test_delete_access_point_name(firewallManagement, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-access-point-name",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.network_objects.access_point_name.delete(
        uid="5064644d-6cc7-4703-823c-54f01ab720e6"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_access_point_names(firewallManagement, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-access-point-names",
        json=resp_from_to_objects,
        status=200,
    )

    resp = (
        firewallManagement.network_objects.access_point_name.show_access_point_names()
    )

    assert isinstance(resp.total, int)
