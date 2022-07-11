import responses
import pytest

from pycheckpoint_api.firewallManagement.exception import MandatoryFieldMissing


@responses.activate
def test_add_application_site(firewallManagement, resp_application_site):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-application-site",
        json=resp_application_site,
        status=200,
    )

    resp = firewallManagement.service_applications.application_site.add(
        name="New Application Site 1",
        tags=["t1"],
        comments="",
        additional_categories=[],
        application_id=15874256,
        description="A custom description",
        groups=[
            {
                "folder": {
                    "uid": "5568324a-68ed-4c6c-9aa6-553978c7e746",
                    "name": "/Global Objects",
                },
                "domain": {
                    "domain-type": "local domain",
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                },
                "type": "application-site",
                "name": "My Service Group1",
                "uid": "70600af1-3e61-41e2-b031-d46b2a171f86",
            },
            {
                "folder": {
                    "uid": "5568324a-68ed-4c6c-9aa6-553978c7e746",
                    "name": "/Global Objects",
                },
                "domain": {
                    "domain-type": "local domain",
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                },
                "type": "application-site",
                "name": "My Service Group2",
                "uid": "e971be7e-8372-475f-9863-c0b0c5285cc0",
            },
        ],
        primary_category="Anonymizer",
        risk="",
        url_list=["www.4dz84zd39f9az26rh4hz64.com"],
        urls_defined_as_regular_expression=False,
        user_defined=True,
    )

    assert resp.uid == "ded526ad-5d62-a851-2523-d3ac26998ef3"
    assert resp.name == "New Application Site 1"

    resp = firewallManagement.service_applications.application_site.add(
        name="New Application Site 1",
        primary_category="Anonymizer",
        application_signature="^games\\.yahoo\\.com$",
    )

    assert resp.uid == "ded526ad-5d62-a851-2523-d3ac26998ef3"
    assert resp.name == "New Application Site 1"

    # Mising mandatory parameter
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.service_applications.application_site.add(
            name="New Application Site 1",
            primary_category="Anonymizer",
        )


@responses.activate
def test_show_application_site(firewallManagement, resp_application_site):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-application-site",
        json=resp_application_site,
        status=200,
    )

    resp = firewallManagement.service_applications.application_site.show(
        uid="ded526ad-5d62-a851-2523-d3ac26998ef3"
    )

    assert resp.uid == "ded526ad-5d62-a851-2523-d3ac26998ef3"
    assert resp.name == "New Application Site 1"


@responses.activate
def test_set_application_site(firewallManagement, resp_application_site):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-application-site",
        json=resp_application_site,
        status=200,
    )

    resp = firewallManagement.service_applications.application_site.set(
        uid="ded526ad-5d62-a851-2523-d3ac26998ef3",
        new_name="New Application Site 1",
        tags=["t1"],
        comments="",
        additional_categories=[],
        application_id=15874256,
        description="A custom description",
        groups=[
            {
                "folder": {
                    "uid": "5568324a-68ed-4c6c-9aa6-553978c7e746",
                    "name": "/Global Objects",
                },
                "domain": {
                    "domain-type": "local domain",
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                },
                "type": "application-site",
                "name": "My Service Group1",
                "uid": "70600af1-3e61-41e2-b031-d46b2a171f86",
            },
            {
                "folder": {
                    "uid": "5568324a-68ed-4c6c-9aa6-553978c7e746",
                    "name": "/Global Objects",
                },
                "domain": {
                    "domain-type": "local domain",
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                },
                "type": "application-site",
                "name": "My Service Group2",
                "uid": "e971be7e-8372-475f-9863-c0b0c5285cc0",
            },
        ],
        primary_category="Anonymizer",
        risk="",
        url_list=["www.4dz84zd39f9az26rh4hz64.com"],
        urls_defined_as_regular_expression=False,
        user_defined=True,
    )

    assert resp.uid == "ded526ad-5d62-a851-2523-d3ac26998ef3"
    assert resp.name == "New Application Site 1"

    resp = firewallManagement.service_applications.application_site.set(
        name="New Application Site 1",
        primary_category="Anonymizer",
        application_signature="^games\\.yahoo\\.com$",
    )

    assert resp.uid == "ded526ad-5d62-a851-2523-d3ac26998ef3"
    assert resp.name == "New Application Site 1"

    # Missing mandatory field
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.service_applications.application_site.set()


@responses.activate
def test_delete_application_site(firewallManagement, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-application-site",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.service_applications.application_site.delete(
        uid="ded526ad-5d62-a851-2523-d3ac26998ef3"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_application_sites(firewallManagement, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-application-sites",
        json=resp_from_to_objects,
        status=200,
    )

    resp = (
        firewallManagement.service_applications.application_site.show_application_sites()
    )

    assert isinstance(resp.total, int)
