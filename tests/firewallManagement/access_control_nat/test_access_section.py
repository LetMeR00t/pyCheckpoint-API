import responses
import pytest

from pycheckpoint_api.firewallManagement.exception import MandatoryFieldMissing


@responses.activate
def test_add_access_section(firewallManagement, resp_access_section):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-access-section",
        json=resp_access_section,
        status=200,
    )

    resp = firewallManagement.access_control_nat.access_section.add(
        layer="Network",
        position=1,
        name="New Section 1",
    )

    assert resp.uid == "aa5d88e9-a589-abba-1471-5d6988519a26"
    assert resp.name == "New Section 1"


@responses.activate
def test_show_access_section(firewallManagement, resp_access_section):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-access-section",
        json=resp_access_section,
        status=200,
    )

    resp = firewallManagement.access_control_nat.access_section.show(
        uid="aa5d88e9-a589-abba-1471-5d6988519a26", layer="MyLayer"
    )

    assert resp.uid == "aa5d88e9-a589-abba-1471-5d6988519a26"
    assert resp.name == "New Section 1"

    resp = firewallManagement.access_control_nat.access_section.show(
        name="My Rule", layer="MyLayer"
    )

    assert resp.uid == "aa5d88e9-a589-abba-1471-5d6988519a26"
    assert resp.name == "New Section 1"

    # Missing mandatory parameter
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.access_control_nat.access_section.show(layer="Network")


@responses.activate
def test_set_access_section(firewallManagement, resp_access_section):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-access-section",
        json=resp_access_section,
        status=200,
    )

    resp = firewallManagement.access_control_nat.access_section.set(
        layer="Network",
        uid="aa5d88e9-a589-abba-1471-5d6988519a26",
        new_name="New Section 1",
    )

    assert resp.uid == "aa5d88e9-a589-abba-1471-5d6988519a26"
    assert resp.name == "New Section 1"

    resp = firewallManagement.access_control_nat.access_section.set(
        layer="Network", name="New Section 1 Old", new_name="New Section 1"
    )

    assert resp.uid == "aa5d88e9-a589-abba-1471-5d6988519a26"
    assert resp.name == "New Section 1"

    # Missing mandatory parameter
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.access_control_nat.access_section.set(layer="Network")


@responses.activate
def test_delete_access_section(firewallManagement, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-access-section",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.access_control_nat.access_section.delete(
        layer="Network", uid="aa5d88e9-a589-abba-1471-5d6988519a26"
    )

    assert resp.message == "OK"

    resp = firewallManagement.access_control_nat.access_section.delete(
        layer="Network", name="New Section 1"
    )

    assert resp.message == "OK"

    # Missing mandatory parameter
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.access_control_nat.access_section.delete(layer="Network")
