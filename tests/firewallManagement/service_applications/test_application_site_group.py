import responses
import pytest

from pycheckpoint_api.firewallManagement.exception import MandatoryFieldMissing


@responses.activate
def test_add_application_site_group(firewallManagement, resp_application_site_group):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-application-site-group",
        json=resp_application_site_group,
        status=200,
    )

    resp = firewallManagement.service_applications.application_site_group.add(
        name="New Application Site Group 1",
        members=[
            "facebook",
            "Social Networking",
            "New Application Site 1",
            "New Application Site Category 1",
        ],
        tags=["t1"],
    )

    assert resp.uid == "5a2d5c36-1998-2022-acce-a5c3b699d522"
    assert resp.name == "New Application Site Group 1"

    # None arguments
    with pytest.raises(TypeError):
        firewallManagement.service_applications.application_site_group.add()


@responses.activate
def test_show_application_site_group(firewallManagement, resp_application_site_group):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-application-site-group",
        json=resp_application_site_group,
        status=200,
    )

    resp = firewallManagement.service_applications.application_site_group.show(
        uid="5a2d5c36-1998-2022-acce-a5c3b699d522"
    )

    assert resp.uid == "5a2d5c36-1998-2022-acce-a5c3b699d522"
    assert resp.name == "New Application Site Group 1"


@responses.activate
def test_set_application_site_group(firewallManagement, resp_application_site_group):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-application-site-group",
        json=resp_application_site_group,
        status=200,
    )

    resp = firewallManagement.service_applications.application_site_group.set(
        uid="5a2d5c36-1998-2022-acce-a5c3b699d522",
        new_name="New Application Site Group 1",
        members=["https"],
        groups=["My Service Group1", "My Service Group2"],
        tags=["t1"],
    )

    assert resp.uid == "5a2d5c36-1998-2022-acce-a5c3b699d522"
    assert resp.name == "New Application Site Group 1"

    resp = firewallManagement.service_applications.application_site_group.set(
        name="Old Name Group 3", new_name="New Application Site Group 1"
    )

    assert resp.uid == "5a2d5c36-1998-2022-acce-a5c3b699d522"
    assert resp.name == "New Application Site Group 1"

    # None arguments
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.service_applications.application_site_group.set()


@responses.activate
def test_delete_application_site_group(firewallManagement, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-application-site-group",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.service_applications.application_site_group.delete(
        uid="5a2d5c36-1998-2022-acce-a5c3b699d522"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_application_site_groups(firewallManagement, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-application-site-groups",
        json=resp_from_to_objects,
        status=200,
    )

    resp = (
        firewallManagement.service_applications.application_site_group.show_application_site_groups()
    )

    assert isinstance(resp.total, int)
