import pytest
import responses

from pycheckpoint_api.management.exception import MandatoryFieldMissing


@responses.activate
def test_add_application_site_category(management, resp_application_site_category):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-application-site-category",
        json=resp_application_site_category,
        status=200,
    )

    resp = management.service_applications.application_site_category.add(
        name="New Application Site Category 1",
        tags=["t1"],
        comments="",
        description="A custom description",
        user_defined=True,
    )

    assert resp.uid == "aa85d95a-2548-2136-aa4a-cc8a95c26d8ad92"
    assert resp.name == "New Application Site Category 1"

    # Mising mandatory parameter
    with pytest.raises(TypeError):
        management.service_applications.application_site_category.add()


@responses.activate
def test_show_application_site_category(management, resp_application_site_category):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-application-site-category",
        json=resp_application_site_category,
        status=200,
    )

    resp = management.service_applications.application_site_category.show(
        uid="aa85d95a-2548-2136-aa4a-cc8a95c26d8ad92"
    )

    assert resp.uid == "aa85d95a-2548-2136-aa4a-cc8a95c26d8ad92"
    assert resp.name == "New Application Site Category 1"


@responses.activate
def test_set_application_site_category(management, resp_application_site_category):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-application-site-category",
        json=resp_application_site_category,
        status=200,
    )

    resp = management.service_applications.application_site_category.set(
        uid="aa85d95a-2548-2136-aa4a-cc8a95c26d8ad92",
        new_name="New Application Site Category 1",
        tags=["t1"],
        description="A custom description",
    )

    assert resp.uid == "aa85d95a-2548-2136-aa4a-cc8a95c26d8ad92"
    assert resp.name == "New Application Site Category 1"

    resp = management.service_applications.application_site_category.set(
        name="New Application Site Category 1", description="A custom description"
    )

    assert resp.uid == "aa85d95a-2548-2136-aa4a-cc8a95c26d8ad92"
    assert resp.name == "New Application Site Category 1"

    # Missing mandatory field
    with pytest.raises(MandatoryFieldMissing):
        management.service_applications.application_site_category.set()


@responses.activate
def test_delete_application_site_category(management, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-application-site-category",
        json=resp_message_ok,
        status=200,
    )

    resp = management.service_applications.application_site_category.delete(
        uid="aa85d95a-2548-2136-aa4a-cc8a95c26d8ad92"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_application_sites(management, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-application-site-categories",
        json=resp_from_to_objects,
        status=200,
    )

    resp = (
        management.service_applications.application_site_category.show_application_site_categories()
    )

    assert isinstance(resp.total, int)
