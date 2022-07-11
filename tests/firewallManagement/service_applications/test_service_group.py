import responses
import pytest

from pycheckpoint_api.firewallManagement.exception import MandatoryFieldMissing


@responses.activate
def test_add_service_group(firewallManagement, resp_service_group):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-service-group",
        json=resp_service_group,
        status=200,
    )

    resp = firewallManagement.service_applications.service_group.add(
        name="New Service Group 3",
        members=["New Host 1", "My Test Host 3"],
        tags=["t1"],
    )

    assert resp.uid == "dce67d0d-5efe-4808-b22d-2eb99e24c70d"
    assert resp.name == "New Service Group 3"

    # None arguments
    with pytest.raises(TypeError):
        firewallManagement.service_applications.service_group.add()


@responses.activate
def test_show_service_group(firewallManagement, resp_service_group):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-service-group",
        json=resp_service_group,
        status=200,
    )

    resp = firewallManagement.service_applications.service_group.show(
        uid="dce67d0d-5efe-4808-b22d-2eb99e24c70d"
    )

    assert resp.uid == "dce67d0d-5efe-4808-b22d-2eb99e24c70d"
    assert resp.name == "New Service Group 3"


@responses.activate
def test_set_service_group(firewallManagement, resp_service_group):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-service-group",
        json=resp_service_group,
        status=200,
    )

    resp = firewallManagement.service_applications.service_group.set(
        uid="dce67d0d-5efe-4808-b22d-2eb99e24c70d",
        new_name="New Service Group 3",
        members=["https"],
        groups=["My Service Group1", "My Service Group2"],
        tags=["t1"],
    )

    assert resp.uid == "dce67d0d-5efe-4808-b22d-2eb99e24c70d"
    assert resp.name == "New Service Group 3"

    resp = firewallManagement.service_applications.service_group.set(
        name="Old Name Group 3", new_name="New Service Group 3"
    )

    assert resp.uid == "dce67d0d-5efe-4808-b22d-2eb99e24c70d"
    assert resp.name == "New Service Group 3"

    # None arguments
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.service_applications.service_group.set()


@responses.activate
def test_delete_service_group(firewallManagement, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-service-group",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.service_applications.service_group.delete(
        uid="dce67d0d-5efe-4808-b22d-2eb99e24c70d"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_service_groups(firewallManagement, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-service-groups",
        json=resp_from_to_objects,
        status=200,
    )

    resp = firewallManagement.service_applications.service_group.show_service_groups()

    assert isinstance(resp.total, int)
